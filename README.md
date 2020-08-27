# e06-docker
app to calculate Fibonacci numbers with ordination number specifying as GET parameter 'k'

**app without docker-compose:**

### Guide to test app:
1. Create personal subnet:
`docker network create my-network`
1. Run the memcached container:
`docker run --name cachesrv-inner --net=my-network -d memcached`
1. build & run flask container:
`docker build --tag flask-cached:v0.1 .`
`docker run --name flask-cached --net=my-network -p 80:5001 flask-cached:v0.1`
1. send GET request to `http://hostname/?k=1000` -- you should get '268638 ... 74626'


**docker-compose installation:**
`sudo curl -L "https://github.com/docker/compose/releases/download/1.26.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose`

`sudo chmod +x /usr/local/bin/docker-compose`

**app with docker-compose:**
1. run `docker-compose up`