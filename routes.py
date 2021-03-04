from app import app
from flask import render_template, request, redirect
import courses, users

@app.route("/")
def index():
    allow = False
    if users.isAdmin(users.user_id()):
        allow = True       
    return render_template("index.html", isAdmin=allow)

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
    if users.isAdmin(users.user_id()):
        admin = True 
    if users.isTeacher(users.user_id()):
        teacher = True  
    if users.user_id() == id:
        loggedIn = True        
    if not loggedIn and not teacher and not admin:
        return redirect("/")
    else:
        return render_template("profile.html", isAdmin=admin, isTeacher=teacher, id=id)    

@app.route("/editprivileges/<int:id>", methods=["GET", "POST"])
def editprivileges(id):
    admin = False
    if users.isAdmin(users.user_id()):
        admin = True       
    if not admin:
        return redirect("/")
    else:
        if request.method == "GET":
            return render_template("editprivileges.html", id=id)    
        if request.method == "POST":
            newTeacher = request.form["newTeacher"]
            newAdmin = request.form["newAdmin"]
            if newTeacher == "yes":
                if not users.addTeacher(id):
                    return render_template("editprivileges.html", message="Tapahtui virhe opettajan lisäyksessä, yritä uudelleen")
            if newTeacher == "no":
                if not users.removeTeacher(id):
                    return render_template("editprivileges.html", message="Tapahtui virhe opettajan poistossa, yritä uudelleen")
            if newAdmin == "yes":
                if not users.addAdmin(id):
                    return render_template("editprivileges.html", message="Tapahtui virhe ylläpitäjän lisäyksessä, yritä uudelleen")
            if newAdmin == "no":
                if not users.removeAdmin(id):
                    return render_template("editprivileges.html", message="Tapahtui virhe ylläpitäjän poistossa, yritä uudelleen")
            return redirect("/profile/" + str(id))

@app.route("/allprofiles")     
def allprofiles():
    admin = False
    if users.isAdmin(users.user_id()): 
        admin = True       
    if not admin:
        return redirect("/")
    else:
        allUsers = users.getUsers()
    return render_template("allprofiles.html", users=allUsers)     

@app.route("/allcourses")
def allcourses():
    teacher = False
    if users.isTeacher(users.user_id()):
        teacher = True
    allCourses = courses.getCourses()
    return render_template("allcourses.html", courses=allCourses, isTeacher=teacher)    