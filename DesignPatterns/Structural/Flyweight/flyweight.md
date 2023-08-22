"""
Flyweight Design Pattern
------------------------

- A space optimization technique that lets us use less memory by storing externally
the data associated with similar objects.

Aim
- Avoid redundancy when storing data

Example 1: MMORPG
- Plenty of users with identical first/last names
- No sense in storing same first/last name over and over again
- Store a list of names and references to them

Example 2: bold or italic text formatting
- Don't want each character to have a formatting character
- Operate on ranges(e.g., line number, start/end positions)
and saying this range is going to be bold, and this other italic and when
the text overlaps then you have a bunch of text in the middle that's bold and italic

Summary
-------
- Store common data externally
- Specify an index or a reference into the external data store
- Define the idea of 'ranges' on homogenous collections and store data related
to those ranges
"""