# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory in the container to /app
WORKDIR /app

# Add requirements.txt before other files for caching
ADD requirements.txt /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Add the current directory contents into the container at /app
ADD . /app

# Make port 9000 available to the world outside this container
EXPOSE 9000

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "run.py"]
