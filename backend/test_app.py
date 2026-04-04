import unittest
from app import app
import json

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    # ✅ Test home route
    def test_home(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    # ✅ Test add_job route
    def test_add_job(self):
        response = self.app.post(
            '/add_job',
            data=json.dumps({
                'company': 'Test Company',
                'role': 'Tester',
                'status': 'Applied'
            }),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)

    # ✅ Test get_jobs route
    def test_get_jobs(self):
        response = self.app.get('/get_jobs')
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()