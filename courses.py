from db import db

def getCourses():
    result = db.session.execute("SELECT id, name FROM courses C ORDER BY C.id")
    return result.fetchall()

def addCourse(name, content):
    try:
        sql = "INSERT INTO courses (name, content) VALUES (:name, :content)"
        result = db.session.execute(sql, {"name":name,"content":content})
        db.session.commit()
    except:
        return False    
    return True