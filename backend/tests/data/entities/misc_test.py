#  AmazRT  -  Parcel Management System
#  First semester Technical Degree project
#
#  Copyright  (c) 2021 - 2022
#  - Meryem KAYA @MeryemKy
#  - Alexis LEBEL @Alestrio
#  - Malo LEGRAND @HoesMaaad
from backend import Base, engine, Session
from backend.data.entities.City import City


def city_test(asession):
    cities = asession.query(City).all()
    assert (cities is not None)
    for city in cities:
        if city.id_city == 6:
            assert (city.name == 'Ambronay')
            break


def parcel_dummydata():
    pass


def parcel_removedummydata():
    pass


def parcel_test(asession):
    pass


def execute_test(asession):
    city_test(asession)
    parcel_test(asession)
    print('misc tests ok')


if __name__ == '__main__':
    Base.metadata.create_all(engine)

    session = Session()
    execute_test(session)
