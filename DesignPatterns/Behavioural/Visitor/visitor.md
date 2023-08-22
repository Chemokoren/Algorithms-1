Visitor Design Pattern
----------------------
- Need to define a new operation on an entire class hierarchy e.g., make a document model printable to HTML/Markdown
- Do not want to keep modifying every class in the hierarchy
- Need access to the non-common aspects of classes in the hierarchy
- Create an external component to handle rendering 
    * but avoid explicity type checks

## Visitor 
A component(visitor) that knows how to traverse a data structure composed of (possibly related) types