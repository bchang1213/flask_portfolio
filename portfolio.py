from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")

def welcome():
	return render_template('base.html')

@app.route("/projects")
def portfoliomethod():
	return render_template('portfolio.html')

@app.route("/about")
def aboutme():
	return render_template('about.html')

app.run(debug=True)