"""
URL Shortener | TinyURL

Use Case
URL shorterners are widely used on the Internet. One of the most popular services is TinyURL.
It can generate a short URL that redirects to a given site. And when you post a link on Twitter
it will automatically generate a short URL.

Redirections(https://developer.mozilla.org/en-US/docs/Web/HTTP/Redirections)

We will design a scalable URL shortining service with real demo code(https://github.com/realAlgoMonster/system-design/tree/main/tiny-url-shortener).

API
For simplicity, our demo will not have user authentication and all requests are made 
anonymously. 
- GET /<short> 302 redirects to the long URL if the short id is valid, otherwise return 404
not found.
- POST /api/link request:longURL is the long URL to be shortened. response: short is the short
id encoded in Base58. tinyurl is the shortened URL. Both the request and response are in JSON.

In practice, we often need to support additional fields like custom_alias and expiry_date.

Back of the Envelope Calculation
--------------------------------
Lets do some estimation and calculation. Suppose we have 1 million DAU(Daily Active User) and
each user make 3 shortening requests per day. Then there are 3 million new links per day and 
about 1 billion per year. We have 1000000/86400=12 requests per second on average. Suppose 
the peak traffic is 5 times of the average, our system should be able to handle 60 shortening
requests per second at peak. Suppose the read to write ratio is 10:1, we need to handle 600
redirection requests at peak.

we also need to determine the length of the short id, which should be as short as possible. 
Assume we have an alphabet of 58 characters(reason in the implementation section) for the 
short id, here is a table about the number of distinct short id of the given length.

Length	    Number of distinct short ID
1	        58^1 = 58
2	        58^2 = 3,364
3	        58^3 = 195,112
4	        58^4 = 11,316,496
5	        58^5 = 656,356,768
6	        58^6 = 38,068,692,544
7	        58^7 = 2,207,984,167,552

As from this table, there are 38 billion distinct short IDs of length 6 in Base58 and 2 trillion
of length 7. Although length 6 is enough for more than 30 years, we will use length 7 in our demo
to avoid possible collisions.

As for storage, assume each long URL is 100 bytes on average, then we can store 10 million 
links in 1 GB storage. Hence we need about 100GB storage per year.

Service
Our example is very simple so there is only one service that serves the two API endpoint. In 
practice, we also need a user service to handle authentication.

Storage
Our data model for now is very simple and there is not complex relationship. We just need a map 
from short id to long URL, and we have much more reads than writes.So a key-value NoSQL database
is most suitable in this case - Redis. 
Redis is widely used as key-value cache, but it's also a distributed key-value database with 
on-disk persistence with Redis cluster.
Redis is easy to use in python with redis-py and easy to deploy with docker for early 
development.

To minimize the chance of data loss, we need to use AOF Redis.(Redis Persistence-https://redis.io/topics/persistence)
Redis is not perfect. Uins Redis as a database sacrifices write performance to achieve
persistence. Moreover, we must have enough memory to store all the data, so we might run out
of memory as the service get more popular. But from our calculation, we can store about 10m
links in 1GB memory, and we can split the dataset among multiple nodes with the Redis cluster, 
so memory is not a big problem(at least in the first year). 
Even if we use other distributed key-value databases, it's very common to use Redis as a cache 
layer.

Detailed Implementation

Short code
For each shortening request with a long URL, we need to assign a short code and store the pair
in our database then redirects <BaseURL>/<short> to the long URL. There are various ways to
generate the short code. Using an auto increment id is the easiest, but people can gues the id 
of other links, which is insecure if we want to keep the long URL confidential to only people 
who know the short link.

We can also calculate the hash of the long URL and use truncate the hash as short id, but then
if two users shorten the same long URL, the short id will be the same, which is not ideal if
we want to add analytics in the future. We can solve this problem by adding a counter or random
salt to the end of the long URL before hashing. 

Another approach that prevents these problems is to randomly generate a short id. We can use
integer for id in our database and encode it to a short id in the short URL.

Encoding and Decoding
Base64 is commonly used to present binary data in URLs. We can use Base58 in our case which 
removed 0OIl+/ from the alphabet to avoid visually identical looking. It's very easy to 
implement Base58 in Python.

# utils.py

class Base:

    alphabet: str

    size: int

    decode_map: dict


    def __init__(self, alphabet: str):

        self.alphabet = alphabet

        self.size = len(alphabet)

        self.decode_map = dict()

        for i in range(self.size):

            self.decode_map[alphabet[i]] = i


    def encode_int(self, i: int) -> str:

        out = ''

        while i:

            i, idx = divmod(i, self.size)

            out = self.alphabet[idx] + out

        return out


    def decode_int(self, data: bytes) -> int:

        i = 0

        for char in data:

            i = i * self.size + self.decode_map[char]

        return i


BASE58 = Base('123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz')


Data

# models.py

import redis

import random

import json

from types import SimpleNamespace


BASE = 58

LENGTH = 7


r = redis.Redis(host='localhost', port=6379, db=0)


class Link:

    id: int

    longURL: str


    def __init__(self, longURL: str):

        self.longURL = longURL


    @classmethod

    def from_redis(cls, id: int):

        data = r.get(id)

        if not data:

            return None

        cls = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))

        return cls


    def insert(self):

        while True:

            id = random.randrange(0, 58 ** 7)

            if not r.exists(id):

                self.id = id

                r.set(id, json.dumps(self.__dict__))

                break


Web server
# __init__.py

from flask import Flask, request, redirect, abort


from .models import Link

from .utils import BASE58


app = Flask(__name__)

BASE_URL = 'http://localhost:5000/'


@app.route("/api/link", methods=["POST"])

def new_link():

    data = request.get_json()

    link = Link(data["longURL"])

    link.insert()

    short = BASE58.encode_int(link.id)

    data = {

        'short': short,

        'tinyurl': BASE_URL + short

    }

    return {

        'status': 'success',

        'data': data

    }


@app.route("/<short>", methods=["GET"])

def redirect_link(short):

    id = 0

    try:

        id = BASE58.decode_int(short)

    except KeyError:

        abort(404)

    link = Link.from_redis(id)

    if not link:

        abort(404)

    return redirect(link.longURL, code=302)

For Redis, you can use cloud services like AWS, install on your machine or use docker

# install python dependency

pip install flask redis


# run redis from docker

docker run --name tiny-url-shortener-redis -p 6379:6379 -d redis


# start web server

FLASK_APP=. flask run

clone: https://github.com/realAlgoMonster/system-design/tree/main/tiny-url-shortener

Example

Once the web server is started, we can use cURL to send a shortened request by 
curl --header "Content-Type: application/json" --request POST --data '{"longURL":"YOUR_LONG_URL"}' http://localhost:5000/api/link

and a successful response looks like
{"data":{"short":"tuBQHmi","tinyurl":"http://localhost:5000/tuBQHmi"},"status":"success"}

Then you can use  [http://localhost:5000/tuBQHmi](http://localhost:5000/tuBQHmi) to access the your long URL.

Scalability
-----------
Our web server is stateless. They simply process requests, read from the database and send the
results back. There is no data persisted on the web servers. We can easily scale stateless
web servers by adding more servers and putting them behind a load balancer.

For storage, we can scale Redis by using Redis Clusters, essentially splitting data into many
redis instances as explained in the storage section above.
"""