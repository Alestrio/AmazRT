#  AmazRT  -  Parcel Management System
#  First semester Technical Degree project
#
#  Copyright  (c) 2021 - 2022
#  - Meryem KAYA @MeryemKy
#  - Alexis LEBEL @Alestrio
#  - Malo LEGRAND @HoesMaaad
from backend import app, Base, engine, Session
from backend.data.entities.platforms.Plr import Plr


def pld_dummydata(asession):
    pass


def pld_removedummydata(asession):
    pass


def pld_test(asession):
    pld_dummydata(asession)
    pld_removedummydata(asession)


def plr_test(asession):
    plrs = asession.query(Plr).all()
    # print(plrs)
    assert (plrs is not None)
    for plr in plrs:
        if plr.id_plr == 6:
            assert (plr.ref == 'plr11')
            break


def execute_test(asession):
    plr_test(asession)
    pld_test(asession)
    print('platforms tests ok')


if __name__ == '__main__':
    Base.metadata.create_all(engine)

    session = Session()
    execute_test(session)
