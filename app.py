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

@app.route('/multiply/<num_1>/<num_2>')
def multiply(num_1, num_2):
    if num_1.isdigit() and num_2.isdigit() == True: 
        result: int = int(num_1) * int(num_2)
        return f"The result is {result}"
    else: 
        return 'Invalid inputs. Please try again by entering 2 numbers!'

@app.route('/sayntimes/<word>/<n>')
def sayNTimes(word, n):
   n = int(n)
   repeatedWord = ''
   for i in range(n):
      repeatedWord += word
   return repeatedWord

@app.route('/dicegame')
def roll_dice():
    sides = [1, 2, 3, 4, 5, 6]
    result = choice(sides)
    if result == 6:
        return "You Rolled A 6, You Won!" 
    else: 
        return f"You Rolled a {result}, You Lose!" 

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/profile/<users_name>')
def profile(users_name):
    return "Hello " + users_name