from flask import Flask, render_template

#Create a flask instance
app = Flask(__name__)

#Create a route decorator
@app.route('/')
# def index():
#     return '<h1>Hello World!<h1>'
#FILTERS
# safe
# capitalize
# lower
# upper
# title
# trim
# striptags


def index():
    first_name = "John"
    stuff="This is bold text"
    favorite_pizza=["Pepperoni","Cheese","Mushroom", 45]
    return render_template("index.html", first_name=first_name, stuff=stuff,
                           favorite_pizza=favorite_pizza)

#localhost:5555/user/<name>
@app.route('/user/<name>')
def user(name):
    return render_template("user.html", user_name=name)

#Create custom error pages

#invalid url
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

#internal server error
@app.errorhandler(500)
def server_not_found(e):
    return render_template("500.html"), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555, debug=True)