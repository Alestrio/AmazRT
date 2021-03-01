#  AmazRT  -  Parcel Management System
#  First semester Technical Degree project
#
#  Copyright  (c) 2021 - 2022
#  - Meryem KAYA @MeryemKy
#  - Alexis LEBEL @Alestrio
#  - Malo LEGRAND @HoesMaaad
from backend import app, Base, engine, Session
from backend.tests.data.entities import actions_test


def execute_all_tests():
    app.run(debug=True)
    Base.metadata.create_all(engine)

    session = Session()

    actions_test.execute_test(session)


if __name__ == '__main__':
    execute_all_tests()
