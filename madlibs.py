"""A madlib game that compliments its users."""

from random import choice

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]


@app.route('/')
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html",
                           person=player,
                           compliment=compliment)

@app.route('/game')
def show_madlib_form():
    """Show the madlib form"""

    game_answer = request.args.get('yes_or_no')

    if game_answer == "no":
        return render_template("goodbye.html")
    else:
        return render_template("game.html")


@app.route('/madlib')
def show_madlib():
    """Shows completed madlib"""

    person = request.args.get('person')
    color = request.args.get('color')
    noun = request.args.get('noun')
    adjective = request.args.get('adjective')
    noun_two = request.args.get('noun_two')
    monster = request.args.get('monster_name')
    number = request.args.get('number')
    miles = request.args.get('number_of_miles')
    place = request.args.get('place')
    food = request.args.get('food')

    food_list = request.args.getlist('food')

    return render_template("madlib.html",
                            person=person,
                            color=color,
                            noun=noun,
                            adjective=adjective, 
                            noun_two=noun_two,
                            monster_name=monster, 
                            number=number,
                            number_of_miles=miles,
                            place=place, 
                            food=food,
                            food_list=food_list)


if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True, host="0.0.0.0")
