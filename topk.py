# Python code to find top 'k' frequent element

# Importing
import collections
from operator import itemgetter
from itertools import chain

# Input list initialization
Input =[[('Name', 151)], [('ACe', 400)],
		[('TURN', 210)], [('RED', 1113)],
		[('YELLOW', 1)]]

# K initialization
K = 4

# Using defaultdict to find top 'k' frequent element
dict_ = collections.defaultdict(list)
new_list = list(chain.from_iterable(Input))

for elem in new_list:
	dict_[elem[0]].append(elem[1])

res = {k: sum(v) for k, v in dict_.items()}

# Using sorted
Output = sorted(res.items(), key = itemgetter(1),
							reverse = True)[0:K]

# printing output
print("Initial List of tuple is", Input)
print("\nTop 'K' elements are", Output)



"""
Method #2: Using itertools and sorted
"""

# Python code to find top 'k' frequent element
from operator import itemgetter
from itertools import chain

# Input list initialization
Input =[[('Name', 151)], [('ACe', 400)],
		[('TURN', 210)], [('RED', 1113)],
		[('YELLOW', 1)]]

# k initialization
K = 2

# Finding top 'k' frequent element
# without using collection
Output = sorted(list(chain.from_iterable(Input)),
		key = itemgetter(1), reverse = True)[0:K]

# Printing Output
print("Initial List of tuple is", Input)
print("\nTop 'K' elements are", Output)
