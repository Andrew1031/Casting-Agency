import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import setup_db, db_drop_and_create_all, Actor, Movie, SQLALCHEMY_DATABASE_URI, \
  db_drop_and_create_all_defaults
from config import paginate_results
from auth import AuthError, requires_auth

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  CORS(app)
  setup_db(app, SQLALCHEMY_DATABASE_URI)
  db_drop_and_create_all_defaults()

  # allow CORS permissions
  @app.after_request
  def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
    response.headers.add('Access-Control-Allow-Methods', 'GET, PATCH, POST, DELETE, OPTIONS')
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

  # ROUTES
  @requires_auth('get:actors')
  @app.route('/actors', methods=['GET'])
  def get_actors():
    actors = Actor.query.order_by(Actor.id).all()
    if len(actors) == 0:
      abort(404)
    actors_paginated = paginate_results(request, actors)

    return jsonify({
      'success': True,
      'actors': actors_paginated
    })

  @requires_auth('get:movies')
  @app.route('/movies', methods=['GET'])
  def get_movies():
    movies = Movie.query.order_by(Movie.id).all()
    if len(movies) == 0:
      abort(404)
    movies_paginated = paginate_results(request, movies)

    return jsonify({
      'success': True,
      'movies': movies_paginated
    })

  @requires_auth('delete:actor')
  @app.route('/actors/<actor_id>', methods=['DELETE'])
  def delete_actor(actor_id):
    actorToDelete = Actor.query.get(actor_id)
    if not actorToDelete:
      abort(404)
    actorToDelete.delete()
    return jsonify({
      'success': True,
      'deleted': actor_id
    })

  @requires_auth('delete:movie')
  @app.route('/movies/<movie_id>', methods=['DELETE'])
  def delete_movie(movie_id):
    movieToDelete = Movie.query.get(movie_id)
    if not movieToDelete:
      abort(404)
    movieToDelete.delete()
    return jsonify({
      'success': True,
      'deleted': movie_id
    })

  @requires_auth('post:actor')
  @app.route('/actors', methods=['POST'])
  def create_actor():
    body = request.get_json()
    name = body.get('name', None)
    age = body.get('age', None)
    gender = body.get('gender', None)
    if body.get('name') == '' or body.get('age') == '' or body.get('gender') == ''\
            or 'name' not in body or 'age' not in body or 'gender' not in body:
      abort(422)
    actor = Actor(name=name, age=age, gender=gender)
    actor.insert()
    return jsonify({
      'success': True,
      'created': actor.id
    })

  @requires_auth('post:movie')
  @app.route('/movies', methods=['POST'])
  def create_movie():
    body = request.get_json()
    title = body.get('title', None)
    date = body.get('release', None)
    if body.get('title') == '' or body.get('release') == '':
      abort(422)
    movie = Movie(title=title, release=date)
    movie.insert()
    return jsonify({
      'success': True,
      'created': movie.id
    })

  @requires_auth('patch:actor')
  @app.route('/actors/<actor_id>', methods=['PATCH'])
  def edit_actor(actor_id):
    body = request.get_json()
    if not body:
      abort(404)

    actor_to_edit = Actor.query.get(actor_id)
    if not actor_to_edit:
      abort(404)

    if 'name' in body and body['name']:
      actor_to_edit.name = body['name']

    if 'age' in body and body['age']:
      actor_to_edit.age = body['age']

    if 'gender' in body and body['gender']:
      actor_to_edit.gender = body['gender']

    actor_to_edit.update()
    return jsonify({
      'success': True,
      'edited': actor_to_edit.id,
      'actor': [actor_to_edit.format()]
    })

  @requires_auth('patch:movie')
  @app.route('/movies/<movie_id>', methods=['PATCH'])
  def edit_movie(movie_id):
    body = request.get_json()
    if not body:
      abort(404)

    movie_to_edit = Movie.query.get(movie_id)
    if not movie_to_edit:
      abort(404)

    if 'title' in body and body['title']:
      movie_to_edit.title = body['title']

    if 'release' in body and body['release']:
      movie_to_edit.release = body['release']

    movie_to_edit.update()
    return jsonify({
      'success': True,
      'edited': movie_to_edit.id,
      'movie': [movie_to_edit.format()]
    })

  # Error Handlers

  @app.errorhandler(404)
  def not_found(error):
    return jsonify({
      "success": False,
      "error": 404,
      "message": "Not found"
    }), 404

  @app.errorhandler(400)
  def bad_request(error):
    return jsonify({
      "success": False,
      "error": 400,
      "message": "Invalid request"
    }), 400

  @app.errorhandler(422)
  def unprocessable(error):
    return jsonify({
      "success": False,
      "error": 422,
      "message": "unprocessable"
    }), 422

  @app.errorhandler(500)
  def internal_server_error(error):
    return jsonify({
      "success": False,
      "error": 500,
      "message": "internal server error"
    }), 500

  @app.errorhandler(AuthError)
  def authError(e):
    return jsonify({
      'success': False,
      'error': e.status_code,
      'message': e.error
    }), e.status_code

  return app

APP = create_app()

# Default port:
if __name__ == '__main__':
    APP.run(debug=True)

