from db import db
from flask import session
import os
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
            session["csrf_token"] = os.urandom(16).hex()
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

def deleteUser(id): 
    try:
        sql = "DELETE FROM users WHERE id=:id"
        db.session.execute(sql, {"id":id})
        db.session.commit()
    except:
        return False   
    return True   

def editprivileges(id, newTeacher, newAdmin):   
    if newTeacher == "yes":
        if not setTeacher(id):
            return False
    if newTeacher == "no":
        if not removeTeacher(id):
            return False
    if newAdmin == "yes":
        if not setAdmin(id):
            return False
    if newAdmin == "no":
        if not removeAdmin(id):
            return False
    return True        

def setTeacher(id):
    try:
        sql = "UPDATE privileges SET teacher = 1 WHERE user_id=:user_id"
        db.session.execute(sql, {"user_id":id})
        db.session.commit()
    except:
        return False
    return True     

def setAdmin(id):
    try:
        sql = "UPDATE privileges SET admin = 1 WHERE user_id=:user_id"
        db.session.execute(sql, {"user_id":id})
        db.session.commit()
    except:
        return False
    return True     

def removeTeacher(id):
    try:
        sql = "UPDATE privileges SET teacher = 0 WHERE user_id=:user_id"
        db.session.execute(sql, {"user_id":id})
        db.session.commit()
    except:
        return False
    return True

def removeAdmin(id):
    try:
        sql = "UPDATE privileges SET admin = 0 WHERE user_id=:user_id"
        db.session.execute(sql, {"user_id":id})
        db.session.commit()
    except:
        return False
    return True

def isTeacher(id):
    if user_id() == 0:
        return False
    try:    
        sql = "SELECT teacher FROM privileges WHERE user_id=:id"
        result = db.session.execute(sql, {"id":id})
        teacher = result.fetchone()[0]
    except:
        return False    
    return teacher == 1

def isAdmin(id):
    if user_id() == 0:
        return False
    try:     
        sql = "SELECT admin FROM privileges WHERE user_id=:id"
        result = db.session.execute(sql, {"id":id})
        admin = result.fetchone()[0]
    except:
        return False    
    return admin == 1

def isEmpty(username):
    return username == ""

def user_id():
    return session.get("user_id",0)

def getUsers():
    result = db.session.execute("SELECT id, username FROM users")
    return result.fetchall()

def getUsername(id):
    sql = "SELECT username FROM users WHERE id=:id"
    result = db.session.execute(sql, {"id":id})
    return result.fetchone()[0]

def valid_csrf():
    return session["csrf_token"] != request.form["csrf_token"]    