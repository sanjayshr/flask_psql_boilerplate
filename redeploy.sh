#!/bin/bash

# Stop the existing container
docker stop flask_psql

# Remove the existing container
docker rm flask_psql

# Rebuild the Docker image
docker build -t flask_psql .

# Run a new container from the rebuilt image
docker run -d -p 9000:5000 --network flask_psql_network --name flask_psql flask_psql
