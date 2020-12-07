# Full Stack Capstone Project

## Full Stack Capstone

HeroKu URl: https://cap2m.herokuapp.com/
Local URl : http://127.0.0.1:5000/

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
