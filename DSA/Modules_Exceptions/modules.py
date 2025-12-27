"""
Pythons built-in modules

- Math
- Random
- Time
- Threading

** List all members of the module
- import module-name
- dir(module-name)
"""
import math
print(dir(math))
l = dir(math)

for i in l:
    print(i)

"""
- dunder methods are pre-defined methods and are also private which cannot be used by the programmer
** How to import module names
import math -- all the definitions & functions and statements are available in the main program
- In this way of importing, all the identifiers must be fully qualified when accessed to avoid name clashes e.g.
print(math.pi, math.e, math.pow(2,3))
print(pi) - returns an error indicating that members must be fully qualified with the module name

Aliases for Module name

import math as m
print(m.pi, m.e, m.pow(2,3))

- once we use an alias, we cannot use the module name e.g.
print(math.pi)  --returns a NameError

from math import sqrt, pi, pow
- in this approach there's no need to use namespace qualifiers
print(pi, pow(2,3), sqrt(2))

Instead of specifying every member of the module, we use the *
from math import  *
print(sqrt(25))

Aliases: from math import sqrt as s, pow as p


Creating our own Modules

Advantages of Modules
- Allows large programs to be broken into manageable size
- Effective software development process
- Eventually integrated into complex complete system
- Facilitates program modification and updation

by convention, module names are in lowecase

"""
