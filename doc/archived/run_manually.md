# Flask Boilerplate

# Setup

> Pull postgres docker image
   1. `docker pull postgres`

   
## Options 
1. ## Docker network

   1. Run with docker network
      1.  Create docker network
       2.  `docker network create flask_psql_network`
   2.  Run postgres with network
       1. `docker run --name my-postgres --network flask_psql_network -p 5432:5432 -e POSTGRES_PASSWORD=mysecretpassword -d postgres`

   3. Run the flask app
      1. `sh redploy.sh`
   4. Access the flask app
      1. `http://0.0.0.0:9000/api/test`

 

2. ## Local
   1. Run without docker network
      1. `docker run --name my-postgres -e POSTGRES_PASSWORD=mysecretpassword -p 0.0.0.0:5432:5432 -d postgres`

## Flask

### Run the flask_psql container
`docker run --name flask_psql --network flask_psql_network -p 5000:5000 -d flask_psql`

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

