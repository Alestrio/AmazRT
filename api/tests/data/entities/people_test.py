#  AmazRT  -  Parcel Management System
#  First semester Technical Degree project
#    Copyright  (c) 2021 - 2022
#   - Meryem KAYA @MeryemKy
#   - Alexis LEBEL @Alestrio
#   - Malo LEGRAND @HoesMaaad
from application.data.base import Base, engine, Session
from application.data.entities.people.Customer import Customer
from application.data.entities.people.Operator import Operator
from application.data.entities.people.Supplier import Supplier


def customer_dummydata(asession):
    asession.add(
        Customer(6, 'aCustomerRef', 'Ecila', 'Alice', 'login1', 'pass1'))
    asession.add(
        Customer(7, 'anoCustomerRef', 'Bob', 'Bob', 'login2', 'pass2'))
    asession.add(
        Customer(8, 'lastCustomerRef', 'Cirdec', 'Cedric', 'login3', 'pass3'))
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
        if custom.ref == 'anoCustomerRef':
            assert (custom.firstname == 'Bob')
            break
    customer_removedummydata(asession)


def supplier_dummydata(asession):
    asession.add(
        Supplier(6, 'supplierRef', 'Toto Industries', 'toto', 'totopass', 'Cordonnier'))
    asession.add(
        Supplier(7, 'anotherRef', 'Titi Incorporate', 'titi', 'titipass', 'Coutelier'))
    asession.add(
        Supplier(8, 'lastRef', 'Tata Ltd', 'tata', 'tatapass', 'Charpentier'))
    asession.commit()


def supplier_removedummydata(asession):
    suppliers = asession.query(Supplier).all()
    for supp in suppliers:
        if supp.ref == 'supplierRef' or supp.ref == 'anotherRef' or supp.ref == 'lastRef':
            asession.delete(supp)
    asession.commit()


def supplier_test(asession):
    supplier_dummydata(asession)
    suppliers = asession.query(Supplier).all()
    assert (suppliers is not None)
    for supp in suppliers:
        if supp.ref == 'supplierRef':
            assert (supp.login == 'toto')
            break
    supplier_removedummydata(asession)


def operator_dummydata(asession):
    op = Operator(6, 'Elica', 'Alice', 'toto', 'totopass')
    op.hash_password()
    asession.add(op)
    op = Operator(7, 'Bob', 'Bob', 'titi', 'titipass')
    op.hash_password()
    asession.add(op)
    op = Operator(8, 'Cirdec', 'Cedric', 'tata', 'tatapass')
    op.hash_password()
    asession.add(op)
    asession.commit()


def operator_removedummydata(asession):
    operators = asession.query(Operator).all()
    for op in operators:
        if op.firstname == 'Alice' or op.firstname == 'Bob' or op.firstname == 'Cedric':
            asession.delete(op)
    asession.commit()


def operator_test(asession):
    operator_dummydata(asession)
    operators = asession.query(Operator).all()
    assert (operators is not None)
    for op in operators:
        if op.firstname == 'Alice':
            assert (op.login == 'toto')
            break
    operator_removedummydata(asession)


def execute_test(asession):
    customer_test(asession)
    supplier_test(asession)
    operator_test(asession)
    print('people tests ok')


if __name__ == '__main__':
    Base.metadata.create_all(engine)

    session = Session()
    execute_test(session)
