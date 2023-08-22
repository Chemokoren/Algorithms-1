"""
Load Balancer Demo with Nginx

Illustrates how load balancer works and why we need load balancing. We will use an Nginx load 
balancer to distribute traffic to three web servers.You need Nginx and Flask installed.

The flask web server returns Hello {port nunber}! as response



# demo.py

from flask import Flask

import sys


app = Flask('demo')

port = 8000


@app.route('/')

def hello_world():

    return f'Hello, {port}!\n'


if __name__ == '__main__':

    port = sys.argv[1]

    app.run(host='127.0.0.1', port=port)


Now we can start 3 server instances.
1. python demo.py 8001
2. python demo.py 8002
3. python demo.py 8003

Next we configure Nginx as a load balancer to distribute traffic to the three web servers.We 
create a new config file /etc/nginx/conf.d/demo.conf

upstream demo {

    server localhost:8001;

    server localhost:8002;

    server localhost:8003;

}


server {

    listen 8080;


    location / {

      proxy_pass http://demo;

    }

}

Use systemctl to restart nginx (sudo systemctl restart nginx)

Now, you should be able to access http://localhost:8080/. The default load balancing method 
here is round-robin, thus the response from the load balancer will be Hello, 8001!, 
Hello, 8002! and Hello, 8003! in order.

Load Balancer and High Availability
To emulate servers going offline, we stop the web server that run on 8002 and 8003 and visit our load balancer at http://localhost:8080/ . It should be still accessible and always returns Hello, 8001!, the message returned by the first server. This is why load balancer and high availability - two web servers are down and we are still serving requests from the remaining one without the user noticing any downtime. We can scale a service by adding more web servers and put them behind load balancers.

Demo: https://www.youtube.com/watch?v=NwZnx1NHxgE
https://www.nginx.com/resources/glossary/load-balancing/

"""