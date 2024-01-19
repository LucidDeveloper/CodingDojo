# MVC (Models Views Controllers)
# Modularization
# Step 3: Models
# (Models Receives the Method Calls from the Controller and Interacts with the Database, sending and receiving the Data as it is being requested from the Controller)
# (The model contains the class which is a model of the table from the database as well as all the attributes associated with table and the class methods which act upon the attributes and intereact with the database)

# 1. Create models folder inside flask_app folder
# 2. move users.py module which holds model class Users which is model of table in database into models folder
# 3. Change the module name to singular form to represent single model
# 4. Change the import statement to import all models and classes from correct folders

from flask_app.config.mysqlconnection import connectToMySQL # import connectToMySQL function from mysqlconnection module from config folder

db = 'users_schema'

class Users:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM users;'
        results = connectToMySQL(db).query_db(query)
        users = []
        for user in results:
            users.append(cls(user))
        return users # Returns list of objects
    
    @classmethod
    def get_one(cls, data):
        query = 'SELECT * FROM users WHERE id = %(user_id)s;'
        results = connectToMySQL(db).query_db(query, data)
        users = []
        for user in results:
            users.append(cls(user))
        return users[0] # Returns object at position 1 (index 0 ) from created List of dictionaries
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, email) VALUES (%(first_name)s,%(last_name)s,%(email)s);"
        user_id = connectToMySQL(db).query_db(query, data)
        return user_id # Returns respective id of created user record
    
    @classmethod 
    def delete(cls, data):
        query = "DELETE FROM users WHERE id = %(user_id)s;"
        connectToMySQL(db).query_db(query, data)
        return
    
    @classmethod 
    def update(cls, data):
        query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s WHERE id = %(user_id)s;"
        connectToMySQL(db).query_db(query, data)
        return