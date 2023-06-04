# Flask Boilerplate

# Setup

#### Run the following commands:

1. `export FLASK_APP=run.py`
2. `pip install -r requirements.txt`
3. `flask db init`
4. `flask db migrate -m "initial migration"`

#### Upgrade schema

1. `flask db migrate -m "initial migration"` 
2. `flask db upgrade`


### Run the app

`python3 run.py`

### REST APIs

1. Register new user

```sh
curl -X POST -H "Content-Type: application/json" -d '{"username":"exampleUser","email":"example@domain.com","password":"securePassword123"}' http://localhost:5000/api/users
```

2. Get users
   
```sh
curl -X GET http://localhost:5000/api/users
```

