import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy


from app import create_app
from models import setup_db, Movie, Actor


class CapstoneTestCase(unittest.TestCase):
    """This class represents the Capstone test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.assistant = os.environ['ASSISTANT']
        self.director = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlNZRzQzay00MjZEajlxNmFoUzBOMyJ9.eyJpc3MiOiJodHRwczovL20wYXRoLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZmNiYTE1ODM4NTE4ZjAwNmYyYWY2YjEiLCJhdWQiOiJDYXBzdG9uZSIsImlhdCI6MTYwNzMyNDU2NiwiZXhwIjoxNjA3NDEwOTY2LCJhenAiOiI2MlNXR3k4NWtHcm82cjB0NDFXSWZjTXpyaXM0T2p0SyIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicG9zdDphY3RvcnMiXX0.MM4stffTEVgY7jge8eaR9PdgI90ofSS34xOytpZPHkGzbu7cBsag0Y5rX_DKXLDwsQm0Z_KZBF2Ee2jLV6Y2TlsFufo-2GbAT9hAH3jcqfUJ_tAN5AXFagYNcEdMC08B0MNwW3_FVc3BitYh787sQPp_8R3-XKSHv388mB7lOojA5icr1UmgAp3x4aWP6ZjucDKc3jUQEsIeXgqJk1sMHIKcJeduJHpp-ICQ_r2J-zinxWRcTMzJzaEO-L3LR81pR8qR21guCgbWIVCiLsU105DWDtFx0-RmH8QWiUYpcYllSkBSiMANAAX9UK4P0MUPMrYBC86yCufNyx73zk0TSA'
        self.producer = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlNZRzQzay00MjZEajlxNmFoUzBOMyJ9.eyJpc3MiOiJodHRwczovL20wYXRoLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZmNiYTRiODgwNDEwNzAwNzYxMWUxODAiLCJhdWQiOiJDYXBzdG9uZSIsImlhdCI6MTYwNzMyNDcxMiwiZXhwIjoxNjA3NDExMTEyLCJhenAiOiI2MlNXR3k4NWtHcm82cjB0NDFXSWZjTXpyaXM0T2p0SyIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIiwicG9zdDptb3ZpZXMiXX0.WUd19Bb23onB7VHQtrDjXKRAM-0yEbofiXZusI_HccWZb_6_8DA4RBLgLdNQ8rIePNDbTbXXF9jdu10fxlu4zs8jGTrS_3DA_D5IEtaOnE-JzBgykbffnyDvwIBqdGtz-ZJg3-mP0jHCT3QxPcxHSEqlAHJDavlkxRADfOU9xI7ciYj1q76TeEVyfsjKC6_TbiQKViRb1QfeMIeI_FYrXFONcwZe2amv7u9hvJvBPo1cMvl20oZx5Q-VSp2n1HaEwWY_gJhKlKkm82V9XpulHW1o6Ji8v_kMAVSAqkO4kDMZ8tyD-tVDuCOgHhrzCafZnkvYEOqYyxByl5N8fYRaoA'
        
        # new actors
        self.new_actor = {
            'name': 'moath',
            'age': '30',
            'gender': 'male'
        }

        # update actors
        self.update_actor = {
            'name': 'upActor',
            'age': '22',
            'gender': 'male'
        }

        # new movies
        self.new_movie = {
            'title': 'myMovie',
            'release_date': '1990'
        }

        # update movies
        self.update_movie = {
            'title': 'upMovie',
            'release_date': '2009'
        }

    def tearDown(self):
        """Executed after reach test"""
        pass

    # All the test start form here
    # test to get actors with success
    def test_get_actors_success(self):
        res = self.client().get(
            '/actors',
            headers={
                "authorization": "Bearer {}".format(
                    self.assistant)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors'])

    # test to get actors with error
    def test_get_actors_error(self):
        res = self.client().get('/actors')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['code'], 'authorization_header_missing')
        self.assertEqual(
            data['description'],
            'Authorization header is expected.')

    # test to get movies with success
    def test_get_movies_success(self):
        res = self.client().get(
            '/movies',
            headers={
                "authorization": "Bearer {}".format(
                    self.assistant)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])

    # test to get movies with error
    def test_get_movies_error(self):
        res = self.client().get('/movies')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['code'], 'authorization_header_missing')
        self.assertEqual(
            data['description'],
            'Authorization header is expected.')

    # test to delete actors with success
    def test_delete_actors_success(self):
        actor = Actor(
            name=self.new_actor['name'],
            age=self.new_actor['age'],
            gender=self.new_actor['gender'])
        actor.insert()

        res = self.client().delete(
            f'/actors/{actor.id}',
            headers={
                "authorization": "Bearer {}".format(
                    self.director)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['delete'])

    # test to delete actors with error
    def test_delete_actors_error(self):
        res = self.client().delete(
            '/actors/1000',
            headers={
                "authorization": "Bearer {}".format(
                    self.director)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

    # test to delete actors with assistant
    def test_delete_actors_with_assistant(self):
        res = self.client().delete(
            '/actors/1',
            headers={
                "authorization": "Bearer {}".format(
                    self.assistant)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['code'], 'unauthorized_header')
        self.assertEqual(
            data['description'],
            'Authorization header must have valid permissions.')

    # test to delete actors with producer
    def test_delete_actors_with_producer(self):
        actor = Actor(
            name=self.new_actor['name'],
            age=self.new_actor['age'],
            gender=self.new_actor['gender'])
        actor.insert()

        res = self.client().delete(
            f'/actors/{actor.id}',
            headers={
                "authorization": "Bearer {}".format(
                    self.producer)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['delete'])

    # test to delete movies with success
    def test_delete_movies_success(self):
        movie = Movie(
            title=self.new_movie['title'],
            release_date=self.new_movie['release_date'])
        movie.insert()

        res = self.client().delete(
            f'/movies/{movie.id}',
            headers={
                "authorization": "Bearer {}".format(
                    self.producer)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['delete'])

    # test to delete movies with error
    def test_delete_movies_error(self):
        res = self.client().delete(
            '/movies/1000',
            headers={
                "authorization": "Bearer {}".format(
                    self.producer)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

    # test to delete movies with assistant
    def test_delete_movies_with_assistant(self):
        res = self.client().delete(
            '/movies/1',
            headers={
                "authorization": "Bearer {}".format(
                    self.assistant)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['code'], 'unauthorized_header')
        self.assertEqual(
            data['description'],
            'Authorization header must have valid permissions.')

    # test to delete movies with director
    def test_delete_movies_with_director(self):
        res = self.client().delete(
            '/movies/1',
            headers={
                "authorization": "Bearer {}".format(
                    self.director)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['code'], 'unauthorized_header')
        self.assertEqual(
            data['description'],
            'Authorization header must have valid permissions.')

    # test to post actors with success
    def test_post_actors_success(self):
        res = self.client().post(
            '/actors',
            json=self.new_actor,
            headers={
                "authorization": "Bearer {}".format(
                    self.director)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors'])

    # test to post actors with error
    def test_post_actors_error(self):
        res = self.client().post(
            '/actors/45',
            json=self.new_actor,
            headers={
                "authorization": "Bearer {}".format(
                    self.director)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Method Not Allowed here :(')

    # test to post actors with assistant
    def test_post_actors_with_assistant(self):
        res = self.client().post(
            '/actors',
            json=self.new_actor,
            headers={
                "authorization": "Bearer {}".format(
                    self.assistant)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['code'], 'unauthorized_header')
        self.assertEqual(
            data['description'],
            'Authorization header must have valid permissions.')

    # test to post actors with producer
    def test_post_actors_with_producer(self):
        res = self.client().post(
            '/actors',
            json=self.new_actor,
            headers={
                "authorization": "Bearer {}".format(
                    self.producer)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors'])

    # test to post movies with success
    def test_post_movies_success(self):
        res = self.client().post(
            '/movies',
            json=self.new_movie,
            headers={
                "authorization": "Bearer {}".format(
                    self.producer)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])

    # test to post movies with error
    def test_post_movies_error(self):
        res = self.client().post(
            '/movies/45',
            json=self.new_actor,
            headers={
                "authorization": "Bearer {}".format(
                    self.producer)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Method Not Allowed here :(')

    # test to post movies with assistant
    def test_post_movies_with_assistant(self):
        res = self.client().post(
            '/movies',
            json=self.new_actor,
            headers={
                "authorization": "Bearer {}".format(
                    self.assistant)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['code'], 'unauthorized_header')
        self.assertEqual(
            data['description'],
            'Authorization header must have valid permissions.')

    # test to post movies with director
    def test_post_movies_with_director(self):
        res = self.client().post(
            '/movies',
            json=self.new_actor,
            headers={
                "authorization": "Bearer {}".format(
                    self.director)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['code'], 'unauthorized_header')
        self.assertEqual(
            data['description'],
            'Authorization header must have valid permissions.')

    # test to patch actors with success
    def test_patch_actors_success(self):
        actor = Actor(
            name=self.new_actor['name'],
            age=self.new_actor['age'],
            gender=self.new_actor['gender'])
        actor.insert()
        res = self.client().patch(
            f'/actors/{actor.id}',
            json=self.update_actor,
            headers={
                "authorization": "Bearer {}".format(
                    self.director)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actor'])

    # test to patch actors with error
    def test_patch_actors_error(self):
        res = self.client().patch(
            '/actors/2000',
            json=self.update_actor,
            headers={
                "authorization": "Bearer {}".format(
                    self.director)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

    # test to patch actors with assistant
    def test_patch_actors_with_assistant(self):
        res = self.client().patch(
            '/actors/1',
            json=self.update_actor,
            headers={
                "authorization": "Bearer {}".format(
                    self.assistant)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['code'], 'unauthorized_header')
        self.assertEqual(
            data['description'],
            'Authorization header must have valid permissions.')

    # test to patch actors with producer
    def test_patch_actors_with_producer(self):
        actor = Actor(
            name=self.new_actor['name'],
            age=self.new_actor['age'],
            gender=self.new_actor['gender'])
        actor.insert()
        res = self.client().patch(
            f'/actors/{actor.id}',
            json=self.update_actor,
            headers={
                "authorization": "Bearer {}".format(
                    self.producer)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actor'])

    # test to patch movies with success
    def test_patch_movies_success(self):
        movie = Movie(
            title=self.new_movie['title'],
            release_date=self.new_movie['release_date'])
        movie.insert()
        res = self.client().patch(
            f'/movies/{movie.id}',
            json=self.update_movie,
            headers={
                "authorization": "Bearer {}".format(
                    self.producer)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movie'])

    # test to patch movies with error
    def test_patch_movies_error(self):
        res = self.client().patch(
            '/movies/2000',
            json=self.update_movie,
            headers={
                "authorization": "Bearer {}".format(
                    self.producer)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

    # test to patch movies with assistant
    def test_patch_movies_with_assistant(self):
        res = self.client().patch(
            '/movies/1',
            json=self.update_movie,
            headers={
                "authorization": "Bearer {}".format(
                    self.assistant)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['code'], 'unauthorized_header')
        self.assertEqual(
            data['description'],
            'Authorization header must have valid permissions.')

    # test to patch movies with producer
    def test_patch_movies_with_producer(self):
        res = self.client().patch(
            '/movies/1',
            json=self.update_movie,
            headers={
                "authorization": "Bearer {}".format(
                    self.director)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['code'], 'unauthorized_header')
        self.assertEqual(
            data['description'],
            'Authorization header must have valid permissions.')


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
