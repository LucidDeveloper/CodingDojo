# Playground
* Coding Dojo Assiignment: Flask Template Engine and Jinja Syntax

# Objectives:
* Get comfortable passing information from the route to the template
* Understand how to display information passed from the route in the template file
* Get comfortable using for loops in the template file
* Get comfortable using if statements in the template file

# Tasks:

Level 1
When a user visits http://localhost:5000/play, have it render three beautiful looking blue boxes. Please use a template to render this.

Level 2
When a user visits localhost:5000/play/(x), have it display the beautiful looking blue boxes x times. For example, localhost:5000/play/7 should display these blue boxes 7 times. Calling localhost:5000/play/35 would display these blue boxes 35 times. Please remember that x originally is a string, and if you want to use it as an integer, you must first convert it to integer using int(). For example int("7") returns 7.

Level 3
When a user visits localhost:5000/play/(x)/(color), have it display beautiful looking boxes x times, but this time where the boxes appear in (color). For example, localhost:5000/play/5/green would display 5 beautiful green boxes. Calling localhost:5000/play/35/red would display 35 beautiful red boxes.


* Create a new Flask project

* Have the /play route render a template with 3 blue boxes

* Have the /play/<x> route render a template with x number of blue boxes

* Have the /play/<x>/<color> route render a template with x number of boxes the color of the provided value

* NINJA BONUS: Use only one template for the whole project