# messagebird-exercises

## Exercise 1

Write and deploy a web-server application in any language of your choice to kubernetes cluster 
running in any cloud provider of your choice. 
 
This Web app must show Homer Simpson picture when accessing /homersimpson and the time in the moment of request in Covilha City (Portugal) when accessing /covilha. 
 
- Run on a static-IP 
 
- Only the port 80 should be open 
 
* Application should have built-in prometheus exporter and provide two metrics: 
  * Total number of requests to /homersimpson uri 
  * Total number of requests to /covilha uri 

### My approach

I will use EKS as the Kubernetes solution because it is quicker for me to set up.

I am creating a Docker container to run the solution using Flask and Gunicorn to run a python application providing both metrics. This is based on https://github.com/tiangolo/meinheld-gunicorn-flask-docker .

I may not be able to run the cluster on a public IP, but a full-fledged Load Balancer endpoint.

Port 80 will be exposed on the service, Prometheus metrics are exposed on `/metrics` .

### Useful commands

`sudo docker build . | tail -n 1 | cut -d' ' -f3 | xargs sudo docker run -p 80:80` to build and run my containers for testing purposes

`sudo docker exec -it $(sudo docker container ls | tail -n 1 | awk ' { print $NF } ') /bin/bash` to log into my container

`eksctl` is great to set up EKS :)

## Exercise 2

Deploy prometheus server (everything should be made with any configuration management mechanism) 
 
- Create a VM in any cloud provider of your choice. 
 
- Deploy a Prometheus server of any version to that VM 
 
- Configure Prometheus server to scrape metrics from your application 
 
### My approach

I will use ansible-galaxy to set up a Prometheus server, and then add some configuration of my own to make it scrape the metrics from my endpoint.

Used https://github.com/William-Yeh/ansible-prometheus as a source.

## Some thoughts on the task

I believe the best approach to run this 'in real life' is to use a Prometheus pod on the EKS cluster to gain additional features, like service discovery. Service discovery, in this case, would collect metrics automatically based on pod labels, reducing the maintenance burden. As I am exposing only a Load Balancer endpoint, having more than one instance behind the LB would cause the metrics not to be reliable, as you will get to a different backend pod every time :/

Service Discovery can also be achieved by running a Prometheus EC2 instance within the VPC and Subnet the worker nodes are using, but additional permissions might be needed for such an instance, as API calls to the contorl plane require authentication which id done via the aws-iam-authenticator tool.

I used gunicorn+flask just to have a working environment that was Python-friendly.

Automation of the instance creation process could have been done via CloudFormation or Terraform in order to automate that step as well.
