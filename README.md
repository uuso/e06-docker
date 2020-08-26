# e06-docker
docker-flask-cache

app without docker-compose:

Guide to test app:
0. Create personal subnet:
- docker network create my-network
1. Run the memcached container:
- docker run --name cachesrv-inner --net=my-network -d memcached
2. build & run flask container:
- docker build --tag flask-cached:v0.1 .
- docker run --name flask-cached --net=my-network -p 80:5001 flask-cached:v0.1
3. send GET request to http://hostname/?k=1000 -- you should get '268638 ... 74626'
