# import modules
import heapq as hq

# list of students
list_stu = [(5,'Rina'),(1,'Anish'),(3,'Moana'),(2,'cathy'),(4,'Lucy'),(6,'Kibet'),(7,'Ann')]

# Arrange based on the roll number
hq.heapify(list_stu)

print("The order of presentation is :")

for i in list_stu:
    print(i[0],':',i[1])

