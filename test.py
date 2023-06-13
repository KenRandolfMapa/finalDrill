import unittest
import warnings
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


if __name__ == "__main__":
    unittest.main()