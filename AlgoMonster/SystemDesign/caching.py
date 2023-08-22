"""
What is caching?

A cache is a generic term commonly referring to a high-speed data storage layer which stores a 
subset of underlying data(the data to be "cached") to efficiently reuse previously retrieved
or computed data. Depending on the context, caching can be different things.
For example, modern CPUs typically have 3 layers of cache called L1, L2, and L3 to speedup 
accessing data in memory. Operating system also use free memory as cache for local file system

In system design, caching normally means database caching and sometimes web caching.(https://aws.amazon.com/caching/)

Database Caching
----------------
Database caching, such as Memcached and Redis are mainly to reduce the frequency of database
reads. Especially in the past when databases are stored on hard drive disks, random reading is 
slow and SSD or in-memory caching is very important.

Reading Cache
-cache-aside is the most common and simple way to use database cache. The web server will try
to read data from cache. If data does not exist in cache, the server will fetch data from the
database and save data to cache. But this method cannot handle data updates.
(https://kroki.io/mermaid/svg/eNpLy8kvT85ILCpR8AniCk4tKkst0tW1qzHUUygpqlQoyVcoSk1MqXFOTM5IRZI20lPITFPIyy9RSMsvzUvRAatSSCvKz1VISapxSSxJTEosTo3WgLE0Y5E0G-spFCeWpYIMTwaZCzEdAKsnLxk=)

-Read-Through - cache sits between the application and the database. The application does not
interact with database directly. When there is a cache miss, cache fetches with the database
itself. A real-world example of a Read-Through cache is Amazon's DynamoDB Accelerator(DAX)(https://aws.amazon.com/dynamodb/dax/)
(https://kroki.io/mermaid/svg/eNpLy8kvT85ILCpR8AniCk4tKkst0tW1qzHUUyhKTUypcU5MzkjlApM2IHEjPYXMNIW8_BKFtPzSvBQdsCqFtKL8XIWUJIXEvBSF4sSy1BqXxJLEpMTi1GgNGEszFgB4hCQm)

Updating Cache
-Write-Through is a method that keeps data consistently between the cache and the database.
Then for any data updates, the server updates the data in cache and database synchronously.
This method keeps data consistency but may sacrifice writing performance.
Write-Back - is similar to Write-Through, but updates the data in cache and database 
asynchronously to improve write performance. However, there might be data loss when the server
craches before the writing to database is done.

Redis/SQLite Demo
We will use a Flask app with SQLite as database and Redis as cache for this example. This is
a Cache-aside demo and does not involve any writing.

First, let's generate some random data.

# init.py

import sqlite3

import random


con = sqlite3.connect('data.db')

cur = con.cursor()

size = 1000000


# Create table

cur.execute('''CREATE TABLE comments

              (domain text, page int, content text)''')


# Insert data

for i in range(size):

    cur.execute("insert into comments values (?, ?, ?)", ("algo.monster",

                random.randint(0, size // 10), f'Comment number {i}'))


con.commit()

con.close()

Then write a flask server to query and return the data directly from SQLite.

# server.py

from datetime import time

from flask import Flask, Response

import time

import sqlite3


app = Flask('cache')


con = sqlite3.connect('data.db', check_same_thread=False)


@app.route('/')

def hello_world():

    return 'Hello!\n'


@app.route('/<id>')

def page(id):

    content = f'Comments from page {id}:\n'

    start = time.time()


    cur = con.cursor()

    cur.execute("select * from comments where page=?", (id,))

    comments = cur.fetchall()

    for comment in comments:

        content += comment[2] + '\n'


    cost = time.time() - start

    content += f'Time cost: {cost}\n'

    return Response(content, mimetype='text/plain')


if __name__ == '__main__':

    app.run(host='127.0.0.1', port=5000)

Without cache, the flask web server would query SQLite database every request, which takes about 
0.06 seconds for now. This is not very slow, but not ideal if our dataset will grow later.


Now, let's add Redis to save the queries from SQLite in the cache, and indicate whether we 
hit the cache in the response.

# server.py

from datetime import time

import json

from flask import Flask, Response

import time

import sqlite3

import redis


app = Flask('cache')


r = redis.Redis(host='localhost', port=6379, db=0)

con = sqlite3.connect('data.db', check_same_thread=False)


@app.route('/')

def hello_world():

    return 'Hello!\n'


@app.route('/<id>')

def page(id):

    content = f'Comments from page {id}:\n'

    start = time.time()

    comments = []


    if r.exists(id):

        content += 'Cache: hit\n'

        comments = json.loads(r.get(id))

    else:

        content += 'Cache: miss\n'

        cur = con.cursor()

        cur.execute("select * from comments where page=?", (id,))

        comments = cur.fetchall()

        r.set(id, json.dumps(comments))


    for comment in comments:

        content += comment[2] + '\n'


    cost = time.time() - start

    content += f'Time cost: {cost}\n'

    return Response(content, mimetype='text/plain')


if __name__ == '__main__':

    app.run(host='127.0.0.1', port=5000)

The response of the first request still takes about 0.06 second since our cache is empty at
the beginning.

For future requests, the flask server will use Redis directly without accessing the SQLite 
server, and it only takes about 0.001 second, which is a huge improvement on performance. (
    Reading from memory is much faster than reading from Disk)

HTTP Caching - Content Delivery Network (CDN)
-For websites and applications, many resources like JavaScript files and CSS files are static 
and can be reused, so HTTP caching can improve web performance

There are 2 kinds of HTTP cahces
-A shared cache, indicated by header Cache-Control: public, is the cache used by CDN and can be
used by more than one user.
-A private cache, indicated by header Cache-Control: private, is the cache used by user's 
browser that can be used by only one user.
(https://algomonster.s3.us-east-2.amazonaws.com/system_design/http_cache_type.png)
(https://developer.mozilla.org/en-US/docs/Web/HTTP/Caching)

"""