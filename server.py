from flask import Flask, redirect, url_for, jsonify 
app = Flask(__name__)
import mysql
import mysql.connector
import requests

# Jeśli pojawi się błąd przy imporcie to ja użyłam tych komend:
# pip install Flask
# pip install mysqlclient
# pip install mysql-connector-python


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="zadPy"
)

# Pupil's endpoints
# -----------------------------------------------
@app.route('/addPupil/<id>/<name>/<surname>/<requestPesel>/<className>')
def addPupil(id, name, surname, requestPesel, className):
    mycursor = mydb.cursor()
    newPupil = "INSERT INTO pupil (pupil_id, name, surname, pesel, class) VALUES (%s, %s, %s, %s, %s)" 
    newPupilValues = (id, name, surname, requestPesel, className)
    mycursor.execute(newPupil, newPupilValues)   
    mydb.commit()
    print(mycursor.rowcount, " record successfully inserted.")
    return jsonify(
        IMPORTANT="Pupil with id "+ id +" added to database. If there is an error change id then try again)",
    )

@app.route('/showAllPupils')
def showAllPupils():
    mycursor = mydb.cursor()
    sql = 'SELECT * FROM pupil'
    mycursor.execute(sql)
    results = mycursor.fetchall()
    for x in results:
        print(x)
    return jsonify(
        IMPORTANT='All pupils showed',
    )

@app.route('/removeAllPupils')
def removeAllPupils():
    mycursor = mydb.cursor()
    sqlQuery = "DELETE FROM pupil"
    mycursor.execute(sqlQuery)
    mydb.commit()
    print(mycursor.rowcount, "record deleted")
    return jsonify(
        IMPORTANT="All Pupils removed succesfully"
    )
# -----------------------------------------------

# Teacher's endpoints
# -----------------------------------------------
@app.route('/addTeacher/<id>/<name>/<surname>/<requestPesel>/<subject>')
def addTeacher(id, name, surname, requestPesel, subject):
    mycursor = mydb.cursor()
    newTeacher = "INSERT INTO teacher (teacher_id, name, surname, pesel, subject) VALUES (%s, %s, %s, %s, %s)" 
    newTeacherValues = (id, name, surname, requestPesel, subject)
    mycursor.execute(newTeacher, newTeacherValues)   
    mydb.commit()
    print(mycursor.rowcount, " record successfully inserted.")
    return jsonify(
        IMPORTANT="Teacher with id "+ id +" added to database. If there is an error change id then try again",
    )

@app.route('/showAllTeacher')
def showAllTeacher():
    mycursor = mydb.cursor()
    sql = 'SELECT * FROM Teacher'
    mycursor.execute(sql)
    results = mycursor.fetchall()
    for x in results:
        print(x)
    return jsonify(
        IMPORTANT='All teachers showed'
    )
    
@app.route('/removeAllTeachers')
def removeAllTeachers():
    mycursor = mydb.cursor()
    sqlQuery = "DELETE FROM teacher"
    mycursor.execute(sqlQuery)
    mydb.commit()
    print(mycursor.rowcount, "record deleted")
    return jsonify(
        IMPORTANT="All teachers removed succesfully"
    )
# -----------------------------------------------

# Subject's endpoints
# -----------------------------------------------
@app.route('/addSubject/<id>/<name>')
def addSubject(subject_id,name ):
    mycursor = mydb.cursor()
    newSubject = "INSERT INTO Subject (subject_id, name) VALUES (%s, %s)"
    newSubjectValues = (id, name)
    mycursor.execute(newSubject, newSubjectValues)   
    mydb.commit()
    print(mycursor.rowcount, " record inserted.")
    return jsonify(
        IMPORTANT="Subject with id "+ id +" added to database. If there is an error change id then try again"
    )

@app.route('/showAllSubjects')
def showAllSubjects():
    mycursor = mydb.cursor()
    sql = 'SELECT * FROM Subject'
    mycursor.execute(sql)
    results = mycursor.fetchall()
    for x in results:
        print(x)
    return jsonify(
        IMPORTANT='All subjects showed'
    )

# @app.route('/showIdOfMathSubjects')
# def showAllSubjects():
#     mycursor = mydb.cursor()
#     sql = 'SELECT subject_id FROM Subject where name = "Math"'
#     mycursor.execute(sql)
#     results = mycursor.fetchall()
#     for x in results:
#         print(x)
#     return jsonify(
#         IMPORTANT='All subjects showed'
#     )

@app.route('/removeAllSubjects')
def removeAllSubjects():
    mycursor = mydb.cursor()
    sqlQuery = "DELETE FROM subject"
    mycursor.execute(sqlQuery)
    mydb.commit()
    print(mycursor.rowcount, "record deleted")
    return jsonify(
        IMPORTANT="All subjects removed succesfully"
    )
# -----------------------------------------------

# Pupil_Subject's endpoints
# -----------------------------------------------
@app.route('/addPupilSubject/<pupil_id>/<subject_id>')
def add_pupilsubject(pupil_id, subject_id):
    mycursor = mydb.cursor()
    newPupilSubject = "INSERT INTO Pupil_Subject (pupil_id, subject_id) VALUES (%s, %s)"
    newPupilSubjectValues = (pupil_id, subject_id)
    mycursor.execute(newPupilSubject, newPupilSubjectValues)   
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")
    return jsonify(
        IMPORTANT= "Pupil with id " +pupil_id + " added to subject successfully",
    )

@app.route('/showAllPupilsSubjects')
def showAllPupilsSubjects():
    mycursor = mydb.cursor()
    sql = 'SELECT * FROM Pupil_Subject'
    mycursor.execute(sql)
    results = mycursor.fetchall()
    for x in results:
        print(x)
    return jsonify(
        IMPORTANT='All pupil_subjects showed'
    )

@app.route('/removeAllPupilsSubjects')
def removeAllPupilsSubjects():
    mycursor = mydb.cursor()
    sqlQuery = "DELETE FROM Pupil_Subject"
    mycursor.execute(sqlQuery)
    mydb.commit()
    print(mycursor.rowcount, "record deleted")
    return jsonify(
        IMPORTANT="All pupil_subjects removed succesfully"
    )
# -----------------------------------------------

# Pupil_Teacher's endpoints
# -----------------------------------------------
@app.route('/addPupilTeacher/<pupil_id>/<teacher_id>')
def addPupilTeacher(pupil_id, teacher_id):
    mycursor = mydb.cursor()
    newPupilteacher = "INSERT INTO Pupil_Teacher (pupil_id, teacher_id) VALUES (%s, %s)"
    newPupilteacherValues = (pupil_id, teacher_id)
    mycursor.execute(newPupilteacher, newPupilteacherValues)   
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")
    return jsonify(
        IMPORTANT ="Pupil with id "+ pupil_id + " added successfully to teacher"
    )

@app.route('/showAllPupilTeachers')
def showAllPupilTeachers():
    mycursor = mydb.cursor()
    sql = 'SELECT * FROM Pupil_Teacher'
    mycursor.execute(sql)
    results = mycursor.fetchall()
    for x in results:
        print(x)
    return jsonify(
        IMPORTANT='All Pupil_Teachers showed'
    )

@app.route('/removeAllPupilTeachers')
def removeAllPupilTeachers():
    mycursor = mydb.cursor()
    sqlQuery = "DELETE FROM Pupil_Teacher"
    mycursor.execute(sqlQuery)
    mydb.commit()
    print(mycursor.rowcount, "record deleted")
    return jsonify(
        IMPORTANT="All Pupil_Teacher removed succesfully"
    )
# -----------------------------------------------

# @app.route('/removeSubject/<id>')
# def removeSubject(id):
#     mycursor = mydb.cursor()
#     sqlQuery = "DELETE FROM subject WHERE subject_id = (id == %s)"
#     mycursor.execute(sqlQuery,id)
#     mydb.commit()
#     print(mycursor.rowcount, "record deleted")
#     return jsonify(
#         IMPORTANT="Subject with id: " + id + " removed succesfully"
#     )

# @app.route('/removeSubject/<id>')
# def removeSubject(id):
#     mycursor = mydb.cursor()
#     sql = "DELETE FROM Subject WHERE subject_id = %s"
#     mycursor.execute(sql,id)
#     mydb.commit()
#     print(mycursor.rowcount, "record(s) deleted")
#     return jsonify(
#         IMPORTANT="Subject " + id + " removed",
#         responseCode=200
#     )







# @app.route('/addPupil/<id>/<name>/<surname>/<pesel>/<className>')
# def add_pupil(id, name, surname, pesel, className):
#     ifExist = "Sorry, but user with this id already exists"
#     mycursor = mydb.cursor()
#     new_pupil = "INSERT INTO pupil (pupil_id, name, surname, pesel, class) VALUES (%s, %s, %s, %s, %s)" 
#     selectallif = "SELECT * FROM (SELECT 'pupil_id', 'name', 'surname', 'pesel', 'class') AS tmp WHERE NOT EXISTS (SELECT pupil_id FROM pupil WHERE pupil_id != id) LIMIT 1"
#     responseIfidexist = "SELECT * FROM (SELECT 'pupil_id', 'name', 'surname', 'pesel', 'class') IF pupil_id == id THEN return ifExist;END IF;"
#     new_pupil_values = (id, name, surname, pesel, className)
#     mycursor.execute(new_pupil,selectallif,responseIfidexist, new_pupil_values)   
#     mydb.commit()
#     print(mycursor.rowcount, "record inserted.")
#     return jsonify(
#         IMPORTANT="User " + name + " " + surname + " added successfully to database",
#     )

# @app.route('/removeTeacher/<id>')
# def removeTeacher(id):
#     mycursor = mydb.cursor()
#     sqlQuery = "DELETE FROM teacher WHERE teacher_id = '%s'"
#     mycursor.execute(sqlQuery,id)
#     mydb.commit()
#     print(mycursor.rowcount, "record deleted")
#     return jsonify(
#         IMPORTANT="Teacher with id: "+ id +" removed succesfully"
#     )

if __name__ == "__main__":
    app.run("localhost", 3000, True, {}) # odpalenie serwera (host, port, debug, options)
