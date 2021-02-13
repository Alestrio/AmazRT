#  AmazRT  -  Parcel Management System
#  First semester Technical Degree project
#
#  Copyright  (c) 2021 - 2022
#  - Meryem KAYA @MeryemKy
#  - Alexis LEBEL @Alestrio
#  - Malo LEGRAND @HoesMaaad
import os
import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from backend.util import config

"""
SQLService :

This is the class handling all the database operations.
The database informations are found in environment variables.
"""


class SQLService:

    Base = None

    def __init__(self):
        """
        Constructor :

        Attributes : username, password, address, port, dbname, sql, cursor
        """
        self.username = os.getenv("DB_USERNAME")
        self.password = os.getenv("DB_PW")
        self.address = os.getenv("DB_URL")
        self.port = os.getenv("DB_PORT")
        self.dbname = os.getenv("DB_NAME")
        address = f'postgresql://{self.username}:{self.password}@{self.address}:{self.port}/{self.dbname}'

        try:
            engine = create_engine(address, isolation_level='AUTOCOMMIT')
            Session = sessionmaker(bind=engine)
            self.session = Session()
            Base = declarative_base()
        except:
            print("Database connection problem")


"""def issueQueryWithResult(self, query: str):
        #This method returns the rows found by the query
        cursor = self.sql.execute(query)
        return cursor.fetchall()

    def issueQueryUpdate(self, query: str):
        #
        This method only issue a query to the db, without returning anything.
        It will be used for update/delete opoerations
        #
        cursor = self.sql.execute(query)
        try:
            cursor.commit()
        except:
            print("sql exception (commit cursor)")"""
