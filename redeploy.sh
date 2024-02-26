#!/bin/bash

# Rebuild the Flask app image
docker-compose build web

# Stop the current Flask app service and start a new one with the rebuilt image
docker-compose up -d --no-deps web