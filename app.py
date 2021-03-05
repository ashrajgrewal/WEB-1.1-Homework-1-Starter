from flask import Flask
from random import choice

app = Flask(__name__)


@app.route('/')
def homepage():
    """Shows a greeting to the user."""
    return 'Are you there, world? It\'s me, Ducky!'

@app.route('/animal/<users_animal>')
def favorite_animal(users_animal):
    """Display a message to the user that changes based on their favorite animal."""
    return f'Wow, {users_animal} is my favorite animal, too!'

@app.route('/dessert/<users_dessert>')
def favorite_dessert(users_dessert):
   return f"Wow, how did you know I liked {users_dessert}?"

@app.route('/madlibs/<adjective>/<noun>')
def generate_madlib(adjective, noun):
    return f"Today I went to the living room and saw a(n) {adjective} {noun} sitting on my couch!"

