from flask import Flask, redirect, url_for, jsonify 
app = Flask(__name__)
import mysql
import mysql.connector
import requests
import random

from utils import deleteAllCars, showAllCars

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
    mycursor = mydb.cursor()
    newCar = "INSERT INTO CARS (NAME, BRAND, HP, ENGINE_CAPACITY,MANUFACTURE_DATE) VALUES (%s, %s, %s, %s, %s)" 
    newCarValues = (carname, brandname, carhp, enginecapacity,manufacturedate)
    mycursor.execute(newCar, newCarValues)   
    mydb.commit()
    print(mycursor.rowcount, " record successfully inserted.")
    return jsonify(
        IMPORTANT="Car "+ brandname+" added to database.",
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
# -----------------------------------------------


if __name__ == "__main__":
    app.run("localhost", 3000, True, {})
