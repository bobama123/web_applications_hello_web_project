import os
from flask import Flask, request

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

@app.route('/submit', methods=['POST'])
def post_submit():
    name = request.form['name']
    message = request.form['message']

    return f'Thanks {name}, you sent this message: "{message}"'

@app.route('/wave', methods=['GET'])
def get_wave():
    name = request.args['name']

    return f"I am waving at {name}"

# == Example Code Below ==

# GET /emoji
# Returns a emojiy face
# Try it:
#   ; curl http://127.0.0.1:5001/emoji
@app.route('/emoji', methods=['GET'])
def get_emoji():
    return ":)"

@app.route('/count_vowels', methods=['POST'])
def post_count_vowels():
    text = request.form['text']
    vowel_number = 0
    for character in text:
        if character in 'aeiou':
            vowel_number += 1
    
    return f'There are {vowel_number} vowels in "{text}"'

@app.route('/sort_names', methods=['POST'])
def post_sort_names():
    names = request.form['names']
    names_list = names.split(",")
    sort_list = sorted(names_list)
    string = ",".join(sort_list)
    return string

@app.route('/add', methods=['GET'])
def post_add_name():
    name = request.args['name']
    names = 'Julia, Alice, Karim'
    return f"{names}, {name}"


# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
from example_routes import apply_example_routes
apply_example_routes(app)

# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))



