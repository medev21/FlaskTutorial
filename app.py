#from flask folder get class/package Flask
from flask import Flask, render_template
from flask.ext.assets import Environment, Bundle

app = Flask(__name__, static_folder = 'static') #name is referencing the Flask object
assets = Environment(app)
assets.init_app(app)

@app.route('/')
def homepage():
    return render_template('index.html')

if __name__ == "__main__":
    app.debug = True #the debug log is displayed on the console
    app.run()
    # app.run('0.0.0.0', debug = True) you can set your own address

#one way to do it
# app = Flask(__name__) #name is referencing the Flask object

# @app.route('/') #this is the root page
# def home():
#     return "hello"
#
# @app.route('/profile/<username>') #localhost:5000/profile/whatever word you set
# def profile(username):
#     return "hey, your name is %s" % username + " i hate that name"
#
# @app.route('/post/<int:post_num>') #this accepts integers only; localhost:5000/post/whatever # you set
# def post(post_num):
#     return "<h1>Post ID %s</h1>" % post_num
#
# @app.route('/index')
# def index():
#     return render_template('index.html')
#     """
#     in order for render_template to work, you need to add templates folder and
#     move the index html to that folder, this method will look for a folder
#     called template and load the index page
#     """
#
# if __name__ == "__main__":
#     app.debug = True #the debug log is displayed on the console
#     app.run()
#     # app.run('0.0.0.0', debug = True) you can set your own address
