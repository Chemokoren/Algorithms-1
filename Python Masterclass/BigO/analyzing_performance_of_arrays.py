"""
Objectives
-Understand how objects and arrays work, through the lens of Big O
-Explain why adding elements to the beginning of an array is costly
-Compare and contrast the runtime for arrays and objects as well as built-in methods

Objects (dictionaries)
-unordered, key value pairs!

instructor = {
"firstName": "Kelly",
"isInstructor": True,
"favoriteNumbers":[1,2,3,4]
}

When to use objects 
- when you don't need order
- When you need fast access / insertion and removal

Big O of objects
- insertion -O(1)
- Removal -  O(1)
- Searching  O(N)
- Access     O(1)

instructor.keys() -O(N)
instructor.values() - O(N)
instructor.items() -O(N)
instructor.get("firstName")- O(1)
instructor.__contains__("firstName") -O(1)



Arrays!
-------

- Ordered lists
names =["michael", "Melissa", "Andres"]
values =[True, {}, [], 2, "awesome"]

When to use Arrays
- When you need order
- When you need fast access/insertion and removal

Big O of Arrays
- Insertion - it depends ...
- Removal - It depends ...
- Searching - O(N)
- Access - O(1)

Insertion and removal from the end is constant time and is easier than from the beginning

Big O of Array Operations
-push       -O(1)
-pop        -O(1)
-shift      -O(N)
-unshift    -O(N)
-concat     -O(N)
-slice      -O(N)
-splice     -O(N)
-sort       -O(N*logN)
- foreach/map/filter/reduce -O(N)

"""
