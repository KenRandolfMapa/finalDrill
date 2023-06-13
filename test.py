import json
import unittest
import warnings
from flask import Flask
from flask import request, jsonify, make_response
from ken import app

class MyProgTest(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"]= True
        self.app = app.test_client()

        warnings.simplefilter("ignore", category=DeprecationWarning)

def test_index_page(self):
    response = self.app.get("/")
    self.assertEqual(response.status_code, 200)

def test_test_getcustomer(self):
    response = self.app.get("/customer")
    self.assertEqual(response.status_code, 200)
    self.assertTrue("TRUE" in response.date.decode())

def test_add_employees(self):
    data = {
        "firstName": "John",
        "lastName": "Doe"
    }
    response = self.app.post("/employees", json=data)
    self.assertEqual(response.status_code, 201)
    response_data = json.loads(response.data)
    self.assertEqual(response_data["message"], "employees added successfully")
    self.assertEqual(response_data["rows_affected"], 1)

def test_update_employees(self):
    data = {
    "firstName": "John",
    "lastName": "Doe"
    }
    employee_number = 1
    response = self.app.put(f"/employees/{employee_number}", json=data)
    self.assertEqual(response.status_code, 200)
    response_data = json.loads(response.data)
    self.assertEqual(response_data["message"], "actor updated successfully")
    self.assertEqual(response_data["rows_affected"], 1)

def test_delete_employees(self):
    employee_number = 1
    response = self.app.delete(f"/employees/{employee_number}")
    self.assertEqual(response.status_code, 200)
    response_data = json.loads(response.data)
    self.assertEqual(response_data["message"], "actor deleted successfully")
    self.assertEqual(response_data["rows_affected"], 1)

if __name__ == "__main__":
    unittest.main()
