# bookstore
docker ps   for pid list
docker network ls   for list of actuive interfaces
docker images       list of all images
docker -d   start as detached or demon, so also when quitting the console this stuff still runs
docker -it  after launch keep the app open for interaction
docker exec start a command
    docker exec -it <docker pid> /bin/bash      to start the bash shell when open the container
        psql -U <username> -d <database>    connect to db
docker compose up -d --build    make use of the docker-compose.yml file to start up
                                a bundle project    (start this within the folder of the file)
docker compose down     to stop the container bundle
docker stop <container name>     to stop an active container
docker start <container name>    to start an already previously started and now stopped container
docker build -t <new image name> <src app path>
docker (image) tag <source image><: optional tag if exists> <target imagename>:<new tag name like latest>
                                this in order to push later to dockerhub
docker (image) push <docker login>/<image including tag>
docker rm <container name>      removes a non running container (not image)
docker network create <new docker network name> create a new virtual network in docker engine
docker network inspect <docker network name>    shows all params of the Network confirguration
docker run <docker image name>  default it will looking locally
                                and then on dockerhub if it finds package to download automatically
                Options depending on app
    --name <container name>     define new name of container   
    --net <docker network name> Network name defined in docker to communicated between containers
    -P                          Random port
    -p <port from : port to>    Port of chosing
