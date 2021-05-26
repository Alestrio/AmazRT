#    AmazRT  -  Parcel Management System
#    First semester Technical Degree project
#      Copyright  (c) 2021 - 2022
#     - Meryem KAYA @MeryemKy
#     - Alexis LEBEL @Alestrio
#     - Malo LEGRAND @HoesMaaad
import datetime
import enum


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
                 stage_id:int, ts_type: TripStageType, source_type: LocationType, source: str,
                 destination_type: LocationType, destination: str, send_date: datetime.date = DEFAULT_DATE,
                 reception_date: datetime.date = DEFAULT_DATE):
        self.stage_id = stage_id
        self.ts_type = ts_type
        self.source_type = source_type
        self.source = source
        self.destination_type = destination_type
        self.destination = destination
        self.send_date = send_date
        self.reception_date = reception_date
