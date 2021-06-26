import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, Actor, Movie, db_drop_and_create_all_defaults
from config import SQLALCHEMY_UNIT_TEST_URI

class TriviaTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.database_path = SQLALCHEMY_UNIT_TEST_URI
        setup_db(self.app, self.database_path)
        db_drop_and_create_all_defaults()

        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            self.db.create_all()


    def tearDown(self):
        pass

    """
    Unit test cases. Two tests each, one successful operation and one expected error
    """

    def test_get_actor(self):
        res = self.client.get('/actors')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors'])

    def test_get_actor_fail(self):
        res = self.client.get('/actors')
        data = json.loads(res.data)

    def test_get_movie(self):
        res = self.client.get('/movies')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])

    def test_get_movie_fail(self):
        res = self.client.get('/movies')
        data = json.loads(res.data)

    def test_delete_actor(self):
        toDelete = Actor(name="Kid Cudi", age=37, gender="Male")
        toDelete.insert()
        toDelete_id = str(toDelete.id)
        res = self.client.delete(f'/actors/{toDelete_id}')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], toDelete_id)

    def test_delete_actor_fail(self):
        toDelete_id = str('99999')
        res = self.client.delete(f'/actors/{toDelete_id}')

        # data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)

    def test_delete_movie(self):
        toDelete = Movie(title="Avengers", release="2012")
        toDelete.insert()
        toDelete_id = str(toDelete.id)
        res = self.client.delete(f'/movies/{toDelete_id}')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], toDelete_id)

    def test_delete_movie_fail(self):
        toDelete_id = str('99999')
        res = self.client.delete(f'/movies/{toDelete_id}')

        # data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)

    def test_create_actor(self):
        toSubmit = {
            'name': 'Christian Serratos',
            'age': 30,
            'gender': 'Female'
        }

        res = self.client.post('/actors', json=toSubmit)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_create_actor_fail(self):
        toSubmit = {
            'name': 'John Cena',
            'age': 44
        }

        res = self.client.post('/actors', json=toSubmit)
        # data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)

    def test_create_movie(self):
        toSubmit = {
            'title': 'Joker',
            'release_date': '2019'
        }

        res = self.client.post('/movies', json=toSubmit)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_create_movie_fail(self):
        toSubmit = {
            'title': 'Logan'
        }

        res = self.client.post('/actors', json=toSubmit)
        # data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)

    def test_edit_actor(self):
        toEdit = Actor(name="Norman Reedus", age=52, gender="Male")
        toEdit.insert()
        toEdit_id = str(toEdit.id)
        newData = {
            'name': "Andrew Lincoln",
            'age': 47
        }
        res = self.client.patch(f'/actors/{toEdit_id}', json=newData)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['actor'][0]['age'], 47)
        self.assertEqual(data['actor'][0]['gender'], "Male")
        self.assertEqual(data['actor'][0]['name'], "Andrew Lincoln")

        femaleData = {
            'name': 'Alexa Bliss',
            'age': 29,
            'gender': 'Female'
        }

        res = self.client.patch(f'/actors/{toEdit_id}', json=femaleData)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['actor'][0]['age'], 29)
        self.assertEqual(data['actor'][0]['gender'], "Female")
        self.assertEqual(data['actor'][0]['name'], "Alexa Bliss")

    def test_edit_actor_fail(self):
        res = self.client.patch('/actors/99999')
        # data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)

    def test_edit_movie(self):
        toEdit = Movie(title="The Conjuring", release="2021")
        toEdit.insert()
        toEdit_id = str(toEdit.id)
        newData = {
            'title': 'X-Men',
            'release': '2017'
        }
        res = self.client.patch(f'/movies/{toEdit_id}', json=newData)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['movie'][0]['title'], 'X-Men')
        self.assertEqual(data['movie'][0]['release'], '2017')

        afterEdit = {
            'title': 'Invincible',
            'release': '2022'
        }
        res = self.client.patch(f'/movies/{toEdit_id}', json=afterEdit)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['movie'][0]['title'], 'Invincible')
        self.assertEqual(data['movie'][0]['release'], '2022')

    def test_edit_movie_fail(self):
        res = self.client.patch('/movies/99999')
        # data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()