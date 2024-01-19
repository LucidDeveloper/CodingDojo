# Create a new Flask project
# MVC (Models Views Controllers)
# Modularization
# Step 1: The App Folder


# 7. Add this line to server.py from Step 2: Controllers
from flask_app.controllers import users # import controllers to be used with app
# 5. Add this code to server. py
from flask_app import app # import app to be used with virtual server

if __name__ == '__main__': # run Flask app on debug mode in order to run virtual server
    app.run(debug = True) 

# 6. Move templates folder into flask_app
# 7. Move static folder into flask_app