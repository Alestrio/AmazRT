#  AmazRT  -  Parcel Management System
#  First semester Technical Degree project
#
#  Copyright  (c) 2021 - 2022
#  - Meryem KAYA @MeryemKy
#  - Alexis LEBEL @Alestrio
#  - Malo LEGRAND @HoesMaaad
from backend import app, Base, engine, Session


# ----------- LEAVE TESTS -------------

def leave_dummydata():
    pass


def leave_test():
    pass


def execute_test():
    app.run(debug=True)
    Base.metadata.create_all(engine)

    session = Session()
    leave_test()


if __name__ == '__main__':
    execute_test()
