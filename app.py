import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from models import setup_db, Movie, Actor
from auth import AuthError, requires_auth


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    # For Fun :D
    @app.route('/')
    def be_cool():
        return "I'm cool, man, I'm coooool! I'm almost a FSND grad!"

    # GET actors endpoint
    @app.route('/actors', methods=['GET'])
    @requires_auth('get:actors')
    def get_actors(payload):
        actors = Actor.query.all()
        if len(actors) == 0:
            abort(404)

        try:
            formatted_actors = [actor.format() for actor in actors]
            return jsonify({
                "success": True,
                "actors": formatted_actors
            }), 200

        except Exception:
            abort(422)

    # GET movies endpoint
    @app.route('/movies', methods=['GET'])
    @requires_auth('get:movies')
    def get_movies(payload):
        movies = Movie.query.all()
        if len(movies) == 0:
            abort(404)

        try:
            formatted_movies = [movie.format() for movie in movies]
            return jsonify({
                "success": True,
                "movies": formatted_movies
            }), 200

        except Exception:
            abort(422)

    # DELETE actors endpoint
    @app.route('/actors/<int:id>', methods=['DELETE'])
    @requires_auth('delete:actors')
    def delete_actors(payload, id):
        actor = Actor.query.filter(Actor.id == id).one_or_none()
        if actor is None:
            abort(404)

        try:
            actor.delete()
            return jsonify({
                "success": True,
                "delete": actor.id
            }), 200

        except Exception:
            abort(422)

    # DELETE movies endpoint
    @app.route('/movies/<int:id>', methods=['DELETE'])
    @requires_auth('delete:movies')
    def delete_movies(payload, id):
        movie = Movie.query.filter(Movie.id == id).one_or_none()
        if movie is None:
            abort(404)

        try:
            movie.delete()
            return jsonify({
                "success": True,
                "delete": movie.id
            }), 200

        except Exception:
            abort(422)

    # POST actors endpoint
    @app.route('/actors', methods=['POST'])
    @requires_auth('post:actors')
    def post_actors(payload):
        body = request.get_json()
        new_name = body.get('name')
        new_age = body.get('age')
        new_gender = body.get('gender')

        try:
            actor = Actor(name=new_name, age=new_age, gender=new_gender)
            actor.insert()
            return jsonify({
                "success": True,
                "actors": actor.format()
            }), 200

        except Exception:
            abort(500)

    # POST movies endpoint
    @app.route('/movies', methods=['POST'])
    @requires_auth('post:movies')
    def post_movies(payload):
        body = request.get_json()
        new_title = body.get('title')
        new_release_date = body.get('release_date')

        try:
            movie = Movie(title=new_title, release_date=new_release_date)
            movie.insert()
            return jsonify({
                "success": True,
                "movies": movie.format()
            }), 200

        except Exception:
            abort(500)

    # PATCH actors endpoint
    @app.route('/actors/<int:id>', methods=['PATCH'])
    @requires_auth('patch:actors')
    def edit_actors(payload, id):
        actor = Actor.query.filter(Actor.id == id).one_or_none()
        if actor is None:
            abort(404)

        try:
            body = request.get_json()
            if body.get('name'):
                actor.name = body.get('name', None)
            if body.get('age'):
                actor.age = body.get('age', None)
            if body.get('gender'):
                actor.gender = body.get('gender', None)
            actor.update()

            return jsonify({
                "success": True,
                "actor": actor.format()
            }), 200

        except Exception:
            abort(422)

    # PATCH movies endpoint
    @app.route('/movies/<int:id>', methods=['PATCH'])
    @requires_auth('patch:movies')
    def edit_movies(payload, id):
        movie = Movie.query.filter(Movie.id == id).one_or_none()
        if movie is None:
            abort(404)

        try:
            body = request.get_json()
            if body.get('title'):
                movie.title = body.get('title', None)
            if body.get('release_date'):
                movie.release_date = body.get('release_date', None)
            movie.update()

            return jsonify({
                "success": True,
                "movie": movie.format()
            }), 200

        except Exception:
            abort(422)

    # Error Handling
    '''
    Error handling for unprocessable entity
    '''
    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
        }), 422

    '''
    Error handling for Internal Server Error
    '''
    @app.errorhandler(500)
    def server_error(error):
        return jsonify({
            "success": False,
            "error": 500,
            "message": "Internal Server Error"
        }), 500

    '''
    Error handling for resource not found
    '''
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "resource not found"
        }), 404

    '''
    Error handling for method not allowed
    '''
    @app.errorhandler(405)
    def method_not_allowed(error):
        return jsonify({
            'success': False,
            'error': 405,
            'message': 'Method Not Allowed here :('
        }), 405

    '''
    Error handling for AuthError
    '''
    @app.errorhandler(AuthError)
    def handle_auth_error(ex):
        response = jsonify(ex.error)
        response.status_code = ex.status_code
        return response

    # The End :)
    return app


app = create_app()

if __name__ == '__main__':
    app.run()
