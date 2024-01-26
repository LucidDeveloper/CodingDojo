from flask import Flask, render_template, request, redirect
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

# When the Checkout button is clicked, have the correct information 
# display on the checkout.html page
@app.route('/checkout', methods = ['post'])
def checkout():
    form = request.form
    print(form)
    time_now = datetime.datetime.now().strftime("%A, %B %d %Y at %X %p")
    strawberry_quantity = int( form['strawberry'] )
    raspberry_quantity = int( form['raspberry'] )
    apple_quantity = int( form['apple'] )
    blackberry_quantity = int( form['blackberry'] )
    first_name = form['first_name']
    last_name = form['last_name']
    student_id = form['student_id']
    total_quantity = str( int(strawberry_quantity) + int(raspberry_quantity) + int(apple_quantity) + int(blackberry_quantity) )
    # In the checkout method, add a print statement 
    # that says "Charging {{Customer name}} for {{count}} fruits"
    # While on the checkout screen, hit the refresh button in your browser. 
    # Then check your terminal--what do you notice?
    print(f'Charging {first_name} {last_name} for {total_quantity} fruits.')
    return render_template('/checkout.html', total_quantity = total_quantity, time_now = time_now, strawberry_quantity = strawberry_quantity, raspberry_quantity = raspberry_quantity, apple_quantity = apple_quantity, blackberry_quantity = blackberry_quantity, first_name = first_name, last_name = last_name, student_id = student_id)

# Display all the provided images of fruit on the fruits.html page
@app.route('/fruits')
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    