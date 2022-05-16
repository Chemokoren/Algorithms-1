"""
1) Coding. The candidate has to write some simple code, with correct syntax, in C, C++, or Java.

2) OO design. The candidate has to define basic OO concepts, and come up with classes to model a simple 
problem.

3) Scripting and regexes. The candidate has to describe how to find the phone numbers in 50,000 HTML pages.

4) Data structures. The candidate has to demonstrate basic knowledge of the most common data structures.
5) Bits and bytes. The candidate has to answer simple questions about bits, bytes, and binary numbers.


Area Number One: Coding
-----------------------

The candidate has to write some code. Give them a coding problem that requires writing a short, 
straightforward function. They can write it in whatever language they like, as long as they don't just call
a library function that does it for them.

It should be a trivial problem, one that even a slow candidate can answer in 5 minutes or less.


Example: Format an RGB value (three 1-byte numbers) as a 6-digit hexadecimal string.

def rgb_to_hex(rgb):
    return '%02x%02x%02x' % rgb
rgb_to_hex((255, 255, 195))


*  distributed computing

Area Number Two: Object-Oriented Programming

We shouldn't hire SDEs (arguably excepting college hires) who aren't at least somewhat proficient with OOP.
I'm not claiming that OOP is good or bad; I'm just saying you have to know it, just like you have to know 
the things you can and can't do at an airport security checkpoint.

Two reasons:

1) OO has been popular/mainstream for more than 20 years. Virtually every programming language supports OOP 
in some way. You can't work on a big code base without running into it.

2) OO concepts are an important building block for creating good service interfaces. They represent a shared 
understanding and a common vocabulary that are sometimes useful when talking about architecture.

a) Terminology

The candidate should be able to give satisfactory definitions for a random selection of the following terms:

        class, object (and the difference between the two)

        instantiation

        method (as opposed to, say, a C function)

        virtual method, pure virtual method

        class/static method

        static/class initializer

        constructor

        destructor/finalizer

        superclass or base class

        subclass or derived class

        inheritance

        encapsulation

        multiple inheritance (and give an example)

        delegation/forwarding

        composition/aggregation

        abstract class

        interface/protocol (and different from abstract class)

        method overriding

        method overloading (and difference from overriding)

        polymorphism (without resorting to examples)

        is-a versus has-a relationships (with examples)

        method signatures (what's included in one)

        method visibility (e.g. public/private/other)

b) OO Design

This is where most candidates fail with OO. They can recite the textbook definitions, and then go on 
to produce certifiably insane class designs for simple problems.

For the OO-design weeder question, have them describe:

        What classes they would define.

        What methods go in each class (including signatures).

        What the class constructors are responsible for.

        What data structures the class will have to maintain.

        Whether any Design Patterns are applicable to this problem.


Here are some examples:

        Design a deck of cards that can be used for different card game applications.

            Likely classes: a Deck, a Card, a Hand, a Board, and possibly Rank and Suit. Drill down on who's 
            responsible for creating new Decks, where they get shuffled, how you deal cards, etc. Do you need 
            a different instance for every card in a casino in Vegas?

        Model the Animal kingdom as a class system, for use in a Virtual Zoo program.

            Possible sub-issues: do they know the animal kingdom at all? (I.e. common sense.) What properties 
            and methods do they immediately think are the most important? Do they use abstract classes and/or
            interfaces to represent shared stuff? How do they handle the multiple-inheritance problem posed 
            by, say, a tomato (fruit or veggie?), a sponge (animal or plant?), or a mule (donkey or horse?)

        Create a class design to represent a filesystem.

            Do they even know what a filesystem is, and what services it provides? Likely classes: Filesystem,
            Directory, File, Permission. What's their relationship? How do you differentiate between text 
            and binary files, or do you need to? What about executable files? How do they model a Directory
            containing many files? Do they use a data structure for it? Which one, and what performance 
            tradeoffs does it have?


        Design an OO representation to model HTML.

            How do they represent tags and content? What about containment relationships? Bonus points if they know that this has already been done a bunch of times, e.g. with DOM. But they still have to describe it.

The following commonly-asked OO design interview questions are probably too involved to be good phone-screen 
weeders:

        Design a parking garage.

        Design a bank of elevators in a skyscraper.

        Model the monorail system at Disney World.

        Design a restaurant-reservation system.

        Design a hotel room-reservation system.

A good OO design question can test coding, design, domain knowledge, OO principles, and so on. A good weeder
question should probably just target whether they know when to use subtypes, attributes, and containment.

Area Number Three: Scripting and Regular Expressions

grep -l -R --perl-regexp "\b(\(\d{3}\)\s*|\d{3}-)\d{3}-\d{4}\b" * > output.txt


Let's say you're on my team, and I've decided I'm a real stickler for code formatting. But I've got peculiar 
tastes, and one day I decide I want to have all parentheses stand out very clearly in your code.

So let's say you've got a set of source files in C, C++, or Java. Your choice. And I want you to modify them 
so that in each source file, every open- and close-paren has exactly one space character before and after it. 
If there is any other whitespace around the paren, it's collapsed into a single space character.

For instance, this code:

foo (bar ( new Point(x, graph.getY()) ));

Would be modified to look like this:

foo ( bar ( new Point ( x, graph.getY ( ) ) ) ) ;

Area Number Four: Data Structures
---------------------------------

demonstrate a basic understanding of the most common data structures, and of the fundamentals of "big-O" 
algorithmic complexity analysis.

algorithms usually fall into the following performance classes: constant-time, logarithmic, linear, 
polynomial, exponential, and factorial.

1) arrays - I'm talking about C-language and Java-language arrays: fixed-sized, indexed, contiguous structures
 whose elements are all of the same type, and whose elements can be accessed in constant time given their
  indices.

2) vectors - also known as "growable arrays" or ArrayLists. Need to know that they're objects that are 
backed by a fixed-size array, and that they resize themselves as necessary.

3) linked lists - lists made of nodes that contain a data item and a pointer/reference to the next 
(and possibly previous) node.

4) hashtables - amortized constant-time access data structures that map keys to values, and are backed by a 
real array in memory, with some form of collision handling for values that hash to the same location.

5) trees - data structures that consist of nodes with optional data elements and one or more child 
pointers/references, and possibly parent pointers, representing a heirarchical or ordered set of data elements.

6) graphs - data structures that represent arbitrary relationships between members of any data set, 
represented as networks of nodes and edges.

Candidates should be able to describe, for any of the data structures above:

        what you use them for (real-life examples)

        why you prefer them for those examples

        the operations they typically provide (e.g. insert, delete, find)

        the big-O performance of those operations (e.g. logarithmic, exponential)

        how you traverse them to visit all their elements, and what order they're visited in

        at least one typical implementation for the data structure

Stack, Map, List or Set, and a concrete data structure such as a singly-linked list or a hash table. 
For a given abstract data type (e.g. a Queue), they should be able to suggest at least two possible concrete 
implementations, and explain the performance trade-offs between the two implementations.

Example weeder questions:

1) What are some really common data structures, e.g. in java.util?

2) When would you use a linked list vs. a vector?

3) Can you implement a Map with a tree? What about with a list?

4) How do you print out the nodes of a tree in level-order (i.e. first level, then 2nd level, then 3rd level, etc.)

5) What's the worst-case insertion performance of a hashtable? Of a binary tree?

6) What are some options for implementing a priority queue?


Area Number Five: Bits and Bytes
--------------------------------

This area is fairly contentious, at least inasmuch as people who don't know this area claim you don't need 
to know it.

Candidates do need to know about bits and bytes, at least at the level that I'm outlining here. Otherwise 
they're prone to having an integer-overflow error in their code that brings the website down and costs us
 millions. Or spending a week trying to decode a serialized object they're debugging. 
 Computers don't have ten fingers; they have one.

Candidates should know what bits and bytes are. They should be able to count in binary; e.g. they should be 
able to tell you what 2^5 or 2^10 is, in decimal. They shouldn't stare blankly at you when you ask with 2^16 
is. It's a special number. They should know it.

They should know at least the logical operations AND, OR, NOT, and XOR, and how to express them in their 
favorite/strongest programming language.

They should understand the difference between a bitwise-AND and a logical-AND; similarly for the other
 operations.

Candidates should know the probable sizes of the primitive data types for a standard 32-bit (e.g. Intel) 
architecture.

Everyone should know the difference between signed and unsigned types, what it does to the range of 
representable values for that type, and whether their language supports signed vs. unsigned types.

Candidates should know the bitwise and logical operators for their language, and should be able to use them
 for simple things like setting or testing a specific bit, or set of bits.

Candidates should know about the bit-shift operators in their language, and should know why you would want to 
use them.

A good weeder question for this area is:

Tell me how to test whether the high-order bit is set in a byte.

Another, more involved one is:

Write a function to count all the bits in an int value; e.g. the function with the signature 
int countBits(int x)

Another good one is:

Describe a function that takes an int value, and returns true if the bit pattern of that int value is the 
same if you reverse it (i.e. it's a palindrome); i.e. boolean isPalindrome(int x)

All programmers should be able to count in hexadecimal, and should be able to convert between the binary, octal, and hex 
representations of a number.


"""