# Python Docker Demo

A minimal Flask app for demonstrating Docker image creation and Docker Hub publishing.

## Build

```bash
docker build -t python-docker-demo:1.0 .
```

## Run

```bash
docker run --rm -p 5000:5000 python-docker-demo:1.0
```

Visit http://localhost:5000 or http://localhost:5000/health.

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
docker run --rm -p 5000:5000 YOUR_DOCKERHUB_USERNAME/python-docker-demo:1.0
```
