#  AmazRT  -  Parcel Management System
#  First semester Technical Degree project
#
#  Copyright  (c) 2021 - 2022
#  - Meryem KAYA @MeryemKy
#  - Alexis LEBEL @Alestrio
#  - Malo LEGRAND @HoesMaaad
from datetime import date

from backend.data.entities.Parcel import Parcel
from backend.data.entities.actions.Leave import Leave
from backend.data.entities.people.Supplier import Supplier
from backend.tests.data.entities.misc_test import parcel_dummydata, parcel_removedummydata
from backend.tests.data.entities.people_test import supplier_dummydata, supplier_removedummydata


def leave_dummydata(asession):
    parcel_dummydata(asession)
    supplier_dummydata(asession)
    parcel_id = asession.query(Parcel).all()[1].id_parcel
    supplier_id = asession.query(Supplier).all()[1].id_supplier
    asession.add(
        Leave(parcel_id, 3, supplier_id, date(2021, 3, 10)))
    asession.commit()
    return parcel_id, supplier_id


def leave__removedummydata(asession, parcel, supplier):
    leaves = asession.query(Leave).all()
    for lv in leaves:
        if lv.parcel == parcel and lv.supplier == supplier and lv.pld == 3:
            asession.delete(lv)
    asession.commit()
    parcel_removedummydata(asession)
    supplier_removedummydata(asession)


def leave_test(asession):
    parcel, supplier = leave_dummydata(asession)
    leaves = asession.query(Leave).all()
    assert (leaves is not None)
    for lv in leaves:
        if lv.parcel == parcel and lv.supplier == supplier:
            assert (lv.pld == 3)
            break
    leave__removedummydata(asession, parcel, supplier)


def pull_dummydata():
    pass


def pull_removedummydata():
    pass


def pull_test():
    pass


def send_dummydata():
    pass


def send_removedummydata():
    pass


def send_test():
    pass


def transmit_dummydata():
    pass


def transmit_removedummydata():
    pass


def transmit_test():
    pass


def execute_test(asession):
    leave_test(asession)
    pull_test()
    send_test()
    transmit_test()
    print('actions tests ok')


if __name__ == '__main__':
    execute_test(asession)
