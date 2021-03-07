from db import db
import users

def addCourse(code, name, content, teacher_id):
    try:
        sql = "INSERT INTO courses (code, name, content, teacher_id) VALUES (:code, :name, :content, :teacher_id)"
        result = db.session.execute(sql, {"code":code,"name":name,"content":content, "teacher_id":teacher_id})
        db.session.commit()
    except:
        return False    
    return True

def isCourseTeacher(id):
    sql = "SELECT teacher_id FROM courses WHERE id=:id"
    result = db.session.execute(sql, {"id":id})
    teacher_id = result.fetchone()[0]
    return users.user_id() == teacher_id

def getJoinedCourses(user_id):
    sql = "SELECT id, code, name FROM courses WHERE id IN (SELECT course_id FROM participants WHERE user_id=:user_id)"
    result = db.session.execute(sql, {"user_id":user_id})
    return result.fetchall()

def isCourseStudent(course_id):
    sql = "SELECT 1 FROM participants WHERE course_id=:course_id AND user_id=:user_id"
    result = db.session.execute(sql, {"course_id":course_id,"user_id":users.user_id()})
    return result.fetchone() != None

def getCourseCode(id):
    sql = "SELECT code FROM courses WHERE id=:id"
    result = db.session.execute(sql, {"id":id})
    return result.fetchone()[0]

def getCourseName(id):
    sql = "SELECT name FROM courses WHERE id=:id"
    result = db.session.execute(sql, {"id":id})
    return result.fetchone()[0]

def getCourseContent(id):
    sql = "SELECT content FROM courses WHERE id=:id"
    result = db.session.execute(sql, {"id":id})
    return result.fetchone()[0]

def getCourseTeacher(id):
    sql = "SELECT username FROM users WHERE id=(SELECT teacher_id FROM courses WHERE id=:id)"
    result = db.session.execute(sql, {"id":id})
    return result.fetchone()[0]

def getCourses():
    result = db.session.execute("SELECT id, code, name FROM courses ORDER BY name")
    return result.fetchall()

def getTeachersCourses(user_id):
    sql = "SELECT id, code, name FROM courses WHERE teacher_id=:user_id"
    result = db.session.execute(sql, {"user_id":user_id})
    return result.fetchall()

def participateCourse(course_id):
    try:
        sql = "INSERT INTO participants (user_id, course_id) VALUES (:user_id,:course_id)"
        db.session.execute(sql, {"user_id":users.user_id(),"course_id":course_id})
        db.session.commit()
    except:
        return False    
    return True

def removeFromCourse(course_id):
    try:
        sql = "DELETE FROM participants WHERE course_id=:course_id AND user_id=:user_id"
        db.session.execute(sql, {"course_id":course_id,"user_id":users.user_id()})
        db.session.commit()
    except:
        return False
    return True        
  



