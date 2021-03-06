#  AmazRT  -  Parcel Management System
#  First semester Technical Degree project
#    Copyright  (c) 2021 - 2022
#   - Meryem KAYA @MeryemKy
#   - Alexis LEBEL @Alestrio
#   - Malo LEGRAND @HoesMaaad

#  AmazRT  -  Parcel Management System
#  First semester Technical Degree project
#
#  AmazRT  -  Parcel Management System
#  First semester Technical Degree project
#
from application import Base, engine, Session  # import des composants base de données
from application.data.entities.people.Customer import Customer  # Import de la classe client
from application.data.entities.people.Operator import Operator  # import de la classe opérateur
from application.data.entities.people.Supplier import Supplier  # import de la classe fournisseur


def customer_dummydata(asession):
    asession.add(
        Customer(6, 'aCustomerRef', 'Ecila', 'Alice', '32 Rue des Caribous 32000 Caribouville', 'login1', 'pass1'))
    # Création d'un client
    asession.add(
        Customer(7, 'anoCustomerRef', 'Bob', 'Bob', '64 Avenue binaire 64000 Base2Ville', 'login2', 'pass2'))
    asession.add(
        Customer(8, 'lastCustomerRef', 'Cirdec', 'Cedric', '128 Rue du Python 42000 Pythonville', 'login3', 'pass3'))
    asession.commit()  # Envoi des données sur la base


def customer_removedummydata(asession):
    customers = asession.query(Customer).all()  # Récupération de tous les clients de la BDD
    for custom in customers:
        if custom.ref == 'aCustomerRef' or custom.ref == 'anoCustomerRef' or custom.ref == 'lastCustomerRef':
            asession.delete(custom)  # Suppression du client donné en argument
    asession.commit()  # Envoi des données sur la base


def customer_test(asession):
    customer_dummydata(asession)
    customers = asession.query(Customer).all()  # Récupération de tous les clients de la BDD
    assert (customers is not None)  # Méthode de test
    for custom in customers:
        if custom.ref == 'anoCustomerRef':
            assert (custom.firstname == 'Bob')  # Méthode de test
            break
    customer_removedummydata(asession)


def supplier_dummydata(asession):
    asession.add(
        Supplier(6, 'supplierRef', 'Toto Industries', '12 rue de Toto', 'toto', 'totopass'))
    asession.add(
        Supplier(7, 'anotherRef', 'Titi Incorporate', '42 avenue titi', 'titi', 'titipass'))
    asession.add(
        Supplier(8, 'lastRef', 'Tata Ltd', '69 boulevard tata', 'tata', 'tatapass'))
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
    asession.add(
        Operator(6, 'Elica', 'Alice', 'toto', 'totopass'))
    asession.add(
        Operator(7, 'Bob', 'Bob', 'titi', 'titipass'))
    asession.add(
        Operator(8, 'Cirdec', 'Cedric', 'tata', 'tatapass'))
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
    supplier_removedummydata(asession)


def execute_test(asession):
    customer_test(asession)
    supplier_test(asession)
    operator_test(asession)
    print('people tests ok')


if __name__ == '__main__':
    Base.metadata.create_all(engine)

    session = Session()
    execute_test(session)
