import unittest
from service import app

class TestService(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_get_accounts(self):
        resp = self.client.get("/accounts")
        self.assertEqual(resp.status_code, 200)

if __name__ == "__main__":
    unittest.main()