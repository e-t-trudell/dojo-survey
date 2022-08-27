from multiprocessing import BoundedSemaphore
from flask import Flask, render_template, request, redirect, session


app = Flask(__name__)
app.secret_key = '0ok876bnfj367x93n5osj45bwp9cv'
# PROMPTS
# 1)Create a new Flask application

# 2)Have the root route ("/") show a page with the form

# 3)Have the "/result" route display the information from the form on a new HTML page

# 4)Put the form data into session

# Bounuses
# 1)NINJA BONUS: Use a CSS framework to style your form

# 2)NINJA BONUS: Include a set of radio buttons on your form

# 3)SENSEI BONUS: Include a set of checkboxes on your form

# homepage
@app.route('/')
def index():
    return render_template("index.html")

# go back button...doesnt work not routed correctly?
# @app.route('/restart')
# def restart():
#     session.clear()
#     return render_template('index.html')

# processing information from post request
@app.route('/process', methods=['POST'])
def process():
    session['play_one_name'] = (request.form['play_one_name'])
    session['locations'] = (request.form['locations'])
    session['languages'] = (request.form['languages'])
    session['comments'] = (request.form['comments'])
    # print((request.form['play_one_name']), (request.form['locations']),(request.form['languages']), (request.form['comments']))
    return redirect("/results")

# displaying information from session
@app.route('/results')
def result():
    return render_template("results.html")

if __name__ == "__main__":
    app.run(debug=True, port= 5002)