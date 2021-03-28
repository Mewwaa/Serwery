import unittest
import os
import mysql
import mysql.connector
import mock
from utils import deleteAllCars, showAllCars, addNewCar, deleteCarsById, addNewUser, deleteAllUsers, showAllUsers, deleteUserById, deleteUserByPesel,checkIfUserExists,addNewRental,showAllRentals,deleteAllRentals,deleteRentalById

mydb = None

class TestGetCars(unittest.TestCase): 
    @mock.patch("utils.showAllCars", return_value=['Car1','Car2'] )
    def testGetCarsFromDbMocked(self, mocked_get_cars): 
        result = mocked_get_cars.return_value
        self.assertEqual(2,len(result) )

class TestGetUsers(unittest.TestCase): 
    @mock.patch("utils.showAllUsers", return_value=['User1','User2'] )
    def testGetUsersFromDbMocked(self, mocked_get_users): 
        result = mocked_get_users.return_value
        self.assertEqual(2,len(result) )

class TestGetRentals(unittest.TestCase): 
    @mock.patch("utils.showAllRentals", return_value=['Rental1','Rental2'] )
    def testGetRentalsFromDbMocked(self, mocked_get_rentals): 
        result = mocked_get_rentals.return_value
        self.assertEqual(2,len(result) )

class TestDeleteCars(unittest.TestCase): 
    @mock.patch("utils.deleteAllCars", return_value=[] )
    def testDeleteCarsFromDbMocked(self, mocked_get_rentals): 
        result = mocked_get_rentals.return_value
        self.assertEqual(0,len(result) )

class TestDeleteUsers(unittest.TestCase): 
    @mock.patch("utils.deleteAllUsers", return_value=[] )
    def testDeleteUsersFromDbMocked(self, mocked_get_rentals): 
        result = mocked_get_rentals.return_value
        self.assertEqual(0,len(result) )


if __name__ == '__main__': 
    unittest.main() 