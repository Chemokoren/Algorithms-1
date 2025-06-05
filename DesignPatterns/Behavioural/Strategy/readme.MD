# Strategy Design Pattern

Enables the exact behavior of a system to be selected at run-time.

-Many algorithms can be decomposed into higher - and lower-level parts
-Making tea can be decomposed into
    a) The process of making a hot beverage (boil water, pour into cup) and
    b) Tea-specific things (put teabag into water)
-The high-level algorithm can then be reused for making coffee or hot chocolate
    a) supported by beverage-specific strategies

### Summary
- Define an algorithm at a high level
- Define the interface you expect each strategy to follow
- Provide for dynamic composition of strategies in the resulting object