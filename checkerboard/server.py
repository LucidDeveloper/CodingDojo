# Create a new Flask project

from flask import Flask, render_template

app = Flask(__name__)

# Have the root route render a template with a checkerboard on it
@app.route('/')
def root():
    rows = 8
    columns = 8
    color_one = 'black'
    color_two = 'red'
    return render_template('index.html', rows = rows, columns = columns, color_one = color_one, color_two = color_two)

# Have another route accept a single parameter 
# (i.e. "/<x>") and render a checkerboard with x many rows, 
# with alternating colors
@app.route('/<int:rows>')
def change_rows(rows):
    columns = 8
    color_one = 'black'
    color_two = 'red'
    return render_template('index.html', rows = rows, columns = columns, color_one = color_one, color_two = color_two)

# NINJA BONUS: Have another route accept 2 parameters 
# (i.e. "/<x>/<y>") and render a checkerboard with x rows and y columns,
# with alternating colors
@app.route('/<int:rows>/<int:columns>')
def change_rows_and_columns(rows, columns):
    color_one = 'black'
    color_two = 'red'
    return render_template('index.html', rows = rows, columns = columns, color_one = color_one, color_two = color_two)

#  NINJA BONUS: Have another route accept 3 parameters 
# (i.e. "/<x>/<y>/<color1>") and render a checkerboard with x rows, y columns, 
# and color color1 with alternating colors
@app.route('/<int:rows>/<int:columns>/<string:color_one>')
def change_color_one(rows,columns,color_one):
    color_two = 'red'
    return render_template('index.html', rows = rows, columns = columns, color_one = color_one, color_two = color_two)

# SENSEI BONUS: Have another route accept 4 parameters 
# (i.e. "/<x>/<y>/<color1>/<color2>") and render a checkerboard with x rows and
# y columns, with alternating colors, color1 and color2
@app.route('/<int:rows>/<int:columns>/<string:color_one>/<string:color_two>')
def change_color_one_and_color_two(rows, columns, color_one, color_two):
    return render_template('index.html', rows = rows, columns = columns, color_one = color_one, color_two = color_two)

if __name__ == '__main__':
    app.run(debug=True)

