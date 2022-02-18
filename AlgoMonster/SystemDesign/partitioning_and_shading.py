"""
Partitioning and Sharding

What is Partitioning?

Imagine your business is growing from 0 to millions of users, your database is filled up and 
you are running out of space quickly. What do you do? 
- make the machine and database bigger, aka vertical scaling
- slice the data into pieces and save into multiple databases and possibly multiple machines, 
aka horizontal scaling

In vertical scaling, you are limited by the memory and disk size of a single machine. And if
anything goes wrong with that machine, you are toast. That's why horizontal scaling is
often more desirable for large web applications.

We can partition a large database into smaller databases(shards) according to certain rules.
Naturally, there are two ways to partition the database. We can partition the data by row or by 
column into smaller databases.

Database without partition
ID      Name        Email       Date
1       alice   alice@gmail.com 20210101
2       bob     bob@gmail.com   20210101
3       eve     eve@gmail.com   20210101
4       ann     ann@gmail.com   20210101
5       jj      jj@gmail.com    20210101

Database with horizontal partition
ID      Name        Email       Date
1       alice   alice@gmail.com 20210101
2       bob     bob@gmail.com   20210101
3       eve     eve@gmail.com   20210101

ID      Name        Email       Date
4       ann     ann@gmail.com   20210101
5       jj      jj@gmail.com    20210101


Database with vertical partition

ID      Name       |         Email           Date
1       alice      |         alice@gmail.com 20210101
2       bob        |         bob@gmail.com   20210101
3       eve        |         eve@gmail.com   20210101
4       ann        |         ann@gmail.com   20210101
5       jj         |         jj@gmail.com    20210101

Database Sharding
- Horizontal database partition or sharding is the most commonly used partitioning method 
in SQL databases. Many modern databases have built-in sharding system.

A shard key is selected to decide which shard a data row should go into. Imagine  a sales
database, we can partition it by region, date or simply by hash of customer ids.

List partitioning               Range partitioning                  Hash Partitioning

East Sales Region               - January & February                - h1
- New York                      - March &  April                    - h2
- Virginia                      - May & June                        - h3
- Florida                       - July & August                     - h4

West Sales Region
- California
- Oregon
- Hawaii

Central Sales Region
- Illinois
- Texas
- Missouri


Sharding a SQL database - MySQL(MariaDB)

Suppose we have a comment system with a table of comments. We can partition the table by the
year the comment was created. This method is called RANGE Partitioning.

CREATE TABLE comments

  (

  comment_id INT NOT NULL,

  page_id INT NOT NULL,

  user_id INT NOT NULL,

  content TEXT NOT NULL,

  created_time DATETIME NOT NULL

  )

PARTITION BY RANGE (year(created_time))

  (

  PARTITION pold VALUES LESS THAN (2019),

  PARTITION p19 VALUES LESS THAN (2020),

  PARTITION p20 VALUES LESS THAN (2021),

  PARTITION p21 VALUES LESS THAN (2022),

  PARTITION p22 VALUES LESS THAN (2023)

  );

  Then, insert 2 comments, the first comment is from 2009 and the second comment is from 2021.

  INSERT INTO `comments` (

  `comment_id`, `page_id`, `user_id`,

  `content`, `created_time`

)

VALUES

  (

    '1', '1', '1',

    'The Times 03/Jan/2009 Chancellor on brink of second bailout for banks',

    '2009-01-03 18:15:05'

  ),

  (

    '2', '2', '2',

    'Hello algo.monster',

    '2021-10-11 18:45:02'

  )

  Use the following queries to check results:

  1. SELECT *FROM comments;
  2. SELECT *FROM comments PARTITION(pold);
  3. SELECT *FROM comments PARTITION(p21);

The first query should print all 2 comments. The second quer shows the comment from 2009, and
the third query shows the comment from 2021.  Try it here:  http://sqlfiddle.com/#!9/fccec/3

Sharding a NoSQL database -Redis Cluster
Redis is a key-value NoSQL database with builtin sharding support(tutorial: https://redis.io/topics/cluster-tutorial)
For scalability, Redis Cluster distribute data to nodes by the CRC16 of the key modulo 16384,
so each node is responsible for a subset of the hash slots.

For redundancy, Redis Cluster simply use replica nodes to store copies of the data  in the
master nodes as failovers.
Here are the bash commands for running a minimal cluster with three masters and three replicas
from the tutorial.

mkdir redis-cluster

cd redis-cluster

mkdir 7000 7001 7002 7003 7004 7005


# create redis config files

cat >> ./7000/redis.conf << EOF

port 7000

daemonize yes

cluster-enabled yes

cluster-config-file nodes.conf

cluster-node-timeout 5000

appendonly yes

EOF


cat >> ./7001/redis.conf << EOF

port 7001

daemonize yes

cluster-enabled yes

cluster-config-file nodes.conf

cluster-node-timeout 5000

appendonly yes

EOF


cat >> ./7002/redis.conf << EOF

port 7002

daemonize yes

cluster-enabled yes

cluster-config-file nodes.conf

cluster-node-timeout 5000

appendonly yes

EOF


cat >> ./7003/redis.conf << EOF

port 7003

daemonize yes

cluster-enabled yes

cluster-config-file nodes.conf

cluster-node-timeout 5000

appendonly yes

EOF


cat >> ./7004/redis.conf << EOF

port 7004

daemonize yes

cluster-enabled yes

cluster-config-file nodes.conf

cluster-node-timeout 5000

appendonly yes

EOF


cat >> ./7005/redis.conf << EOF

port 7005

daemonize yes

cluster-enabled yes

cluster-config-file nodes.conf

cluster-node-timeout 5000

appendonly yes

EOF


# start redis servers

cd 7000 && redis-server redis.conf && cd ..

cd 7001 && redis-server redis.conf && cd ..

cd 7002 && redis-server redis.conf && cd ..

cd 7003 && redis-server redis.conf && cd ..

cd 7004 && redis-server redis.conf && cd ..

cd 7005 && redis-server redis.conf && cd ..


# create redis cluster

redis-cli --cluster create 127.0.0.1:7000 127.0.0.1:7001 127.0.0.1:7002 127.0.0.1:7003 127.0.0.1:7004 127.0.0.1:7005 --cluster-replicas 1

You should see a message [OK] All 16384 slots covered after everything is done.

Then we can use redis-cli -c -p 7000 to connect to the first node of the cluster.

$ redis-cli -c -p 7000


$ redis-cli -c -p 7000

127.0.0.1:7000> set algo monster

OK

127.0.0.1:7000> set hello world

OK

127.0.0.1:7000> set foo bar

-> Redirected to slot [12182] located at 127.0.0.1:7002

OK

127.0.0.1:7002> set a a

OK

127.0.0.1:7002> set hello hello

-> Redirected to slot [866] located at 127.0.0.1:7000

OK

At first, both algo and hello fit in [0-5460], the hash slots of the node 7000. Then foo has hash 12182, which is covered by the node 7002, so we are redirected and the prompt is changed. When we set hello again, we are redirected back to the node 7000 because that's where the key hello is stored.

As the dataset grows, we might need to add new nodes to provide more storage. In this case, we need to reshard the cluster since we need to rearrange the hash slots.

"""