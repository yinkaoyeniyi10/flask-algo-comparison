from flask import Flask, render_template, jsonify, request
import random
app = Flask(__name__)
@app.route("/")
#Index section
def index():
    return render_template("index.html")
@app.route("/generate")
def generate():
    numbers = [random.randint(10, 100) for _ in range(20)]
    return jsonify(numbers)
if __name__ == "__main__":
    app.run(debug=True)