from flask import Flask, redirect, url_for, jsonify 
app = Flask(__name__)
import mysql
import mysql.connector
import requests
import random

from utils import deleteAllCars, showAllCars, addNewCar, deleteCarsById, addNewUser, deleteAllUsers, showAllUsers, deleteUserById, deleteUserByPesel,checkIfUserExists,addNewRental,showAllRentals,deleteAllRentals,deleteRentalById

# Jeśli pojawi się błąd przy imporcie to ja użyłam tych komend:
# pip install Flask
# pip install mysqlclient
# pip install mysql-connector-python
# pip install requests
# pip install random

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="carRental"
)

# Car's endpoints
# -----------------------------------------------
@app.route('/addCar/<carname>/<brandname>/<carhp>/<enginecapacity>/<manufacturedate>') # localhost:3000/addCar/Ewa/Mercedes/100/2/2020-09-13
def addCar(carname, brandname, carhp, enginecapacity,manufacturedate):
    results = addNewCar(carname, brandname, carhp, enginecapacity,manufacturedate, mydb)
    return jsonify(
        IMPORTANT="Car "+ brandname +" added successfully to database",
    )
    return jsonify(
        results,
    )

@app.route('/removeAllCars') # localhost:3000/removeAllCars
def removeAllCars():
    results = deleteAllCars(mydb)
    return jsonify(
        IMPORTANT="All cars deleted successfully"
    )
    return jsonify(
        results,
    )

@app.route('/showAllCars') # localhost:3000/showAllCars
def showAllCars():
    results = showAllCars(mydb)
    for x in results:
        print(x)
    return jsonify(
        results,
    )

@app.route('/removeCarById/<id>') # localhost:3000/removePupilById/1
def removeCarById(id):
    results = deleteCarsById(id,mydb)
    return jsonify(
        IMPORTANT="Car with id "+ id +" removed succesfully"
    )
    return jsonify(
        results,
    )
# -----------------------------------------------

# User's endpoints
# -----------------------------------------------
@app.route('/addUser/<name>/<surname>/<pesel>') # localhost:3000/addUser/Ewa/Zalewska/1249
def addUser(name, surname, pesel):
    ifExsit = checkIfUserExists(pesel,mydb)
    if ifExsit is None:
        results = addNewUser(name, surname, pesel, mydb)
        return jsonify(
            IMPORTANT="Pupil "+ name +" "+ surname+" added to database."
        )
    return jsonify(
        IMPORTANT="User "+ name +" "+ surname+" already exists in the database."
    )

@app.route('/removeAllUsers') # localhost:3000/removeAllUsers
def removeAllUsers():
    results = deleteAllUsers(mydb)
    return jsonify(
        IMPORTANT="All users deleted successfully"
    )
    return jsonify(
        results,
    )

@app.route('/showAllusers') # localhost:3000/showAllusers
def showAllusers():
    results = showAllUsers(mydb)
    for x in results:
        print(x)
    return jsonify(
        results,
    )

@app.route('/removeUserById/<id>') # localhost:3000/removeUserById/3
def removeUserById(id):
    results = deleteUserById(id,mydb)
    return jsonify(
        IMPORTANT="User with id "+ id +" removed succesfully"
    )
    return jsonify(
        results,
    )

@app.route('/removeUserByPesel/<pesel>') # localhost:3000/removeUserByPesel/1245
def removeUserByPesel(pesel):
    results = deleteUserByPesel(pesel,mydb)
    return jsonify(
        IMPORTANT="User with pesel "+ pesel +" removed succesfully"
    )
    return jsonify(
        results,
    )
# -----------------------------------------------

# Rental's endpoints
# -----------------------------------------------
@app.route('/addRental/<carId>/<userId>') # localhost:3000/addRental/6/5
def addRental(carId, userId):
    results = addNewRental(carId, userId, mydb)
    return jsonify(
        IMPORTANT="Rental added successfully to database",
    )
    return jsonify(
        results,
    )

@app.route('/removeAllRentals') # localhost:3000/removeAllRentals
def removeAllRentals():
    results = deleteAllRentals(mydb)
    return jsonify(
        IMPORTANT="All rentals deleted successfully"
    )
    return jsonify(
        results,
    )

@app.route('/showRentals') # localhost:3000/showRentals
def showRentals():
    results = showAllRentals(mydb)
    for x in results:
        print(x)
    return jsonify(
        results,
    )

@app.route('/removeRentalById/<id>') # localhost:3000/removeRentalById/1
def removeRentalById(id):
    results = deleteRentalById(id,mydb)
    return jsonify(
        IMPORTANT="Rental with id "+ id +" removed succesfully"
    )
    return jsonify(
        results,
    )
# -----------------------------------------------

# # LendHistory's endpoints
# # -----------------------------------------------
# @app.route('/addLendHistory/<carId>/<userId>/<>') # localhost:3000/addRental/6/5
# def addRental(carId, userId):
#     results = addNewRental(carId, userId, mydb)
#     return jsonify(
#         IMPORTANT="Rental added successfully to database",
#     )
#     return jsonify(
#         results,
#     )

# @app.route('/removeAllRentals') # localhost:3000/removeAllRentals
# def removeAllRentals():
#     results = deleteAllRentals(mydb)
#     return jsonify(
#         IMPORTANT="All rentals deleted successfully"
#     )
#     return jsonify(
#         results,
#     )

# @app.route('/showRentals') # localhost:3000/showRentals
# def showRentals():
#     results = showAllRentals(mydb)
#     for x in results:
#         print(x)
#     return jsonify(
#         results,
#     )

# @app.route('/removeRentalById/<id>') # localhost:3000/removeRentalById/1
# def removeRentalById(id):
#     results = deleteRentalById(id,mydb)
#     return jsonify(
#         IMPORTANT="Rental with id "+ id +" removed succesfully"
#     )
#     return jsonify(
#         results,
#     )
# # -----------------------------------------------
if __name__ == "__main__":
    app.run("localhost", 3000, True, {})
