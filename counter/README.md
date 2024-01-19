# Counter
# Coding Dojo Assignment: Web Application ( Python, Flask, Jinja2, Routing, Template Rendering, Redirecting, Request, Session)

# Objectives:
* Practice using session to store data about a particular client's history with the app
* Be able to check whether a session exists
* Be able to initialize a session
* Be able to modify a session

# Goal:
* Build a flask application that counts the number of times the root route ('/') has been viewed. 
(This assignment is to test your understanding of session.)



* As part of this assignment, please start with the following features first:

localhost:5000 - have the template render the number of times the client has visited this site
localhost:5000/destroy_session - Clear the session. Once cleared, redirect to the root.

* Some Helpful Tips
We can't increment something that doesn't exist! Here's how to check if a key exists in session yet:

if 'key_name' in session:
    print('key exists!')
else:
    print("key 'key_name' does NOT exist")

* If we want to get rid of what is currently stored in session:

session.clear()		# clears all keys
session.pop('key_name')		# clears a specific key

# Tasks:
* Create a new Flask project called counter

* Have the root route render a template that displays the number of times the client has visited this site. Refresh the page several times to ensure the counter is working.

* Add a "/destroy_session" route that clears the session and redirects to the root route. Test it.

* NINJA BONUS: Add a +2 button underneath the counter and a new route that will increment the counter by 2

* NINJA BONUS: Add a Reset button to reset the counter

* SENSEI BONUS: Add a form that allows the user to specify the increment of the counter and have the counter increment accordingly

* SENSEI BONUS: Adjust your code to display both how many times the user has actually visited the page, as well as the value of the counter, given the above functionality

* SENSEI BONUS: Decode the cookie information as shown in the video