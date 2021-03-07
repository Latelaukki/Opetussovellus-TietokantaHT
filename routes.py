from app import app
from flask import render_template, request, redirect, session
import courses, users, quizzes

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
            return render_template("login.html",message="Väärä tunnus tai salasana", username=username, password=password)

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
            return render_template("register.html",message="Antamasi tunnus on jo käytössä, kokeile toista", username=username, password=password)

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
        username = users.getUsername(id)
        joinedCourses = courses.getJoinedCourses(id)
        teachingCourses = courses.getTeachersCourses(id)
        return render_template("profile.html", isAdmin=admin, isTeacher=teacher, id=id, loggedIn=loggedIn, username=username, joinedCourses=joinedCourses, teachingCourses=teachingCourses)    

@app.route("/editprivileges/<int:id>", methods=["GET", "POST"])
def editprivileges(id):
    admin = False
    if users.isAdmin(users.user_id()):
        admin = True       
    if not admin:
        return redirect("/")
    if request.method == "GET":
        return render_template("editprivileges.html", id=id)    
    if request.method == "POST":
        newTeacher = request.form["newTeacher"]
        newAdmin = request.form["newAdmin"]
        if users.editprivileges(id, newTeacher, newAdmin):
            return redirect("/profile/" + str(id))
        else:
            return render_template("editprivileges.html", message="Tapahtui virhe, yritä uudelleen tai peruuta")

@app.route("/delete/<int:id>", methods=["GET", "POST"])
def delete(id):
    allow = False
    isAdmin = False
    if users.isAdmin(users.user_id()):
        allow = True
        isAdmin = True
    if users.user_id() == id:
        allow = True
    if not allow:
        return redirect("/profile/" + str(id))
    if request.method == "GET":
        username = users.getUsername(id)
        return render_template("delete.html", isAdmin=isAdmin, id=id, username=username)    
    if request.method == "POST":
        if users.isTeacher(id):
            return render_template("delete.html", isAdmin=isAdmin, id=id, message="Et voi poistaa käyttäjää, joka on opettaja.")
        if users.deleteUser(id):
            users.logout()
            return redirect("/")        
    return render_template("delete.html", isAdmin=isAdmin, id=id, message="Käyttäjän poistaminen epäonnistui, yritä uudelleen")         

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

@app.route("/addcourse", methods=["GET", "POST"])
def addcourse():
    teacher = False
    if users.isTeacher(users.user_id()):
        teacher = True
    if not teacher:
        return redirect("/")
    if request.method == "GET":
        return render_template("addcourse.html")
    if request.method == "POST":
        if session["csrf_token"] != request.form["csrf_token"]:
            abort(403)
        code = request.form["code"]    
        name = request.form["name"]
        content = request.form["content"]
        teacher_id = users.user_id()
        if courses.addCourse(code, name, content, teacher_id):
            return redirect("/allcourses")
        return render_template("addcourse.html",message="Tapahtui jokin virhe. Huom! Kahta kurssia ei voi olla samalla koodilla.")    

@app.route("/course/<int:id>", methods=["GET", "POST"])
def course(id):
    canAnswerQuestions = False
    isCourseTeacher = False
    if courses.isCourseStudent(id):
        canAnswerQuestions = True
    code = courses.getCourseCode(id)
    name = courses.getCourseName(id)
    content = courses.getCourseContent(id)
    teacher = courses.getCourseTeacher(id)
    if courses.isCourseTeacher(id):
        isCourseTeacher = True
        canAnswerQuestions = False
    quizzes1 = quizzes.getQuizzes(id)
    if request.method == "GET":
        return render_template("course.html", id=id, code=code, name=name, content=content, isCourseTeacher=isCourseTeacher, canAnswerQuestions=canAnswerQuestions, quizzes=quizzes1, teacher=teacher)
    if request.method == "POST":
        choices = request.form.getlist(choice)
        quizzes.checkAnswers(choices, id)
        return render_template("course.html")    


@app.route("/addquestion/<int:id>", methods=["GET","POST"])
def addquestion(id):
    isCourseTeacher = False
    if courses.isCourseTeacher(id):
        isCourseTeacher = True
    if not isCourseTeacher:
        return redirect("/")
    if request.method == "GET":
        return render_template("addquestion.html", id=id)
    if request.method == "POST":
        if session["csrf_token"] != request.form["csrf_token"]:
            abort(403)
        question = request.form["question"]
        choice1 = request.form["choice1"]
        choice2 = request.form["choice2"]
        choice3 = request.form["choice3"]
        choice4 = request.form["choice4"]
        answers = request.form.getlist("answer")
        if quizzes.addQuiz(question, id, choice1, choice2, choice3, choice4, answers):
            return redirect("/course/" + str(id))
        return render_template("addquestion.html", message="Tapahtui virhe, yritä uudelleen. Huom! Vähintään kaksi vastausvaihtoehtoa tarvitaan ja yksi vastaus.")

@app.route("/participate/<int:id>", methods=["GET", "POST"])            
def participate(id):
    isAlreadyStudent = False
    if courses.isCourseStudent(id):
        isAlreadyStudent = True
    code = courses.getCourseCode(id)
    name = courses.getCourseName(id)  
    if request.method == "GET":
        return render_template("participate.html", id=id, isAlreadyStudent=isAlreadyStudent, code=code, name=name)
    if request.method == "POST":
        if isAlreadyStudent:
            if courses.removeFromCourse(id):
                return redirect("/allcourses")
        if not isAlreadyStudent:
            if courses.participateCourse(id):
                return redirect("/allcourses")
    return render_template("participate.html", id=id, message="Tapahtui virhe, yritä uudelleen")                     

