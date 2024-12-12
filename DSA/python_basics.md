# Keywords or Reserved Words
- Keywords are reserved words in Python
- Have a predefined meaning in any programming language
- They define syntax and structure in Python Language
- They cannot define any identifier such as variable name, function name or class name

# Comments
- If encountered python will ignore the comment
- No multiline comments in Python
- To comment multiple line, each line has to be commented individually using hash.
- Triple quoted Strings are provided in Python, but it's used as documentation string not as a comment

# None Data Type
- None in Python means no value is associated
- None is also an object in Python
y =10
y =print(x)
print(y)

# Control Statements
- Sequential
- Selection (if, if-else, elif)
- Iterative (while, for)

# test with break 
n =int(input('Enter Value:'))
print('Number from 1 to ', n)

i = 1
while i <= n:
    print(i)
    i +=1

print('End of Program')


print('--- continue statement ---')
l = [10, 54, 2, 61, 15]
for i in l:
    if i % 2 !=0:
        continue
    print(i)

