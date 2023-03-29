# Docker-Compose

This markdown holds a few docker-compose instructions and commands that will help you get started.

## Setting up your YAML file
*REMEMBER:* Use spaces *NOT* tabs in YAML files.

### Basic structure

```yaml
version: "3.9"
services:
    service-one:
        args
    service-two:
        args
```

Unlike a Dockerfile, your YAML file will contain both information required to *build* your image, and information required to
*run* that image in a container.
This means port numbers, volume mounts, resource limits, and pretty much everything else is going to be in this file.

This is an example of a completed docker compose configuration file:

```yaml
version: "3.9"
services:
  web:
    build: .
    ports:
      - "5001:5000"
    depends_on:
      - redis
    command: python app.py
  redis:
    image: redis
```

So there's two services, two final images, and (at least) two containers:

A service named `web`, with its image built from a Dockerfile that will reside in the current directory (`build: .`),
and a port bind from 5001 to the container's 5000, and this service depends on the `redis` service.
It also runs `python app.py` once it starts (run command).

`redis` is the second service, which is only a container with default run arguments, and it runs the `redis` image from Docker
hub.

### Versions
Versions can be specified in the YAML file with the `version` key, but since version `1.27.0` it has been an optional argument.
We're going to stick to version `'3'` in CS 322.

## Compose commands
First make sure you have docker compose:

```
which docker-compose
```

OR:

```
docker compose -h
```

### Starting your services
This command will spin everything up:

```
docker compose up
```

Run in detached mode (similar to using `-d` in `docker run`):

```
docker compose up -d
```

Force rebuilding images:

```
docker compose up --build
```

Skip rebuilding images:

```
docker compose up --no-build
```

It will build and run everything and ensures dependencies are met.

Optionally, you can build and run separately:

```
docker compose build
docker compose run
```

### Stopping services
```
docker compose down
```

If you want to go the extra step and remove the images it built as well, use `--rmi local`:

```
docker compose down --rmi local
```

If you want to remove even images it fetched from Docker hub (i.e. apache, redis, mongo, python), run this:

(USE WITH CAUTION)

```
docker compose down --rmi all
```

### Restarting
Restart all services:

```
docker compose restart
```

### Viewing output logs
If you ran in detached mode, or are just looking to view service outputs, use:

```
docker compose logs
```

### Executing commands / interactive shell,
You can still use the old docker commands on containers set up by compose, there's no magic here.
But compose makes everything easier.

If you need to execute a command in a running container, you don't have to look up container name any more. Just reference by
service name:

```
docker compose exec $SERVICE $COMMAND
```

For example:

```
docker compose exec web /bin/bash
```
