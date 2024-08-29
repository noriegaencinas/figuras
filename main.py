from flask import flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')
    