from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta


app = Flask(__name__)
db = SQLAlchemy()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'  # Configuration de la base de données SQLite
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=1)  # Durée de validité des messages flash en minutes

app.secret_key = "votre_clé_secrète"


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

@app.route('/car', methods=['GET', 'POST'])
def car():
    return render_template('HTML/car.html')


@app.route('/', methods=['GET', 'POST'])
def newsletter():
    email = request.form.get("email")
    return render_template("accueil.html", email=email)


@app.route('/coon', methods=['POST', 'GET'])
def coon():
    if request.method == 'POST':
        # Récupérer les valeurs du formulaire
        email = request.form.get('email')
        password = request.form.get('mot_de_passe')

        # Vérifier les informations de connexion
        user = User.query.filter_by(email=email).first()

        if user and user.password == password:
            # Connexion réussie, afficher un message flash avec le nom de l'utilisateur
            flash(f'Bienvenue M/Mme {user.name} !!!! Vous pouvez poursuivre vos reservations!', 'success')
            return render_template('HTML/taxi.html')

        # Informations de connexion invalides, afficher un message d'erreur
        flash('Email ou mot de passe incorrect.', 'error')

    return render_template('HTML/coon.html')


@app.route('/inscri', methods=['POST', 'GET'])
def inscri():
    if request.method == 'POST':
        name = request.form.get('nom')
        email = request.form.get('email')
        password = request.form.get('mot_de_passe')
        new_user = User(name=name, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
        flash('Inscription réussie. Vous pouvez maintenant vous connecter.', 'success')
        return render_template('HTML/coon.html')
    return render_template('HTML/inscri.html')

@app.route('/logout')
def logout():
    # Supprimez l'utilisateur de la session pour le déconnecter
    db.session.pop('name', None)
    flash('Vous avez été déconnecté avec succès!!!!', 'info')
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

        message = f"Merci {name} pour votre message. Nous vous contacterons bientôt."
        flash(message, 'success')
        return render_template('HTML/contt.html')

    return render_template('HTML/contt.html')


@app.route('/coon/taxi')
def taxi():
    #flash(f'Bienvenue, {user.name} !!!! Vous pouvez poursuivre vos reservations!', 'success')
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


@app.route('/coon/taxi/reser_taxi', methods=['GET', 'POST'])
def reser_taxi():
    if request.method == 'POST':
        nom = request.form.get('nom')
        prenom = request.form.get('prenom')
        email = request.form.get('email')
        numero = request.form.get('numero')
        pays = request.form.get('pays')
        choix = request.form.get('choix')
        
        flash('Votre réservation a été prise en compte, nous vous contacterons sous peu!', 'success')
        return render_template('HTML/reser_taxi.html')
    
    return render_template('HTML/reser_taxi.html')


db.init_app(app)
if __name__ == "__main__":
    db.create_all()
    app.run()
