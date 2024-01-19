from flask import Flask

app = Flask(__name__)

# Create a root route ("/") that responds with "Hello World!"
@app.route('/')
def root():
    return 'Hello World!'

# Create a route that responds with "Dojo!"
@app.route('/dojo')
def dojo():
    return 'Dojo!'

# Create a route that responds with "Hi" and whatever name is in the URL after /say/
@app.route('/say/<name>')
def say_hi(name):
    name = name.capitalize()
    return 'Hi ' + str(name) + '!'

# Create a route that responds with the given word repeated as many times as specified in the URL
@app.route('/repeat/<num>/<word>')
def repeat_word(num,word):
    word = word.capitalize()
    return int(num) * word

# NINJA BONUS: Ensure the names provided in the 3rd task are strings
@app.route('/saystring/<string:name>')
def say_string(name):
    name = name.capitalize()
    return 'Hi ' + name + '!'

# NINJA BONUS: For the 4th task, ensure the 2nd element in the URL is an integer, and the 3rd element is a string
@app.route('/repeatintegerandstring/<int:num>/<string:name>')
def repeat_integer_and_string(num,name):
    name = name.capitalize()
    return f'{num * name}'

# SENSEI BONUS: Ensure that if the user types in any route other than the ones specified, they receive an error message saying "Sorry! No response. Try again."
@app.route('/<notListedOne>/<notListedTwo>/<notListedThree>/<notListedFour>')
def sorry_no_response_four(notListedOne,notListedTwo,notListedThree,notListedFour):
    return 'Sorry! No Response. Try again.'

@app.route('/<notListedOne>/<notListedTwo>/<notListedThree>')
def sorry_no_response_three(notListedOne,notListedTwo,notListedThree):
    return 'Sorry! No Response. Try again.'

@app.route('/<notListedOne>/<notListedTwo>')
def sorry_no_response_two(notListedOne,notListedTwo):
    return 'Sorry! No Response. Try again.'

@app.route('/<notListedOne>')
def sorry_no_response_one(notListedOne):
    return 'Sorry! No Response. Try again.'

if __name__ == '__main__':
    app.run(debug=True)