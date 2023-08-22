"""
Builder Design Pattern
----------------------

What is the motivation?
-----------------------
- Some objects are simple and can be created in a single initializer call
- Other objects require alot of ceremony to create
- Having an object with 10 initializer arguments is not productive
- Istead, opt for piecewise construction
- Builder provides an API for constructing an object step-by-step

When piecewise object construction is complicated, the builder provide an API for doing it succinctly.

Summary
-------
- A builder is a seperate component for building an object
- Can either give builder an initializer or return it via a static function
- To make builder fluent, return self
- Different facets of an object can be built with different builders working in tandem via a base class

"""