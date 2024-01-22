"""
If you want to modify or extend the behavior of class without directly changing it, you
can go with the Strategy Pattern.

Remove Negatives
[-7, -4, -1, 0, 2, 6, 9]

For example, we can filter an array by removing positive values

[0,2,6,9]

or we can filter it by removing all odd values

remove odd
[-7, -4, -1, 0, 2, 6, 9]

           |
           V
    [-4, 0, 2, 6] 
    
This are two strategies but maybe in the future we wanna add more and we want
to follow the open-closed principle (i.e. open for extension but closed for 
modifications)

"""
from abc import ABC, abstractmethod

class FilterStrategy(ABC):
    
    @abstractmethod
    def removeValue(self, val):
        pass
    
class RemoveNegativeStrategy(FilterStrategy):
    
    def removeValue(self, val):
        # return super().removeValue(val)
        return val < 0

class RemoveOddStrategy(FilterStrategy):
    
    def removeValue(self, val):
        # return super().removeValue(val)
        return abs(val) % 2
    
    
class Values:
    
    def __init__(self, vals):
        self.vals = vals
        
    def filter(self, strategy):
        res =[]
        for n in self.vals:
            if not strategy.removeValue(n):
                res.append(n)
        return res
    
values = Values([-7,-4, -1, 0, 2, 6, 9])

print(values.filter(RemoveNegativeStrategy())) #[0, 2, 6, 9]
print(values.filter(RemoveOddStrategy())) # [-4, 0, 2, 6]

# we can now add other strategies without modifying our Values class

"""
Note: return abs(val) % 2

the purpose of using abs() in the original code may not necessarily be related to the 
sign of val. It could be used to handle cases where val is a float or a complex number, 
in which case abs() returns the magnitude of the number.
Using abs() ensures that the input to % is a non-negative integer.

For example, consider the case where val is a complex number:

val = 3 + 4j
result = abs(val) % 2
print(result)  # Output: 1

In this case, the abs() function returns the magnitude of the complex number val, 
which is 5. The result of abs(val) % 2 is 1, which indicates that val is an odd number.
"""

print("------------------------------ example -------------------------------")

from abc import ABC
from enum import Enum, auto

class OutputFormat(Enum):
    MARKDOWN = auto()
    HTML = auto()

# not required but a good idea
class ListStrategy(ABC):

    def start(self, buffer): pass

    def end(self, buffer): pass

    def add_list_item(self, buffer, item): pass

class MarkdownListStrategy(ListStrategy):

    def add_list_item(self, buffer, item):
        buffer.append(f' * {item} \n')

class HtmlListStrategy(ListStrategy):

    def start(self, buffer):
        buffer.append('<ul>\n')

    def end(self, buffer):
        buffer.append('</ul>\n')

    def add_list_item(self, buffer, item):
        buffer.append(f' <li> {item} </li>\n')

class TextProcessor:

    def __init__(self, list_strategy=HtmlListStrategy()):
        self.buffer = []
        self.list_strategy = list_strategy

    def append_list(self, items):
        self.list_strategy.start(self.buffer)
        for item in items:
            self.list_strategy.add_list_item(self.buffer, item)
        self.list_strategy.end(self.buffer)

    def set_output_format(self, format):
        if format == OutputFormat.MARKDOWN:
            self.list_strategy = MarkdownListStrategy()
        elif format == OutputFormat.HTML:
            self.list_strategy = HtmlListStrategy()

    def clear(self):
        self.buffer.clear()

    def __str__(self) -> str:
        return ''.join(self.buffer)
    
if __name__=='__main__':
    items =['foo', 'bar', 'baz']

    tp = TextProcessor()
    tp.set_output_format(OutputFormat.MARKDOWN)
    tp.append_list(items)
    print(tp)

    tp.set_output_format(OutputFormat.HTML)
    tp.clear()
    tp.append_list(items)
    print(tp)