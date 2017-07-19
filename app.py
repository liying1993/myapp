
from flask import Flask
from flask_cors import CORS
from flask_cors import cross_origin
app = Flask(__name__)
CORS(app)

@cross_origin()
@app.route('/', methods=["GET"])
def hello():
	return "hello world"

app.run()
