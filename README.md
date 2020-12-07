# Full Stack Capstone Project

## Full Stack Capstone

HeroKu URl: https://cap2m.herokuapp.com/
Local URl : http://127.0.0.1:5000/

## Motivation for project

My motivation for this project is to graduate from Udacity with FANS.

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

## Running local development

To run the server, execute:

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

## Running via HeroKu

is running via HeroKu url below:

HeroKu URl: https://cap2m.herokuapp.com/

## Authentication setting

All info about authentication can be found in setup.sh

For testing you can used Postman to test the endpoint

If token is expired used link below with info for each account:

https://m0ath.us.auth0.com/authorize?audience=Capstone&response_type=token&client_id=62SWGy85kGro6r0t41WIfcMzris4OjtK&redirect_uri=https://127.0.0.1:8080/login-results

Assistant
username: assistant@example.com
password: exa@123@

Director
username: director@example.com
password: exa@123@

Producer
username: producer@example.com
password: exa@123@

## API Reference

### Error Handling

Errors are returned as JSON objects in the following format:
```bash
{
    "success": False, 
    "error": 405,
    "message": "Method Not Allowed here :("
}
```

The API will return three error types when requests fail:

- 405: Method Not Allowed here :(
- 404: resource not found
- 422: unprocessable
- 500: Internal Server Error
- AuthError

### Endpoints

#### GET /actors

- General:
    Fetches list of actors
    Permissions : get:actors
- URl: https://cap2m.herokuapp.com/actors

 ```bash
{
    "actors": [
        {
            "age": 30,
            "gender": "male",
            "id": 1,
            "name": "mm"
        },
        {
            "age": 33,
            "gender": "male",
            "id": 2,
            "name": "tt"
        },
        {
            "age": 33,
            "gender": "male",
            "id": 3,
            "name": "t4"
        }
    ]
}
```

#### GET /movies

- General:
    Fetches list of movies
    Permissions : get:movies
- URl: https://cap2m.herokuapp.com/movies

 ```bash
{
    "movies": [
        {
            "id": 1,
            "release_date": "1990",
            "title": "rrr"
        },
        {
            "id": 3,
            "release_date": "1990",
            "title": "lkld"
        },
        {
            "id": 4,
            "release_date": "1990",
            "title": "iieui"
        }
    ]
}
```

#### DELETE /actors/<int:id>

- General:
    Deletes the actor of the given ID if it exists
    Permissions : delete:actors
- URl: https://cap2m.herokuapp.com/actor/1

```bash
{
    "delete": 1,
    "success": true
}
```

#### DELETE /movies/<int:id>

- General:
    Deletes the movie of the given ID if it exists
    Permissions : delete:movies
- URl: https://cap2m.herokuapp.com/movie/1

```bash
{
    "delete": 1,
    "success": true
}
```

#### POST /actors

- General:
    Post new actor with name, age and gender
    Permissions : post:actors
- URl: https://cap2m.herokuapp.com/actors

```bash
{
    "actors": {
        "age": 30,
        "gender": "male",
        "id": 1,
        "name": "moath"
    },
    "success": true
}
```

#### POST /movies

- General:
    Post new movie with title and release date
    Permissions : post:movies
- URl: https://cap2m.herokuapp.com/movies

```bash
{
    "movies": {
        "id": 1,
        "release_date": "1990",
        "title": "Movie"
    },
    "success": true
}
```

#### PATCH /actors/<int:id>

- General:
    Edit the actor of the given ID if it exists
    Permissions : patch:actors
- URl: https://cap2m.herokuapp.com/actors/1

```bash
{
    "actor": {
        "id": 1,
        "name": "newName",
        "age": 30,
        "gender": "male"
    },
    "success": true
}
```

#### PATCH /movies/<int:id>

- General:
    Edit the movie of the given ID if it exists
    Permissions : patch:movies
- URl: https://cap2m.herokuapp.com/movies/1

```bash
{
    "movie": {
        "id": 1,
        "release_date": "1991",
        "title": "movie"
    },
    "success": true
}
```


### Permissions and User

User: Assistant
Permissions: get:actors, get:movies

User: Director
Permissions: all the Permissions that Assistant have it, plus post:actors, patch:actors, delete:actors

User: Producer
Permissions: all the Permissions that Assistant and Director have it, plus patch:movies, post:movies, delete:movies

### Deployment

Project Deployment on HeroKu with URl: https://cap2m.herokuapp.com
### Author

Moath Alghanmy

### Acknowledgements

The awesome team at Udacity and all of the students, soon to be full stack extraordinaires!
