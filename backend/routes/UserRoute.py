#  AmazRT  -  Parcel Management System
#  First semester Technical Degree project
#
#  Copyright  (c) 2021 - 2022
#  - Meryem KAYA @MeryemKy
#  - Alexis LEBEL @Alestrio
#  - Malo LEGRAND @HoesMaaad



from backend import app

@app.route("/")

@app.route("/accueil")
def accueil():
    return 'Nous venons de créer notre première application Flask'

@app.route("/user/all")
def getAllUser():
    return ""

@app.route("/user/get")
def getUserByID():
    return ""

@app.route("/user/update")
def updateUserByID():
    return ""

@app.route("/user/delete")
def deleteUserByID():
    return ""
