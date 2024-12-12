class College:

    def __init__(self):
        print('Outer Class Constructor')

    class Student:
        def __init__(self):
            print('Inner Class Constructor')
        def displayS(self):
            print('Student Method Display')
    def displayC(self):
        print('College Method Display')
C= College()
C.displayC()
S= C.Student() # or College().Student() - instantiating inner class
S.displayS()
