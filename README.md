# AmazRT

This is the second semester project code repository for Technical Degree students in Networking and Telecommunications.
It is a Parcel Management System.

## Structure
This project is composed by a frontend, the UI the user interacts with, and a backend, which is the api 
used by the frontend, and an internal stock management system.

## Backend 

The backend uses Flask as the main API framework. The database is a PostgreSQL database.

There are several kinds of file :

### Services :
Those are files intended to work with the SQLService class. Those are the interfaces between the database and the
programm in itself.

|File name|Use case
|---|-------
|[backend/data/services/AbstractService.py]AbstractService.py|This is the superclass of all the services
|[backend/data/services/ParcelService.py]ParcelService.py|This is the Parcel managament service
|[backend/data/services/TrackingService.py]TrackingService.py|This is the Tracking information management service
|[backend/data/services/UserService.py]UserService.py|This is the User information management service
|[backend/data/SQLService.py]SQLService.py|This one is a litle bit special. This is the interface between the services and the database

### Entities :
Those files are the data models used by the programm :

|File name|Use case
|----|----
|[backend/data/entities/AbstractEntity.py]AbstractEntity.py|This is the superclass of all the entities
|[backend/data/entities/Parcel.py]|This is the data model of a Parcel
|[backend/data/entities/Tracking.py]|This is the data model of tracking information
|[backend/data/entities/User.py]User.py|This is the data model of user information

### Routes:
Those files are api routes

|File name|Use case
|---|---
|[backend/data/routes/ParcelRoutes.py]ParcelRoutes.py|This file contains the routes related to Parcel information
|[backend/data/routes/TrackingRoutes.py]TrackingRoutes.py|This file contains the routes related to Tracking information
|[backend/data/routes/UserRoute.py]UserRoute.py|This file contains the routes related to user management

### Misc:
|File name|Use case
|---|---
|[backend/data/util/config.py]config.py|This is the config file for the API

## Credits :
 
This project is made by :
- Alexis LEBEL @Alestrio
- Meryem Kaya @MeryemKy
- Malo Legrand @HoesMaaad
