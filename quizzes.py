from db import db
import courses

def addQuiz(question, course_id, choice1, choice2, choice3, choice4, answers):                
    try:
        sql = "INSERT INTO quizzes (question, course_id, choice1, choice2, choice3, choice4) VALUES (:question, :course_id, :choice1, :choice2, :choice3, :choice4) RETURNING id"
        result = db.session.execute(sql, {"question":question,"course_id":course_id,"choice1":choice1,"choice2":choice2,"choice3":choice3,"choice4":choice4})
        quiz_id = result.fetchone()[0]
        for answer in answers:
            sql = "INSERT INTO answers (quiz_id, right_answer) VALUES (:quiz_id, :right_answer)"
            result = db.session.execute(sql, {"quiz_id":quiz_id,"right_answer":answer})
        db.session.commit()
    except:
        return False    
    return True

def getQuizzes(course_id):
    sql = "SELECT question, choice1, choice2, choice3, choice4 FROM quizzes WHERE course_id=:course_id"
    result = db.session.execute(sql, {"course_id":course_id})
    return result.fetchall()

def checkAnswers(choices, course_id):
    for choice in choices:
        answers
        if choice != 1 or choice != 2 or choice != 3 or choice != 4:
            sql = "SELECT right_answer WHERE quiz_id=(SELECT id FROM quizzes WHERE question=:choice) AND course_id=:course_id"
            result = db.session.execute(sql, {"choice":choice,"course_id":course_id})
            right_answers = result.fetchall()         