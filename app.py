from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite3://base.db'  # Configuration de la base de données SQLite
db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.email


@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html')
    
@app.route('/connexion', methods=['POST', 'GET'])
def connexion():
    if request.method == 'POST':
        # Récupérer les valeurs du formulaire
        email = request.form.get('email')
        password = request.form.get('mot_de_passe')

        # Vérifier les informations de connexion
        user = User.query.filter_by(email=email).first()

        # Si les informations sont valides, rediriger vers la page d'accueil
        if user and user.password == password:
            return render_template('reservation_voit.html')
        return render_template('connexion.html')
    return render_template('index.html')


@app.route('/inscription', methods=['POST', 'GET'])
def inscription():
    if request.method == 'POST':
        name = request.form.get('Nom & Prenom')
        email = request.form.get('email')
        password = request.form.get('mot_de_passe')
        new_user = User(user=name, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
        return render_template('connexion.html')
    return render_template('inscription.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        numero = request.form.get('numero')
        objet = request.form.get('objet')
        message = request.form.get('message')

        # Traitez les données du formulaire de contact, par exemple, envoyez un e-mail, enregistrez-les dans une base de données, etc.

        thank_you_message = f"Merci {name} pour votre message. Nous vous contacterons bientôt."
        return render_template('contact.html', thank_you_message=thank_you_message)
    
    return render_template('contact.html')

@app.route('/connexion/reservation_taxi')
def reservation_taxi():
    return render_template('reservation_taxi.html')

@app.route('/connexion/reservation_taxi/reservation_voit')
def reservation_voit():
    return render_template('reservation_voit.html')

if __name__ == "__main__":
    db.create_all()
    app.run
