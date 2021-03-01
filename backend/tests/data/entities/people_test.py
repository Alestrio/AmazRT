#  AmazRT  -  Parcel Management System
#  First semester Technical Degree project
#
#  Copyright  (c) 2021 - 2022
#  - Meryem KAYA @MeryemKy
#  - Alexis LEBEL @Alestrio
#  - Malo LEGRAND @HoesMaaad
from backend import Base, engine, Session
from backend.data.entities.people.Customer import Customer


def customer_dummydata(asession):
    asession.add(
        Customer(6, 'aCustomerRef', 'Ecila', 'Alice', '32 Rue des Caribous 32000 Caribouville', 'login1', 'pass1'))
    asession.add(
        Customer(7, 'anoCustomerRef', 'Bob', 'Bob', '64 Avenue binaire 64000 Base2Ville', 'login2', 'pass2'))
    asession.add(
        Customer(8, 'lastCustomerRef', 'Cirdec', 'Cedric', '128 Rue du Python 42000 Pythonville', 'login3', 'pass3'))
    asession.commit()


def customer_removedummydata(asession):
    customers = asession.query(Customer).all()
    for custom in customers:
        if custom.ref == 'aCustomerRef' or custom.ref == 'anoCustomerRef' or custom.ref == 'lastCustomerRef':
            asession.delete(custom)
    asession.commit()


def customer_test(asession):
    customer_dummydata(asession)
    customers = asession.query(Customer).all()
    assert (customers is not None)
    for custom in customers:
        if custom.ref == 'anotherCustomerRef':
            assert (custom.firstname == 'Bob')
            break
    customer_removedummydata(asession)


def supplier_dummydata(asession):
    pass


def supplier_removedummydata(asession):
    pass


def supplier_test(asession):
    pass


def operator_dummydata(asession):
    pass


def operator_removedummydata(asession):
    pass


def operator_test(asession):
    pass


def execute_test(asession):
    customer_test(asession)
    supplier_test(asession)
    operator_test(asession)
    print('people tests ok')


if __name__ == '__main__':
    Base.metadata.create_all(engine)

    session = Session()
    execute_test(session)
