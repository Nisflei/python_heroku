from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index2')
def index2():
    return render_template('index2.html')

@app.route('/ex2d')
def ex2d():
    return render_template('ex2d.html')

@app.route('/ex3a')
def ex3a():
    return render_template('ex3a.html')

#app.run()
