from flask import Flask,redirect,render_template

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route("/home")
def home_red():
    return "<h1>Hello world</h1>"


if __name__=='__main__':
    app.run(debug=True,port=8000)