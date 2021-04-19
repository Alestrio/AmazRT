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
# from application import app, Base, engine, Session
from application import app

if __name__ == "__main__":
    app.run(debug=True)
    #    Base.metadata.create_all(engine)

    print('hello')

#    session = Session()
