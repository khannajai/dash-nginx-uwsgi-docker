# Dash - nginx - uWSGI - Docker

Dash by Plotly is a Python framework to build elegant interactive dashboards for the web. This template can be used to create a Docker image that uses Flask, Nginx, and uWSGI to serve the application.

## Dockerize your Dash app

1. Create Docker image
```
docker build -t my_dashboard .
```

2. Run app in container
```
docker run -p 8080:80 my_dashboard
```
This will run the app on http://localhost:8080/.

The base image used in the Dockerfile: https://hub.docker.com/r/tiangolo/uwsgi-nginx-flask/. 