#  AmazRT  -  Parcel Management System
#  First semester Technical Degree project
#    Copyright  (c) 2021 - 2022
#   - Meryem KAYA @MeryemKy
#   - Alexis LEBEL @Alestrio
#   - Malo LEGRAND @HoesMaaad
import os

from flask_wtf import CSRFProtect

from application import app
from application.data.base import Base, engine, Session

if __name__ == "__main__":
    csrf = CSRFProtect(app)
    SECRET_KEY = os.urandom(32)
    app.config['SECRET_KEY'] = SECRET_KEY
    app.config['WTF_CSRF_SECRET_KEY'] = SECRET_KEY
    csrf.init_app(app)
    app.run(debug=True)
    Base.metadata.create_all(engine)

    print('hello')

    session = Session()
    app.config['SESSION_SQLALCHEMY'] = session
