from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "1234abcd"

@app.route("/hello")
def index():
    flash("คุณชื่ออะไรหรือครับ?")
    return render_template("index.html")

@app.route("/greet", methods=["POST", "GET"])
def greet():
    flash("สวัสดีครับ คุณ " + str(request.form['name_input']) + ", ดีใจที่รู้จักครับ")
    return render_template("index.html")
    