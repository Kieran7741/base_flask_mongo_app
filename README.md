# Run Flask and MongoDB using docker-compose

When dealing with multi container applications you should define the application in a docker-compose.yml file. This file defines how the different componets of the app should be run and how they interact.

## App components

The app uses a `web` and `db` container. The `web` container runs the Flask webserver while the `db` container runs MongoDB.

**Note:** `build .` indicates that the `DockerFile` in the current directory should be used to build the image.

* docker-compose.yml

```yaml
web:
    build: .
    command: python app.py
    ports:
        - '5000:5000'
    volumes:
        - .:/app
    links:
        - db
db:
    image: mongo
```

* Dockerfile

```Dockerfile
FROM python:3.6
ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt
```

## Run

* `build` with use the definitions in `docker-compose.yml` to pull and build images locally
* `up` with run the built images with the meta data provided in `docker-compose.yml`

```commandline
> docker-compose build
> docker-compose up
```
