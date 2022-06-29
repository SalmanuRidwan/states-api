import os
import unittest
import json

from flaskr import create_app
from models import setup_db, State
from settings import DB_PASSWORD, TEST_DB_NAME, DB_USER


class StateTestCase(unittest.TestCase):
    """This class represents the state test case"""

    def setUp(self):
        """Defefine test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = TEST_DB_NAME
        self.database_path = 'postgresql://{}:{}@{}/{}'.format(
            DB_USER, DB_PASSWORD, 'localhost:5432', self.database_name)
        setup_db(self.app, self.database_name)

        self.state = {
            'name': 'Kaduna',
            'capital': 'Kaduna',
            'governor': 'Nasir Ahmad El-rufai'
        }

    def tearDown(self):
        """Executed after each test"""
        pass

    def test_get_paginated_states(self):
        res = self.client().get('/states')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['total_states'])
        self.assertTrue(len(data['states']))

    def test_404_sent_requesting_beyond_valid_page(self):
        res = self.client().get('/states?page=1000', json={'governor': 'Ridwan Salmanu'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')


if __name__ == "__main__":
    unittest.main()
