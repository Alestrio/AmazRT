#  AmazRT  -  Parcel Management System
#  First semester Technical Degree project
#
#  Copyright  (c) 2021 - 2022
#  - Meryem KAYA @MeryemKy
#  - Alexis LEBEL @Alestrio
#  - Malo LEGRAND @HoesMaaad
from backend import app, Base, engine, Session


def execute_all_tests():
    app.run(debug=True)
    Base.metadata.create_all(engine)

    session = Session()


if __name__ == '__main__':
    execute_all_tests()
