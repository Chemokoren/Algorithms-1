"""
Web Crawler

The internet is a huge graph with web pages being its nodes and hyperlinks being its edges. A
web crawler(spider) is a bo tthat traverses the internet graph.

Graph of the internet(https://algomonster.s3.us-east-2.amazonaws.com/system_design/2-A-graph-visualisation-of-the-topology-of-network-connections-of-the-core-of-the.png)

There are many purposes of a web crawler. For example, search engines like Google use web 
crawlers to create web indices. The web index created by the web crawler is typically an
inverted index, i.e, a mapping from content to document id. Imagine we have three documents.


    website1.com/a: "system design interview"
    website2.com/b: "algorithm interview"
    website3.com/c: "tech interview system"

The inverted index would look like this

{

  "system": ["website1.com/a", "website3.com/c"],

  "design": ["website1.com/a"],

  "interview": ["website1.com/a", "website2.com/b", "website3.com/c"],

  "algorithm": ["website2.com/a"],

  "tech": ["website3.com/a"],

}
It should be obvious an inverted index provides quick access to document ids that contain a
term. Now if a user searches for "system interview", we can find the intersection of the "
system" set and "interview" set.

The web crawler for search engines could be much more complex than our example. 
Google's paten on web crawler architecture(https://patents.google.com/patent/US20110307467A1/en)

For simplicity, we will develop a web crawler for mirroring website by downloading all html pages 
of the given website, with real demo code(https://github.com/realAlgoMonster/system-design/tree/main/web-crawler)

Back of the envelop calculations

Let's do some estimation and calculation. Suppose we want to fetch 1 billion HTML document per
year on average, then we have 1000/365=3 million new files per day and 3000000/86400=35 per
second.

According to the HTTP Archive, the average size of HTML documents is 30KB, then we can store 
about 35 thousand links in 1GB storage. Hence we need about 30TB storage per year.

Service
At a high level a web crawler has to:
- Download a page
- Create and update the index(if the goal is to index and rank pages) or write the page to 
filesystem(if the goal is to mirror a site)
-Extract links and check duplicates
-visit pages linked from the current page

DFS vs BFS

Since the problem we are trying to solve is essentially graph traversal, it's natural to ask 
whether to use DFS or BFS.  If the internet were static and we have no time requirement, both
algorithm have the same complexity. In reality, if the resource is limited and we are trying
to crawl as many websites as possible, then we would crawl only the most important pages.
In most case, this is the home page of each website. Under these constrains, BFS would be 
superior to DFS.

Does that mean DFS is not used? Not really. To crawl a website, the crawler has to establish
a TCP connection which requires expensive setups such as the three handshakes. It's a bit of
a waste to only visit the home page in one connection. In this case, it's more efficient to
visit all the pages of a website in one TCP connection, which is essentially DFS.

In reality, all websites are not created equal, the order of crawling is managed by a scheduler.
A scheduler store the URLs to be crawled in a Priority Queue. Overall, a web crawling process
is more of BFS than DFS.

Now that we have clarified the problem and explored the potential solutions, we can propose a 
high-level design:
Web crawler design(https://kroki.io/mermaid/svg/eNotjcsKwjAQRfd-xSzbf1ChD8VFBbV1FbIYk9GElqbkYRXy8bbB3T1wD-c5mFkotH4DULAOXQ_XQIH4wiWrzTwOBiVZDrvdPp66cwMPI78RKtbosYfDx1sU3thVKNLpYqYI5YIVbFeuFIkeZJgGLdCTi1Cz7KhH7RRJuN8al_P0TnJwKkKx1hO3-KYI7RLAF7HsP3L-A5t9O1s=)
Let's look at each components:

Downloader

Downloader is the worker(s) that take a url and downloads the HTML file and saves it into 
storage and also sends the HTML body to Link Extractor to extract the links in the HTML.
It pops tasks(which contains the url to be fetched) from the task queue.

Task Queue
Task Queue is a message queue of urls to crawl. Our workers(Downloader) fetch the message from 
the task  queue.

Link Extractor
Link Extractor extracts links(anchor tags) and pushes them into the Task Queue if the url 
hasn't been crawled yet.

Finished URLs
This is the algorithm equivalent of a hashset that stores all the URLs that have been crawled.

Storage
From our calculations, we need about 30TB storage per year, so the local file system is probably
not enough. For such large projects, we can use distributed file storage like HDFS, or tools 
like Rclone to mount cloud storage like AWS S3 onto the file system and have the downloader
write directly into them.

Sample Implementation

"Talk is cheap. Show me the code. - Linus Torvalds"

To help you understand the idea better, we show a sample implementation of mirroring a website.
We will download the entire website of http://quotes.toscrape.com/ and save it in our local file
system.

web crawler design redis scrapy

It's very common to use Python for web crawlers, and Scrapy(https://scrapy.org/) is a 
very popular web crawling framework with high quality documentation(https://docs.scrapy.org/) 
and tutorial(https://docs.scrapy.org/en/latest/intro/tutorial.html). Scrapy is powerful and 
extensible, it can handle robots.txt for you.

For the queue design, we can use a in-memory data structure since the items in the queue are 
just transient work items and do not need to be persisted. We will use Redi's list data type.
(https://redis.com/ebook/part-2-core-concepts/chapter-6-application-components-in-redis/6-4-task-queues/6-4-1-first-in-first-out-queues/)
Alternatively, you can use Kafka or RabbitMQ. However, we don't need data persistence and our 
model is very simple, so Redis is our choice.

Redis also doubles as a distributed hashset to store finished links here.

Here is the code of our spider.

# spider.py

import scrapy

from urllib.parse import urlparse

from scrapy.linkextractors import LinkExtractor

import redis

import os

import time

from pathlib import Path


class QuotesSpider(scrapy.Spider):

    name = "quotes"

    le = LinkExtractor()

    r = redis.Redis(host='localhost', port=6379, db=0)

    path = 'data'

    hostname = ''


    def start_requests(self):

        # init task queue with a URL

        self.r.rpush('task_queue', 'http://quotes.toscrape.com/page/1/')


        while True:

            item = self.r.lpop('task_queue')

            if item is None:

                time.sleep(1)

                item = self.r.lpop('task_queue')

                if item is None:

                    break

            url = item.decode("utf-8")

            if self.hostname == '':

                self.hostname = urlparse(url).hostname

            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):

        filepath = urlparse(response.url).path

        if filepath[-1] == '/':

            filepath += 'index.html'

        path = self.path + filepath

        Path(os.path.dirname(path)).mkdir(parents=True, exist_ok=True)

        with open(path, 'wb') as f:

            f.write(response.body)


        self.r.sadd('task_finished', response.url)


        for link in self.le.extract_links(response):

            url = link.url

            if urlparse(url).hostname != self.hostname:

                break

            if self.r.sismember('task_finished', url):

                break

            self.r.rpush('task_queue', url)

The web crawler continuously pop urls from the front of the task queue, which is a redis list.
After writing the HTML document to the file ssytem, the crawler adds the url to the set of 
finished  urls, extract the urls in the current HTML document and check if a url is already 
finished. If not, then the crawler pushes the url to the end of the task queue.
(https://github.com/realAlgoMonster/system-design/tree/main/web-crawler)

# install python dependency

pip install scrapy redis


# run redis from docker

docker run --name web-crawler-redis -p 6379:6379 -d redis


# start crawling

scrapy runspider spider.py


This spider can crawl([quotes.toscrape.com](http://quotes.toscrape.com))  in one second
and the entire website has been crawled into data folder. web crawler scrape the quotes results.





"""