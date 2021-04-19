#  AmazRT  -  Parcel Management System
#  First semester Technical Degree project
#
#    Copyright  (c) 2021 - 2022
#   - Meryem KAYA @MeryemKy
#   - Alexis LEBEL @Alestrio
#   - Malo LEGRAND @HoesMaaad

#  AmazRT  -  Parcel Management System
#  First semester Technical Degree project
#
from application import Base, engine, Session
from application.tests.data.entities import actions_test, platforms_test, misc_test, people_test
from application.util.config import test_motd


def execute_all_tests():
    print(test_motd)
    Base.metadata.create_all(engine)

    session = Session()

    platforms_test.execute_test(session)
    people_test.execute_test(session)
    misc_test.execute_test(session)
    actions_test.execute_test(session)


if __name__ == '__main__':
    execute_all_tests()
