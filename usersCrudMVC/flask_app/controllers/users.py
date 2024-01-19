# MVC (Models Views Controllers)
# Modularization
# Step 2: Controllers
# (Controllers interact as the Mediator between the Client side and Back end, It directs the requests and serves the web pages as routes are requested
# and Calls the methods executed by the Class Model)

# 3. Create a .py file named after what ever we are controlling in a pluralization form

# 4. Move all the @app.route functions into the controller file
# 5. Insert this code in the controllers file
from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models.user import Users # import model database class from models folder
# 6. Remove above code from server.py

# 5. Have the controller call the model class methods Class from Step 3: Models
# 6. Update the Model class import statement in the controller to import model from correct model folder

# All Home links should redirect to the Read (All) page
@app.route('/')
def root():
    return redirect('/users')

# Display all users from the database on the Read (All) page
# All Home links should redirect to the Read (All) page
@app.route('/users')
def users():
    users = Users.get_all()
    print("View Page for All Users")
    return render_template('show (all).html', users = users)

@app.route('/users/new')
def users_new():
    print("Create Page for New User")
    return render_template('create (one).html')

# Display form to create new users on the Create page
# When the form is submitted, a new user should be inserted into the database
# After successful creation of a new User, redirect to Read (One) page
@app.route('/users/process', methods = ['post'])
def users_process():
    data = {}
    data['first_name'] = request.form['first_name']
    data['last_name'] = request.form['last_name']
    data['email'] = request.form['email']
    user_id = Users.save(data)
    session['user_id'] = user_id
    print(f"User with id {user_id} created.")
    return redirect('/users/show')

# Show link will render the Users Read (One) page
# After successful creation of a new User, redirect to Read (One) page
# Read (One) page will display the User's information
@app.route('/users/show/')
def users_show():
    data = {}
    data['user_id'] = session['user_id']
    session.clear()
    user = Users.get_one(data)
    print(f"Showing View Page for User with id {data['user_id']}")
    return render_template('show (one).html', user = user)

# Show link will render the Users Read (One) page
# Read (One) page will display the User's information
@app.route('/users/show/<user_id>')
def users_show_user_id(user_id):
    data = {}
    data['user_id'] = user_id
    user = Users.get_one(data)
    print(f"Showing View Page for User with id {data['user_id']}")
    return render_template('show (one).html', user = user)

# Edit link will render the Users Edit page
# Edit page will have a form pre-populated with the users information
# Update the updated_at field when editing the User's information
@app.route('/users/edit/<user_id>')
def users_edit_user_id(user_id):
    data = {}
    data['user_id'] = user_id
    user = Users.get_one(data)
    print(f"Showing Edit Page for User with id {data['user_id']}")
    return render_template('edit (one).html', user = user)

# Edit link will render the Users Edit page
# Edit page will have a form pre-populated with the users information
# Update the updated_at field when editing the User's information
# After successful update of user, redirect to the Read (One) page and display the updated information
@app.route('/users/edit/process/<user_id>', methods = ['post'])
def users_edit_process_user_id(user_id):
    data = {}
    data['user_id'] = user_id
    data['first_name'] = request.form['first_name']
    data['last_name'] = request.form['last_name']
    data['email'] = request.form['email']
    session['user_id'] = user_id
    Users.update(data) #MySQL Update set to update DATETIME Stamp ON Update by Default
    print(f"Update made on User with id {data['user_id']}")
    return redirect('/users/show')

# Delete link will delete the User from the database, and redirect to the Read (All) page
@app.route('/users/delete/<user_id>')
def users_delete_user_id(user_id):
    data = {}
    data['user_id'] = user_id
    user = Users.get_one(data)
    print(f"Show User with id {user_id} for Delete Confirmation")
    return render_template('delete (one).html', user = user)

# Delete link will delete the User from the database, and redirect to the Read (All) page
@app.route('/users/delete/process/<user_id>')
def users_delete_process_user_id(user_id):
    data = {}
    data['user_id'] = user_id
    Users.delete(data)
    print(f"Deleted User with id {user_id}")
    return redirect('/users')

