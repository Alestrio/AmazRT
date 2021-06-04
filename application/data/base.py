#  AmazRT  -  Parcel Management System
#  First semester Technical Degree project
#    Copyright  (c) 2021 - 2022
#   - Meryem KAYA @MeryemKy
#   - Alexis LEBEL @Alestrio
#   - Malo LEGRAND @HoesMaaad
import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

"""
base :

This is the module handling the database connection.
The database informations are found in environment variables.
"""

if os.getenv("DB_USERNAME") is not None:
    username = os.getenv("DB_USERNAME")
    password = os.getenv("DB_PW")
    address = os.getenv("DB_URL")
    port = os.getenv("DB_PORT")
    dbname = os.getenv("DB_NAME")
else:  # debug
    username = "api"
    password = "amazrt-api"
    address = "10.59.63.12"
    port = 5432
    dbname = 'postgres'

address = f'postgresql://{username}:{password}@{address}:{port}/{dbname}'

try:
    engine = create_engine(address, isolation_level='AUTOCOMMIT', pool_recycle=180)
    Session = sessionmaker(bind=engine)
    session = Session()
    Base = declarative_base()
except:
    print("Database connection problem")
