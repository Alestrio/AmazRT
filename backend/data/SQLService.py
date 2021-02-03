#  AmazRT  -  Parcel Management System
#  First semester Technical Degree project
#
#  Copyright  (c) 2021 - 2022
#  - Meryem KAYA @MeryemKy
#  - Alexis LEBEL @Alestrio
#  - Malo LEGRAND @HoesMaaad
import os
import psycopg2
from backend.util import config

"""
SQLService :

This is the class handling all the database operations.
The database informations are found in environment variables.
"""


class SQLService:

    """
    Constructor :

    Attributes : username, password, address, port, dbname, sql, cursor
    """
    def __init__(self):
        if config.isDebug:
            self.username = "postgres"
            self.password = "test"
            self.address = "localhost"
            self.port = "5432"
            self.dbname = "amazrt"
        else:
            self.username = os.getenv("DB_USER")
            self.password = os.getenv("DB_PW")
            self.address = os.getenv("DB_URL")
            self.port = os.getenv("DB_PORT")
            self.dbname = os.getenv("DB_NAME")

        self.sql = psycopg2.connect(database=self.dbname,
                                    user=self.username,
                                    host=self.address,
                                    password=self.password,
                                    port=self.port)
        self.cursor = self.sql.cursor()

    """
    Destructor :
    
    Closes the connection
    """
    def __del__(self):
        self.sql.close()
