#### Dockerizing a Flask

Login to Docker Hub

```zsh
$ docker login
```

create a Flask container

```zsh
$ docker build -t {yourDockerUsername}/spring-boot-api:1.0.0 .
```

Test the Flask container by running it. It should be visible at localhost:8080

```zsh
$ docker run -p 8080:5000 {yourDockerUsername}/spring-boot-api:1.0.0
```

Push the container to your Docker Hub account repository

```zsh
$ docker push {yourDockerUsername}/spring-boot-api:1.0.0
```
