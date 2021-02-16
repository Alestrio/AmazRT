# AmazRT

This is the second semester project code repository for Technical Degree students in Networking and Telecommunications.
It is a Parcel Management System.

## Structure
This project is composed by a frontend, the UI the user interacts with, and a backend, which is the api 
used by the frontend, and an internal stock management system.

## Backend 

The backend uses Flask as the main API framework. The database is a PostgreSQL database.

There are several kinds of file :

### Flask :

|File name|Use case
|---|---
|[run.py](backend/run.py)|Main entry point of the app

### Services :
Those are files intended to work with the SQLService class. Those are the interfaces between the database and the
programm in itself.

|File name|Use case
|---|-------
|[base.py](backend/data/base.py)|This is the interface between the services and the database

### Entities :
Those files are the data models used by the programm :

|File name|Use case
|----|----
|[AbstractEntity.py](backend/data/entities/AbstractEntity.py)|This is the superclass of all the entities
|[Parcel.py](backend/data/entities/Parcel.py)|This is the data model of a Parcel
|[Tracking.py](backend/data/entities/Tracking.py)|This is the data model of tracking information
|[User.py](backend/data/entities/User.py)|This is the data model of user information

### Routes:
Those files are api routes

|File name|Use case
|---|---
|[ParcelRoute.py](backend/routes/ParcelRoute.py)|This file contains the routes related to Parcel information
|[TrackingRoute.py](backend/routes/TrackingRoute.py)|This file contains the routes related to Tracking information
|[UserRoute.py](backend/routes/UserRoute.py)|This file contains the routes related to user management

### Misc:
|File name|Use case
|---|---
|[config.py](backend/util/config.py)|This is the config file for the API

## Dependencies :
- Flask : `# pip3 install flask`
- Psycopg2 : `# pip3 install psycopg2-binary`
- SQLAlchemy : `# pip3 install sqlalchemy`

## Credits :
 
This project is made by :
- Alexis LEBEL @Alestrio
- Meryem Kaya @MeryemKy
- Malo Legrand @HoesMaaad
