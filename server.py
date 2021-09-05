from flask import Flask, render_template  # added render_template!

# Create a new instance of the Flask class called "app"
app = Flask(__name__)

print(__name__)


@app.route("/")
def index():
    return render_template("index.html", row=8, column=8)


@app.route("/<x>/<y>/")
def play(x, y):
    return render_template("index.html", row=int(x), column=int(y))


if __name__ == "__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)    # Run the app in debug mode.
