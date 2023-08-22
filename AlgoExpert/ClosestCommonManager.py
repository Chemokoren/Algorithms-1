# Closest Common Manager Problem
# This repository has two different solutions to the problem listed below. One solution is implemented in Python and the other in JavaScript. The JS implementation uses classical inheritance over prototypical inheritance because I wanted to stay true to the assignment (which was supposed to be written in either Java or C).
#
# The Question:
#
# Initech is a company which has CEO Bill and a hierarchy of employees. Employees can have a list of other employees reporting to them, which can themselves have reports, and so on. An employee with at least one report is called a manager.
#
# Please implement the closestCommonManager method to find the closest manager (i.e. farthest from the CEO) to two employees. You may assume that all employees eventually report up to the CEO.
#
# Tree structure:
#
# Bill -> Dom, Samir, Michael
#
# Dom -> Bob, Peter, Porter
#
# Peter -> Milton, Nina
#
# Sample Data:
#
# CEO Bill has 3 employees reporting to him: {Dom, Samir, Michael}
#
# Dom has three reports { Peter, Bob, Porter}
#
# Samir has no reports {}
#
# Michael has no reports {}
#
# Peter has 2 reports {Milton, Nina}
#
# Bob has no reports {}
#
# Porter has no reports {}
#
# Milton has no reports {}
#
# Nina has no reports {}
#
# Sample calls:
#
# closestCommonManager(Milton, Nina) = Peter
#
# closestCommonManager(Nina, Porter) = Dom
#
# closestCommonManager(Nina, Samir) = Bill
#
# closestCommonManager(Peter, Nina) = Peter
#
# The Solution:
#
# ON THE PROBLEM:
#
# In thinking about the problem for a while, I came across a couple different solutions. The JS program traverses the tree by starting at the root and goes to each child and recursively checks each path to see where the report is. Once found, I store each of the parent managers to an array. I end up with two arrays, one for each employee, consisting of the parent managers to the employee found. Once I have both arrays, I check each array for equality and if equal, I push it to a temp array. If they aren't equal, I print the last item in the temp array, which is the manager.
#
# For example: After traversing the tree for PETER and PORTER, the arrays will look like:
#
# Peter: [Bill, Dom, Peter]
#
# Porter: [Bill, Dom, Porter]
#
# Once these are found, a loop is run until there is a difference between the arrays and then the last matching item in the array is used (Dom, in this case).
#
# ON TIME COMPLEXITY:
#
# Regarding time complexity, this process leads to a O(n) time complexity, where n signifies the number of employees. We would span O(n) twice, with the comparison being O(m), where m signifies the number of levels from lowest employee to CEO (including the two of them).
#
# In order to reduce time complexity and make it faster, we would need to target the data structure used. I would use a hash table that would store employees and their manager. If we have a hash table, my assumption is that it would reduce the time complexity to O(m). We would get the employee immediately (no tree traversal), and then check managers and do a comparison, which as mentioned previously, is O(m).

class Employee:

  def __init__(self, id, name):
    self.id = id
    self.name = name
    self.reports = []

  def getId(self):
    return self.id

  def getName(self):
    return self.name

  def getReports(self):
    return self.reports

  def addReport(self, employee):
    self.reports.append(employee)

def getClosestManager(root, employee1, employee2):
  manager, flag1, flag2 = getClosestManager2(root, employee1, employee2)
  print ("Manager of %s and %s is %s" % (employee1.getName(), employee2.getName(), manager.getName()))
  return manager

def getClosestManager2(root, employee1, employee2):
  flag1 = (root == employee1)
  flag2 = (root == employee2)
  manager = None
  for employee in root.getReports():
    manager, eFlag1, eFlag2 = getClosestManager2(employee, employee1, employee2)
    if manager is not None:
      return manager, flag1, flag2
    flag1 |= eFlag1
    flag2 |= eFlag2
    if flag1 and flag2:
      manager = root
      return manager, flag1, flag2
  return manager, flag1, flag2

def printEmployees(root, header = ""):
  print(header, root.getName())
  for employee in root.getReports():
    printEmployees(employee, header + "  ")

if __name__ == '__main__':
  ceo = Employee(1, 'Bill')
  dom = Employee(2, 'Dom')
  samir = Employee(3, 'Samir')
  michael = Employee(4, 'Michael')
  bob = Employee(5, 'Bob')
  peter = Employee(6, 'Peter')
  porter = Employee(7, 'Porter')
  milton = Employee(8, 'Milton')
  nina = Employee(9, 'Nina')
  ceo.addReport(dom)
  ceo.addReport(samir)
  ceo.addReport(michael)
  dom.addReport(bob)
  dom.addReport(peter)
  dom.addReport(porter)
  peter.addReport(milton)
  peter.addReport(nina)
  getClosestManager(ceo, peter, porter)
