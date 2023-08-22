# file = open("kaki.txt", "w")
# try:
#     file.write("hello")
# finally:
#     file.close()
#
# with open("file.txt", "w") as file:
#     file.write("hello")


# class File:
# 	def __init__(self,filename, method):
# 		self.file =open(filename,method)
# 	def __enter__(self):
# 		print("Enter")
# 		return self.file
# 	def __exit__(self,type, value, traceback):
# 		print(f"{type}, {value},{traceback}")
# 		print("Exit")
# 		self.file.close()
# 		if type==Exception:
# 			return True
#
# with File("file.txt","w") as f:
# 	print("Middle")
# 	f.write("hello!")
# 	raise Exception()

print("##############################################################")
from contextlib import contextmanager

@contextmanager
def file(filename, method):
	print("enter")
	file =open(filename,method)
	yield file
	file.close()
	print("exit")

with file("text.txt", "w") as f:
	print("middle")
	f.write("hello")
 

"""
The contextlib module in Python provides several useful tools for managing resources and performing context-dependent operations. Here are some ways you might apply the @contextmanager decorator in your daily coding life:

    Working with files: The @contextmanager decorator can be used to simplify the management of file resources, such as opening, writing to, and closing files. This can be particularly useful when working with large or complex files, or when you want to ensure that files are properly closed even in the event of an exception.

    Working with database connections: The @contextmanager decorator can also be used to manage database connections, ensuring that connections are properly closed when they are no longer needed. This can be particularly useful when working with long-running processes that require persistent database connections.

    Setting up and tearing down test fixtures: The @contextmanager decorator can be used to set up and tear down test fixtures, such as creating and destroying temporary databases, files, or other resources. This can make it easier to write and maintain test code, and can help ensure that test environments are properly cleaned up after each test run.

    Working with network connections: The @contextmanager decorator can also be used to manage network connections, ensuring that connections are properly opened and closed, and that any associated resources (such as sockets or ports) are properly released when they are no longer needed.

Overall, the @contextmanager decorator can be a powerful tool for simplifying the management of resources in your code, and for ensuring that your code is more robust and less error-prone.
"""

print("################################ example ################################")

import psycopg2
from contextlib import contextmanager

@contextmanager
def get_db_connection():
    conn = psycopg2.connect(database="narok_county", user="postgres", password="postgres", host="localhost", port="5432")
    try:
        yield conn
    finally:
        conn.close()

# Example usage
with get_db_connection() as conn:
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM tenants_tenant")
        rows = cursor.fetchall()
        print(rows)