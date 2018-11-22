
# from app import routes
from flask import Flask

app = Flask(__name__)


# # TODO: place routes in separate folder
# decorators (HOC)
# # from app import routes
@app.route('/')
@app.route('/index')
# view functions are similar to handlers
def index():
    return "Hello, World!"
