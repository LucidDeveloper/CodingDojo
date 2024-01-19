# Create a new Flask project called counter
from flask import Flask, render_template, redirect, request, session
from key import KEY

app = Flask(__name__)
app.secret_key = KEY

# Have the root route render a template that displays the number of times 
# the client has visited this site. Refresh the page several times to ensure 
# the counter is working.
# SENSEI BONUS: Adjust your code to display both how many times the user has actually visited the page, 
# as well as the value of the counter, after applying the given methods
@app.route('/')
def root():
    if 'visit_count' not in session:
        session['visit_count'] = 1
        session['total_count'] = 1
        session['increment'] = 1
    else:
        session['visit_count'] += 1
        session['total_count'] += session['increment']
    # if session == {} :
    #     session['count'] = 1
    # else:
    #     session['count'] += 1
    print('Gloabal Dictionary named Session.')
    print(session)
    print('Count of Visits to Home Page.')
    print(session['total_count'])
    return render_template('index.html', visit_count = session['visit_count'], total_count = session['total_count'])

@app.route('/count_by_one')
def count_by():
    if 'total_count' not in session:
        session['total_count'] = 1
    else:
        session['total_count'] += 1
    return render_template('index.html', visit_count = session['visit_count'], total_count = session['total_count'])

# Add a "/destroy_session" route that clears the session and
# redirects to the root route. Test it.
# NINJA BONUS: Add a Reset button to reset the counter
@app.route('/destroy_session')
def clear_count():
    session.clear()
    # session.pop('count')
    return redirect ('/')

# NINJA BONUS: Add a +2 button underneath the counter and
# a new route that will increment the counter by 2
@app.route('/count_by_two')
def count_by_2():
    if 'total_count' not in session:
        session['total_count'] = 2
    else:
        session['total_count'] += 2
    return render_template('index.html', visit_count = session['visit_count'], total_count = session['total_count'])

# SENSEI BONUS: Add a form that allows the user to 
# specify the increment of the counter and 
# have the counter increment accordingly
@app.route('/increment_by', methods = ['post'])
def increment_by():
    session['increment'] = int( request.form['increment'] )
    return redirect('/increment')

@app.route('/increment')
def increment():
    session['total_count'] += session['increment']
    return render_template('index.html', visit_count = session['visit_count'], total_count = session['total_count'])

if __name__ == '__main__':
    app.run(debug = True)