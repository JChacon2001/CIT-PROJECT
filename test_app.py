import unittest
from app import app

class FlaskAppTest(unittest.TestCase):
    def setup(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_route(self):
        response = self.app.get("/")
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()