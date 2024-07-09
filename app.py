from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "manbearpig_MUDMAN888"

@app.route("/home", methods=['POST', 'GET'])
def home():
	return render_template("home.html")

@app.route("/create", methods=['POST', 'GET'])
def create():
	return render_template("create.html")

@app.route("/answer", methods=['POST', 'GET'])
def answer():
	#flash("Answer of " + str(request.form['front_card']) + " is : " + str(request.form['back_card']))
	return render_template("answer.html")

@app.route("/signup", methods=['POST', 'GET'])
def signup():
	
	user =[request.form['username'], request.form['password'], request.form['email']]
	return render_template("signup.html")

@app.route("/login", methods=['POST', 'GET'])
def login():
	return render_template("login.html")

if __name__ == "__main__": 
    app.run(debug=True) 
	