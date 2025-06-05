# Prototype
- When it's easier to copy an existing object to fully initialize a new one.
- Complicated objects e.g. cars aren't designed from scratch
    - They reiterate existing designs
- An existing (partially or fully constructed) design is a prototype
- We make a copy(clone) the prototype and customize it
    - Requires 'deep copy' support
- We make the cloning process convenient via a Factory (Factories have a few predefined designs and you ask the factory to customize these designs giving you a custom item)
- In summary, a prototype is a partially or fully initialized object that you copy(clone) and make use of.
# Summary
- To implement a prototype, partially construct an object and store it somewhere
- Deep copy the prototype
- Customize the resulting instance
- A factory provides a convenient API for using prototypes