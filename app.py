from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/cars")
def cars(): 
    return render_template('cars.html')


if __name__ == "__main__":
    app.run(debug=True, port=8000, host="127.0.0.1")
