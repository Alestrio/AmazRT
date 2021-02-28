#  AmazRT  -  Parcel Management System
#  First semester Technical Degree project
#
#  Copyright  (c) 2021 - 2022
#  - Meryem KAYA @MeryemKy
#  - Alexis LEBEL @Alestrio
#  - Malo LEGRAND @HoesMaaad
from backend import app, Base, engine, Session


def pld_dummydata():
    pass


def pld_test():
    pass


def execute_test():
    app.run(debug=True)
    Base.metadata.create_all(engine)

    session = Session()
    pld_test()


if __name__ == '__main__':
    execute_test()
