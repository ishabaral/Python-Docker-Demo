# Python Docker Demo

A minimal Flask app for demonstrating Docker image creation and Docker Hub publishing.

## Build

```bash
docker build -t python-docker-demo:1.0 .
```

## Run

```bash
docker run --rm -p 5001:5001 python-docker-demo:1.0
```

Visit http://localhost:5001 or http://localhost:5001/health.

## Push to Docker Hub

Replace YOUR_DOCKERHUB_USERNAME with your actual username:

```bash
docker login
docker tag python-docker-demo:1.0 YOUR_DOCKERHUB_USERNAME/python-docker-demo:1.0
docker push YOUR_DOCKERHUB_USERNAME/python-docker-demo:1.0
```

## Pull and run

```bash
docker pull YOUR_DOCKERHUB_USERNAME/python-docker-demo:1.0
docker run --rm -p 5001:5001 YOUR_DOCKERHUB_USERNAME/python-docker-demo:1.0
```

--------------------------------

## docker-compose 

```bash
docker compose up
```
command is not used in web so it uses default from the Dockerfile
api replaces that cmd with: `python api.py`

The depends_on command makes sure the api container is up and running before the web: 
```bash
depends_on:
    - api
```

## Volumes

Docker volumes are managed by Docker and are suitable for persistent application data.
Bind mounts link a specific host directory or file to a container.
Volumes are easier to manage across Docker environments, while bind mounts provide direct access to host files.


1. To demonstrate the concept, first start the container without volume

Data is lost once you stop the container, so how can the data be persistent?

```bash
docker build -t python-docker-demo:2.0 . 

docker run --rm -p 5001:5001 python-docker-demo:2.0
```
2. Reload the page several times (notic the value of count)
3. Stop container using crtl+C


4. Now specify volume:

```bash
docker run --rm -p 5001:5001 -v my_python_demo:/app/data python-docker-demo:2.0
```

or can also create volume first using `docker volume create <volume_name>`

5. when starting the container, make sure the previous count is already gone i.e count=0

6. Restart the page several times
7. Crtl+C
8. again restart the container using 4, but the count data should persist because of volume

9. show where volume actually lives

```bash

docker volume ls 

docker volume inspect my_python_demo

sudo ls /var/lib/docker/volumes/my_python_demo/_data

sudo cat /var/lib/docker/volumes/my_python_demo/_data/count.txt 
```

10. Remove volume 

```bash
docker volume rm my_python_demo
docker volume ls
```

### Bind-mount

```bash
mkdir bind-mount

docker run --rm -p 5001:5001 -v ./bind-mount:/app/data python-docker-demo:3.0 

cat bind-mount/count.txt 

```