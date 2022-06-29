NG-STATES - API
===============

## Setting up Development Environment

### Install Dependencies

1. **Python 3.7** - Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

2. **Virtual Environment** - I recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organized. Instructions for setting up a virual environment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

```
python -m virtualenv env
source env/bin/activate
```
>**Note** - In Windows, the `env` does not have a `bin` directory. Therefore, you'd use the analogous command shown below:
```
source env/Scripts/activate
```

3. **PIP Dependencies** - Once your virtual environment is setup and running, install the required dependencies by running:

```bash
pip install -r requirements.txt
```

#### Key Pip Dependencies

- [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use to handle the lightweight SQL database. You'll primarily work in `app.py`and can reference `models.py`.

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross-origin requests from our frontend server.

### Run the development server:
```
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

**Verify on the Browser**<br>
Navigate to project homepage [http://127.0.0.1:5000/](http://127.0.0.1:5000/) or [http://localhost:5000](http://localhost:5000) 

## Setting up Database
> Note that this project is built using local database. To use this, you have to set up your local database in [`models.py`](models.py) and populate it with necessary inputs

- To Connect the project with your local database, update the `database_path` in [models.py](models.py) file with your database `NAME, USER and PASSWORD`

## NG-STATE API Endpoints

- GET `/states`
  - Returns all states available in the country
  - Countries are displayed 10 per page
  - Returns success value, list of states and total number of states
  - Returns 404 error if no state exist in database
  - URI: `http://localhost:5000/states`
  - Response:

```
  {
  "states": [
    {
      "capital": "Maidugur", 
      "governor": "Ridwan Salmanu", 
      "id": 1, 
      "name": "Borno"
    }, 
    {
      "capital": "Ikeja", 
      "governor": "Ganduje Lawal", 
      "id": 2, 
      "name": "Lagos"
    } 
  ], 
  "success": true, 
  "total_states": 2
}
```

- POST `/states`
  - Creates a new state
  - Returns the succes value, id of state created, all the states avalable as well as the total number of states
  - URI: `curl http://localhost:5000/states -X POST -H "Content-Type: application/json" -d '{"name": "Cross-river", "capital": "Calabar", "governor": "Amechi"}'`
  - Response:
```
    {
  "created": 4, 
  "states": [
    {
      "capital": "Kaduna", 
      "governor": "Ridwan Salmanu", 
      "id": 1, 
      "name": "Kaduna"
    }, 
    {
      "capital": "Kano", 
      "governor": "Ganduje Lawal", 
      "id": 2, 
      "name": "kano"
    }, 
    {
      "capital": "Jalingo", 
      "governor": "Faruk Shehu Hamza", 
      "id": 3, 
      "name": "Taraba"
    }, 
    {
      "capital": "Calabar", 
      "governor": "Amechi", 
      "id": 4, 
      "name": "Cross-river"
    }
  ], 
  "success": true, 
  "total_states": 4
}
```

- GET `/states/3`
  - Returns a specific question based on the id provided. On this case 3
  - Returns success value, and values of state with respect to the id provided. On this case 3
  - URI: `curl http://localhost:5000/states/3`
  - Response:
```
{
  "state": {
    "capital": "Kano", 
    "governor": "Ganduje Lawal", 
    "id": 3, 
    "name": "kano"
  }, 
  "success": true
}
```

- DELETE `/states/2`
  - Deletes a specific state based on the id provided
  - Returns success value, id of state deleted, available states and total number of the available states
  - URI: `curl http://localhost:5000/states/4 -X DELETE -H "Content-Type: application/json"`
  
```
    'deleted': 4,
    'success': True,
    'total_states: 3
```

- PATCH `/states/10`
  - Update the governor of a state
  - Returns success value and the id of state updated
  - URI: `curl -X PATCH http://localhost:5000/states/10 -H "Content-Type: application/json" -d '{"governor": "Lawal Yahaya"}'`
  - Response:
```
    {
        "id": 10, 
        "success": true
    }
```
