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
