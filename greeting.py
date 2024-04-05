from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index4.html')

@app.route('/greet', methods = ['POST'])
def greet():
    if request.method == 'POST':
        name = request.form['name']
        return redirect(url_for('greeting', name = name))
    
@app.route('/greeting/<name>')
def greeting(name):
    return render_template('greeting.html', name = name)

if __name__ == '__main__':
    app.run(debug = True)