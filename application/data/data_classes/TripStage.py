#    AmazRT  -  Parcel Management System
#    First semester Technical Degree project
#      Copyright  (c) 2021 - 2022
#     - Meryem KAYA @MeryemKy
#     - Alexis LEBEL @Alestrio
#     - Malo LEGRAND @HoesMaaad
import datetime
import enum

from flask import jsonify

from application.data.entities.actions.Leave import Leave
from application.data.entities.actions.Pull import Pull
from application.data.entities.actions.Send import Send
from application.data.entities.actions.Transmit import Transmit


class TripStageType(enum.Enum):
    """
    @Data class - enumeration
    This is the enumeration replacing raw strings for TripStage types
    """
    LEAVE = 'leave'
    PULL = 'pull'
    SEND = 'send'
    TRANSMIT = 'transmit'


class LocationType(enum.Enum):
    """
    @Data class - enumeration
    This is the enumeration replacing raw strings for location types
    """
    PLD = 'pld'
    PLR = 'plr'
    CUSTOMER = 'customer'
    SUPPLIER = 'supplier'


class TripStage:
    """
    @Data class
    This is the class intended to store each step in a parcel transmission from the supplier to the final customer.
    To be used with FLASK and Jinja : simplifies the data manipulation.
    It stores the source, destination and dates of each stage of the delivery.
    Enumerations are used instead of raw String, to comply with the "DRY" rule.
    """
    DEFAULT_DATE = datetime.datetime.fromtimestamp(0)

    stage_id: int
    ts_type: TripStageType
    source_type: LocationType
    source: str
    destination_type: LocationType
    destination: str
    send_date: datetime.date
    reception_date: datetime.date

    def __init__(self,
                 stage_id: int, ts_type: TripStageType, source_type: LocationType, source: str,
                 destination_type: LocationType, destination: str, send_date: datetime.datetime = DEFAULT_DATE,
                 reception_date: datetime.datetime = DEFAULT_DATE):
        self.stage_id = stage_id
        self.ts_type = ts_type
        self.source_type = source_type
        self.source = source
        self.destination_type = destination_type
        self.destination = destination
        self.send_date = send_date
        self.reception_date = reception_date

    def __dict__(self):
        return {
            "stage_id": self.stage_id,
            "ts_type": self.ts_type.value,
            "source_type": self.source_type.value,
            "source": self.source,
            "destination_type": self.destination_type.value,
            "destination": self.destination,
            "send_date": self.send_date,
            "reception_date": self.reception_date
        }


def from_leave(leave: Leave):
    stage = TripStage(
        0, TripStageType.LEAVE, LocationType.SUPPLIER, leave.supplier, LocationType.PLD, leave.pld,
        reception_date=leave.deposit_date
    )
    return stage


def from_pull(stage_id, pull: Pull):
    stage = TripStage(
        stage_id, TripStageType.PULL, LocationType.PLD, pull.pld, LocationType.CUSTOMER, pull.customer,
        send_date=pull.pull_date
    )
    return stage


def from_send(stage_id, send: Send):
    if send.pld_to_plr:
        stage = TripStage(
            stage_id, TripStageType.SEND, LocationType.PLR, send.plr, LocationType.PLD, send.pld, send.send_date,
            send.reception_date
        )
    else:
        stage = TripStage(
            stage_id, TripStageType.SEND, LocationType.PLD, send.pld, LocationType.PLR, send.plr, send.send_date,
            send.reception_date
        )
    return stage


def from_transmit(stage_id, transmit: Transmit):
    stage = TripStage(
        stage_id, TripStageType.TRANSMIT, LocationType.PLR, transmit.plr, LocationType.PLR, transmit.dest_plr,
        transmit.send_date, transmit.reception_date
    )
    return stage


def orderByDate(stages: list[TripStage]()):
    ordered = [stages[0]]
    stages.pop(0)
    pull = None
    for i in stages:
        if i.ts_type != TripStageType.PULL:
            k = -1
            for j in ordered:
                if i.reception_date > j.reception_date:
                    ordered.insert(k, i)
                    break
                k -= 1
        else:
            pull = i
    if pull is not None:
        ordered.insert(-1, pull)
    return ordered
