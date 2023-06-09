from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # Configuration de la base de données SQLite
db = SQLAlchemy(app)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/connexion')
def connexion():
    email = request.form.get('email')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first()
    if user and user.password == password:
        return "Connexion réussie pour l'utilisateur : {}".format(email)
    else:
        return "Email ou mot de passe incorrect.", 401


@app.route('/inscription')
def inscription():
    return render_template('inscription.html')

@app.route('/contact')
def contact():
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




class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.email

@app.route('/connexion', methods=['POST'])
def connexion():
    email = request.form.get('email')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first()

    if user and user.password == password:
        return "Connexion réussie pour l'utilisateur : {}".format(email)
    else:
        return "Email ou mot de passe incorrect.", 401

if __name__ == '__main__':
    
    app.run()
