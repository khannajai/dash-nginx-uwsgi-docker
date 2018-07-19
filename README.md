# Dash - nginx - uWSGI - Docker

Dash by Plotly is a Python framework to build elegant interactive dashboards for the web. The aim of this project is to allow smooth development and deployment of Dash apps by creation of a docker image that uses flask, nginx, and uWSGI under the hood.

## Dockerize your Dash app

1. Create Docker image
```
docker build -t my_dashboard .
```

2. Run app in container
```
docker run --net=host my_dashboard
```
This will run the app on http://localhost:80/.

The base image used in the Dockerfile: https://hub.docker.com/r/tiangolo/uwsgi-nginx-flask/. 