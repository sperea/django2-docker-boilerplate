# django2_docker_boilerplate
A boilerplate for Django - Docker web applications 


## make initial migrations

docker-compose run web python3 manage.py migrate

## Start srvice containers

docker-compose up

## Verify

Simply hit the localhost i.e. http://localhost:8000 and you’ll have the Django homepage appear.