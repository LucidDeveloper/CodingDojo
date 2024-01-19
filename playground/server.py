# Create a new Flask project
from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', number = 0, color = 'skyblue')

# Have the /play route render a template with 3 blue boxes
@app.route('/play')
def play():
    return render_template('index.html', number = 3, color = 'skyblue')

# Have the /play/<x> route render a template with x number of blue boxes
@app.route('/play/<int:number>')
def play_number(number):
    return render_template('index.html', number = number, color = 'skyblue')

# Have the /play/<x>/<color> route render a template with x number of boxes the color of the provided value
@app.route('/play/<int:number>/<string:color>')
def play_number_color(number,color):
    return render_template('index.html', number = number, color = color)

# NINJA BONUS: Use only one template for the whole project

if __name__ == '__main__':
    app.run(debug=True)