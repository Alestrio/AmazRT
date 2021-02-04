from projetflask.prj_flask import app
@app.route("/")
@app.route("/accueil")
def accueil():
    return 'Nous venons de créer notre première application Flask'