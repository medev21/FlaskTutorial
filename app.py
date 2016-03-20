#from flask folder get class/package Flask
from flask import Flask

app = Flask(__name__) #name is referencing the Flask object

@app.route('/') #this is the root page
def home():
    return "This is my house"

if __name__ == "__main__":
    app.run()
