from flask import Flask, request, render_template, make_response
import pronotepy
from pronotepy.ent import ac_orleans_tours
import time

app = Flask(__name__)

utilisations = 10

@app.route('/', methods=['GET', 'POST'])
def login():
    global utilisations
    print(utilisations)
    if request.method == 'POST':
        # Récupérer les données du formulaire
        user_name = request.form.get('nom')
        password = request.form.get('password')

        try :

            client = pronotepy.Client(
                'https://0451526p.index-education.net/pronote/eleve.html?login=true',
                username=user_name, # votre identifiant ENT !!!
                password=password, # votre mot de passe
                ent=ac_orleans_tours)
            print('Nouvelle utilisation')
            utilisations += 1
        
        except Exception as e :
            print(e)
            return render_template('fail.html')
        
        return render_template("login.html",message="Votre moyenne générale : "+client.current_period.overall_average)
    return render_template('login.html',utilisations=str(utilisations))


@app.route('/style.css') # Mettre le css
def css():
    resp = make_response(render_template("style.css"))
    resp.headers['Content-type'] = 'text/css'
    return resp


if __name__ == '__main__':
    app.run(host = '0.0.0.0', port=80, debug = False)
