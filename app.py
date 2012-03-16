from flask import Falsk

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    APP.run(host='0.0.0.0', port=environ["PORT"])
