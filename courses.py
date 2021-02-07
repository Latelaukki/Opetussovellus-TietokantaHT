from db import db

def get_courses():
    sql = "SELECT C.name FROM courses C ORDER BY C.id"
    result = db.session.execute(sql)
    return result.fetchall()

def add_course():
    sql = "INSERT INTO courses (name, content) VALUES (testi-kurssi, hello)"
    db.session.commit()
    return True