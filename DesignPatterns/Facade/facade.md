Facade
------

- An outward appearance that is used to conceal a less pleasant or credible reality.
- In programming word the outward appearance is the class or interface we interact with and the less pleasant is the complexity(a complicated set of interdependent subsystems) hidden from us.

- A facade is simply a wrapper class that can be used to abstract lower level details that we don't wanna worry about

- Common examples include http clients that abstract how low level network details e.g.
fetch('http://example.com/movies.json')
    .then((response)=> response.json())
    .then((data)=> console.log(data))
    
-or even arrays i.e. dynamic arrays like vectors(C++), ArrayList(Java) are constantly being resized under the hood.
