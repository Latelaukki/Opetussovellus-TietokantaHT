from app import app
from flask import render_template, request, redirect
import courses, users

@app.route("/")
def index():
    list = courses.get_courses
    return render_template("index.html", courses=list)


@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.login(username,password):
            return redirect("/")
        else:
            return render_template("error.html",message="Väärä tunnus tai salasana")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.register(username,password):
            return redirect("/")
        else:
            return render_template("error.html",message="Antamasi tunnus on jo käytössä, kokeile toista")

# @app.route("/logout", methods=["GET"])
# def logout():
#     if request.method == "GET":