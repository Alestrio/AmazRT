#  AmazRT  -  Parcel Management System
#  First semester Technical Degree project
#
#  Copyright  (c) 2021 - 2022
#  - Meryem KAYA @MeryemKy
#  - Alexis LEBEL @Alestrio
#  - Malo LEGRAND @HoesMaaad

from backend import app, Base, engine, Session

if __name__ == "__main__":
    app.run(debug=True)
    Base.metadata.create_all(engine)

    print('hello')

    session = Session()
