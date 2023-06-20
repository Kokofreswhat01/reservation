from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
db = SQLAlchemy()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'  # Configuration de la base de données SQLite


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=False, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.email


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/coon', methods=['POST', 'GET'])
def coon():
    if request.method == 'POST':
        # Récupérer les valeurs du formulaire
        email = request.form.get('email')
        password = request.form.get('mot_de_passe')

        # Vérifier les informations de connexion
        user = User.query.filter_by(email=email).first()

        # Si les informations sont valides, rediriger vers la page d'accueil
        if user and user.password == password:
            return render_template('HTML/taxi.html')
    return render_template('HTML/coon.html')
    #return render_template('index.html')


@app.route('/inscri', methods=['POST', 'GET'])
def inscri():
    if request.method == 'POST':
        name = request.form.get('nom')
        email = request.form.get('email')
        password = request.form.get('mot_de_passe')
        new_user = User(name=name, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
        return render_template('HTML/coon.html')
    return render_template('HTML/inscri.html')

@app.route('/logout')
def logout():
    # Supprimez l'utilisateur de la session pour le déconnecter
    db.session.pop('username', None)
    return redirect(url_for('coon'))


@app.route('/contt', methods=['GET', 'POST'])
def contt():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        numero = request.form.get('numero')
        objet = request.form.get('objet')
        message = request.form.get('message')

        # Traitez les données du formulaire de contact, par exemple, envoyez un e-mail, enregistrez-les dans une base de données, etc.

        thank_you_message = f"Merci {name} pour votre message. Nous vous contacterons bientôt."
        return render_template('HTML/contt.html', thank_you_message=thank_you_message)

    return render_template('HTML/contt.html')


@app.route('/coon/taxi')
def taxi():
    return render_template('HTML/taxi.html')


@app.route('/coon/taxi/voit_car')
def voit_car():
    return render_template('HTML/voit_car.html')


@app.route('/coon/taxi', methods=['GET', 'POST'])
def rdv_taxi():
    if request.method == 'POST':
        lieu_attente = request.form['lieu_attente']
        destination = request.form['destination']
        date = request.form['startDate']
        heure_rdv = request.form['heure_rdv']
        passagers = request.form['passagers']
        
        # Faites ce que vous voulez avec les valeurs récupérées du formulaire
        
        return "Données du formulaire envoyées avec succès!"
    
    return render_template('HTML/taxi.html')


@app.route('/coon/taxi/voit_car', methods=['GET', 'POST'])
def rdv_voit_car():
    if request.method == 'POST':
        lieu_attente = request.form['lieu_att']
        type_voiture = request.form['car_voit']
        date = request.form['startDate']
        heure_rdv = request.form['rdv']
        date_remise = request.form['date_remise']
        heure_remise = request.form['heure_re']
        
        # Faites ce que vous voulez avec les valeurs récupérées du formulaire
        
        return "Données du formulaire envoyées avec succès!"
    
    return render_template('HTML/voit_car.html')


db.init_app(app)
if __name__ == "__main__":
    db.create_all()
    app.run()
