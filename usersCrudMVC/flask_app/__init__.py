# MVC (Models Views Controllers)
# Modularization
# Step 1: The App Folder

# 1. Create a directory called flask_app

# 2. Create __init__.py file inside the flask_app folder

# Create a new Flask project

# 3. Insert this code
# 4. Remove code from server.py
from flask import Flask # import Flask to create instance of Flask to be used for app
from env import KEY # import secret Key to be used with Flask app

app = Flask(__name__)
app.secret_key = KEY