# Create a new Flask project called great_number_game

from flask import Flask, render_template, redirect, request, session
from env import KEY
import random

app = Flask(__name__)
app.secret_key = KEY

# In the root route, save a random number between 1 and 100 and
# display a form for the user to guess the number
# NINJA BONUS: Display the results as shown in the wireframe
# (i.e. with appropriate colors and positioning)
# NINJA BONUS: Allow the user to keep guessing until they get it correct
@app.route('/')
def root():
    if 'random_int' not in session:
        session['random_int'] = random.randint(1,100)
    if 'guess' not in session:
        session['guess'] = 0
    if 'attempts' not in session:
        session['attempts'] = 0
    return render_template('index.html', random_int = session['random_int'], guess = session['guess'], attempts = session['attempts'] )

# Create a route that determines whether the number submitted is too high,
# too low, or correct. Show this status on the HTML page.
# NINJA BONUS: Display the results as shown in the wireframe
# (i.e. with appropriate colors and positioning)
# NINJA BONUS: Allow the user to keep guessing until they get it correct
# NINJA BONUS: Let the user know how many attempts they took before
# guessing the correct number
@app.route('/process_guess', methods = ['post'])
def process_guess():
    session['guess'] = int(request.form['guess'])
    
    if 'attempts' not in session:
        session['attempts'] = 1
    else:
        session['attempts'] += 1
    return redirect('/')

@app.route('/try_again')
def try_again():
    session.clear()
    return redirect('/')

# SENSEI BONUS: If they win, allow the user to submit their name. 
# Have a link to a leaderboard page that shows winners' names and 
# how many attempts they took to guess correctly.
@app.route('/process_leaderboard', methods = ['post'])
def process_leaderboard():
    session['name'] = request.form['name']
    return redirect('/leaderboard')

# SENSEI BONUS: If they win, allow the user to submit their name. 
# Have a link to a leaderboard page that shows winners' names and 
# how many attempts they took to guess correctly.
@app.route('/leaderboard')
def leaderboard():
    return render_template('leaderboard.html', name = session['name'], attempts = session['attempts'])

if __name__ == '__main__':
    app.run( debug = True )