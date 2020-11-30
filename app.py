import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import setup_db, Movies, Actors

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  CORS(app)

  @app.route('/')
  def be_cool():
      return "Be cool, man, be coooool! You're almost a FSND grad!"

  

  return app

app = create_app()

if __name__ == '__main__':
    app.run()