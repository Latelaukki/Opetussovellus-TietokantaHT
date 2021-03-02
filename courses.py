from db import db

def get_courses():
    sql = "SELECT C.name FROM courses C ORDER BY C.id"
    result = db.session.execute(sql)
    return result.fetchall()

def add_course(name, content):
    try:
        sql = "INSERT INTO courses (name, content) VALUES (:name, :content)"
        result = db.session.execute(sql, {"name":name,"content":content})
        db.session.commit()
    except:
        return False    
    return True