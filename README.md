# e06-docker
docker-flask-cache

app without docker-compose:

Guide to test app:
1. Run the memcached container:
- docker run --name=my_memc_host --network="host" -d memcached:1.6.6-alpine
2. build & run flask container:
- docker build --tag flask:mc-docker .
- docker run -p 80:80 flask:mc-docker
3. send GET request to http://hostname/?k=10 -- you should get '34'
