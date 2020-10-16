# file = open("kaki.txt", "w")
# try:
#     file.write("hello")
# finally:
#     file.close()

# with open("file.txt", "r") as file:
#     file.write("hello")


class File:
	def __init__(self,filename, method):
		self.file =open(filename,method)
	def __enter__(self):
		print("Enter")
		return self.file
	def __exit__(self,type, value, traceback):
		print(f"{type}, {value},{traceback}")
		print("Exit")
		self.file.close()
		if type==Exception:
			return True
		# return True;

with File("file.txt","w") as f:
	print("Middle")
	f.write("hello!")
	raise Exception()

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