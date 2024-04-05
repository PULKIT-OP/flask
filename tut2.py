from flask import Flask, render_template

app = Flask(__name__)                   #   First flask program

@app.route("/")                     # endpoint 1
def hello_world():
    return render_template('index.html')


@app.route("/index2")               # endpoint 3
def index():
    return render_template('index2.html')

@app.route("/about")                # endpoint 4
def about():
    name = "PULKIT"
    return render_template('about.html', name2 = name)

@app.route("/bootstrap")
def bootstrap():
    return render_template('bootstrap.html')
app.run(debug = True)