"""
Composite Design Pattern
-The goal is to treat indivial components and groups of objects in a uniform version so as
to provide an identity interface over both aggregates of components or individual components
(Treating individual and aggregate objects uniformly).

Motivation
- Objects use other object's properties/members through inheritance and composition
- Composition lets us make compound objects
    - e.g. a mathematical expression composed of simple expressions; or 
    - A grouping of shapes that consists of several shapes
- Composite design pattern is used to treat both single(scalar) and composite objects
uniformly.
    - i.e.,Foo and Sequence(yielding Foo's) have common APIs
- A mechanism for treating individual (scalar) objects and compositions of objects in a
uniform manner.

Summary

- Objects can use other objects via inheritance/composition
- Some composed and singular objects need similar/identical behaviours
- Composite design pattern lets us treat both types of objects uniformly
- Python supports iteration with __iter__ the Iterable ABC
- A single object can make itself iterable by yielding self from __iter__

"""