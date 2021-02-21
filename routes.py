from app import app
from flask import render_template, request, redirect
import courses, users

@app.route("/")
def index():
    allow = False
    if users.isAdmin():
        allow = True       
    return render_template("index.html", IsAdmin=allow)

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
            return render_template("login.html",message="Väärä tunnus tai salasana")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.isEmpty(username):
            return render_template("register.html", message="Tunnuksen on oltava vähintään 1 merkki.")
        if users.register(username,password):
            return redirect("/")
        else:
            return render_template("register.html",message="Antamasi tunnus on jo käytössä, kokeile toista")

@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")

@app.route("/profile/<int:id>")
def profile(id):
    loggedIn = False 
    teacher = False
    admin = False
    if users.isAdmin():
        admin = True 
    if users.isTeacher():
        teacher = True  
    if users.user_id() == id:
        loggedIn = True        
    if not loggedIn and not teacher and not admin:
        return redirect("/")
    else:
        return render_template("profile.html", isAdmin=admin, isTeacher=teacher)    

@app.route("/editprivileges", methods=["GET", "POST"])
def addprivileges():
    admin = False
    if users.isAdmin(): 
        admin = True       
    if not admin:
        return redirect("/")
    else:
        if request.method == "GET":
            return render_template("editprivileges.html")    
        if request.method == "POST":
            username = request.form["username"]
            password = request.form["password"]
            if users.login(username,password):
                return redirect("/")
            else:
                return render_template("editprivileges.html",message="Väärä tunnus tai salasana")