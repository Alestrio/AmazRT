#  AmazRT  -  Parcel Management System
#  First semester Technical Degree project
#    Copyright  (c) 2021 - 2022
#   - Meryem KAYA @MeryemKy
#   - Alexis LEBEL @Alestrio
#   - Malo LEGRAND @HoesMaaad

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

"""
base :

This is the module handling the database connection.
The database informations are found in environment variables.
"""

username = "api"  # os.getenv("DB_USERNAME")
password = "amazrt-api"  # os.getenv("DB_PW")
address = "10.59.63.12"  # os.getenv("DB_URL")
port = 5432  # os.getenv("DB_PORT")
dbname = 'postgres'  # os.getenv("DB_NAME")
address = f'postgresql://{username}:{password}@{address}:{port}/{dbname}'

try:
    engine = create_engine(address, isolation_level='AUTOCOMMIT')
    Session = sessionmaker(bind=engine)
    session = Session()
    Base = declarative_base()
except:
    print("Database connection problem")
