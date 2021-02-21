from db import db
from flask import session
from werkzeug.security import check_password_hash, generate_password_hash

def login(username, password):
    sql = "SELECT password, id FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()
    if user == None:
        return False
    else:
        if check_password_hash(user[0],password):
            session["user_id"] = user[1]
            return True
        else:
            return False

def logout():
    del session["user_id"]

def register(username,password):
    hash_value = generate_password_hash(password)
    try:
        sql = "INSERT INTO users (username,password) VALUES (:username,:password) RETURNING id"
        result = db.session.execute(sql, {"username":username,"password":hash_value})
        user_id = result.fetchone()[0]
        sql = "INSERT INTO privileges (user_id,admin,teacher) VALUES (:user_id,0,0)"
        db.session.execute(sql, {"user_id":user_id})
        db.session.commit()
    except:
        return False   
    return login(username,password)

def addTeacher(username):
    try:
        sql = "SELECT id FROM users WHERE username=:username"
        result = db.session.execute(sql, {"username":username})
        user_id = result.fetchone()
        sql = "UPDATE privileges SET teacher = 1 WHERE user_id=:user_id"
        db.session.execute(sql, {"user_id":user_id})
        db.session.commit()
    except:
        return False
    return True     

def isTeacher():
    if user_id() == 0:
        return False
    sql = "SELECT teacher FROM privileges WHERE user_id=:id"
    result = db.session.execute(sql, {"id":user_id()})
    return result.fetchone()[0] == 1

def isAdmin():
    if user_id() == 0:
        return False
    print(user_id())    
    sql = "SELECT admin FROM privileges WHERE user_id=:id"
    result = db.session.execute(sql, {"id":user_id()})
    return result.fetchone()[0] == 1

def isEmpty(username):
    return username == ""

def user_id():
    return session.get("user_id",0)