def deleteAllCars(mydb):
    mycursor = mydb.cursor()
    sqlQuery = "DELETE FROM cars;"
    deleting = mycursor.execute(sqlQuery)
    mydb.commit()
    return deleting

def showAllCars(mydb):
    mycursor = mydb.cursor()
    sql = 'SELECT * FROM cars'
    mycursor.execute(sql)
    results = mycursor.fetchall()
    return results