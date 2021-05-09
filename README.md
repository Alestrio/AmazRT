# AmazRT

This is the second semester project code repository for Technical Degree students in Networking and Telecommunications.
It is a Parcel Management System.

## Structure
This project is composed by a frontend, the UI the user interacts with, and a backend, which is the api.

## Backend 

The backend uses Flask as the main API framework. The database is a PostgreSQL database.

There are several kinds of file :

### Flask :

|File name|Use case
|---|---
|[run.py](application/run.py)|Main entry point of the app

### Services :
Those are files intended to work with the SQLService class. Those are the interfaces between the database and the
programm in itself.

|File name|Use case
|---|-------
|[base.py](application/data/base.py)|This is the interface between the services and the database

### Entities :
Those files are the data models used by the programm :

|File name|Use case
|----|----
|[AbstractEntity.py](application/data/entities/AbstractEntity.py)|This is the superclass of all the entities
|[City.py](application/data/entities/City.py)|This is the data model of a City
|[Parcel.py](application/data/entities/Parcel.py)|This is the data model of a parcel.
|[Leave.py](application/data/entities/actions/Leave.py)|This is the data model for parcel deposit.
|[Pull.py](application/data/entities/actions/Pull.py)|This is the data model for parcel gathering by the customer.
|[Send.py](application/data/entities/actions/Send.py)|This is the data model for parcel transmission from a PLR to a PLD.
|[Transmit.py](application/data/entities/actions/Transmit.py)|This is the data model for parcel transmission from a PLD to a PLR or another PLD.
|[Customer.py](application/data/entities/people/Customer.py)|This is the data model for a customer.
|[Operator.py](application/data/entities/people/Operator.py)|This is the data model for an operator.
|[Supplier.py](application/data/entities/people/Supplier.py)|This is the data model for a supplier.
|[Pld.py](application/data/entities/platforms/Pld.py)|This is the data model for a PLD.
|[Plr.py](application/data/entities/platforms/Plr.py)|This is the data model for a PLR.

People entities (such as Operator, Supplier and Customer) are subclasses of the UserMixin class. UserMixin implements
attributes and methods related to user management, login and register.

### Routes:

Those files are flask routes

__API routes :__

|File name|Use case
|---|---
|[ParcelRoute.py](application/routes/ParcelRoute.py)|This file contains the routes related to Parcel information
|[CityRoutes.py](application/routes/CityRoutes.py)|This file contains the routes related to Cities information
|[CustomerRoutes.py](application/routes/people/CustomerRoutes.py)|This file contains the routes related to customer management
|[OperatorRoutes.py](application/routes/people/OperatorRoutes.py)|This file contains the routes related to operator management
|[SupplierRoutes.py](application/routes/people/SupplierRoutes.py)|This file contains the routes related to supplier management
|[PldRoutes.py](application/routes/platforms/PldRoutes.py)|This file contains the routes related to PLD management
|[PlrRoutes.py](application/routes/platforms/PlrRoutes.py)|This file contains the routes related to PLR management

__Frontend routes :__

|File name|Use case
|---|---
|[index.py](application/routes/frontend/index.py)|This file contains the routes related to the index page.
|[products_services.py](application/routes/frontend/products_services.py)|This file contains the routes related to the products and services page.
|[tracking_expedition.py](application/routes/frontend/tracking_expedition.py)|This file contains the routes related to the index page.
|[common_routes.py](application/routes/frontend/common_routes.py)|This file contains the routes related to login, register, and data processing logic.

### Static :

Those are files needed by the frontend (CSS, images, enventually JS scripts)

### Templates :

Those are ressources needed by Flask to deliver the frontend. They are the base architecture of the pages.

### Tests :

Those are automated test intended to gain time by not making tests by hand.

Those tests currently supports database operations, by will soon support web operations.

### Misc:
|File name|Use case
|---|---
|[config.py](application/util/config.py)|This is the config file for the API

## Dependencies :
- Flask : `# pip3 install flask`
- Flask-wtforms : `# pip3 install flask-wtf`
- Psycopg2 : `# pip3 install psycopg2-binary`
- SQLAlchemy : `# pip3 install sqlalchemy`

## Credits :
 
This project is made by :
- Alexis LEBEL @Alestrio
- Meryem Kaya @MeryemKy
- ~~Malo Legrand @HoesMaaad~~
