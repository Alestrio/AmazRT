#  AmazRT  -  Parcel Management System
#  First semester Technical Degree project
#
#  Copyright  (c) 2021 - 2022
#  - Meryem KAYA @MeryemKy
#  - Alexis LEBEL @Alestrio
#  - Malo LEGRAND @HoesMaaad



from backend import app
from backend.data.services.UserService import UserService

@app.route("/")
@app.route("/accueil")
def accueil():
    return 'Nous venons de créer notre première application Flask'

@app.route("/parcel/all")
def getAllParcels():
    return "jsonify(service.findAll())"
