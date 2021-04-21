#  AmazRT  -  Parcel Management System
#  First semester Technical Degree project
#    Copyright  (c) 2021 - 2022
#   - Meryem KAYA @MeryemKy
#   - Alexis LEBEL @Alestrio
#   - Malo LEGRAND @HoesMaaad
from application import Base, engine, Session
from application.data.entities.City import City
from application.data.entities.Parcel import Parcel


def city_test(asession):
    cities = asession.query(City).all()
    assert (cities is not None)
    for city in cities:
        if city.id_city == 6:
            assert (city.name == 'Ambronay')
            break


def parcel_dummydata(asession):
    asession.add(Parcel('ThisIs1Ref666', 'ParceltypeGoBrrr'))
    asession.add(Parcel('ThisIsAn0th3rRef', 'ParcelTypeAgain'))
    asession.add(Parcel('LastRef4g41n', 'LastParcelType'))
    asession.commit()


def parcel_removedummydata(asession):
    parcels = asession.query(Parcel).all()
    for parcel in parcels:
        if parcel.type == 'ParceltypeGoBrrr' or parcel.type == 'ParcelTypeAgain' or parcel.type == 'LastParcelType':
            asession.delete(parcel)
    asession.commit()


def parcel_test(asession):
    parcel_dummydata(asession)
    parcels = asession.query(Parcel).all()
    assert(parcels is not None)
    for parcel in parcels:
        if parcel.type == 'ParcelTypeAgain':
            assert (parcel.ref == 'ThisIsAn0th3rRef')
            break
    parcel_removedummydata(asession)


def execute_test(asession):
    city_test(asession)
    parcel_test(asession)
    print('misc tests ok')


if __name__ == '__main__':
    Base.metadata.create_all(engine)

    session = Session()
    execute_test(session)
