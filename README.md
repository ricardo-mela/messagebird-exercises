# messagebird-exercises

## Exercise 1

Write and deploy a web-server application in any language of your choice to kubernetes cluster 
running in any cloud provider of your choice. 
 
This Web app must show Homer Simpson picture when accessing /homersimpson and the time in the moment of request in Covilha City (Portugal) when accessing /covilha. 
 
- Run on a static-IP 
 
- Only the port 80 should be open 
 
- Application should have built-in prometheus exporter and provide two metrics: 
-- Total number of requests to /homersimpson uri 
-- Total number of requests to /covilha uri 

### My approach

I will use EKS as the Kubernetes solution because it is easier for me to set up.

I am creating a Docker container to run the solution using Flask and Gunicorn to run a python application providing both metrics.

I may not be able to run the cluster on a public IP, but a full-fledged Load Balancer endpoint.

Port 80 will be exposed on the service, Prometheus metrics are exposed on /metrics

### Useful commands

`sudo docker build . | tail -n 1 | cut -d' ' -f3 | xargs sudo docker run -p 80:80` to build and run my containers for testing purposes

`sudo docker exec -it $(sudo docker container ls | tail -n 1 | awk ' { print $NF } ') /bin/bash` to log into my container`

`eksctl` is great to set up EKS :)

## Exercise 2

Deploy prometheus server (everything should be made with any configuration management mechanism) 
 
- Create a VM in any cloud provider of your choice. 
 
- Deploy a Prometheus server of any version to that VM 
 
- Configure Prometheus server to scrape metrics from your application 
 
### My approach

I will use ansible-galaxy to set up a Prometheus server, and then add some configuration of my own to make it scrape the metrics from my endpoint.
