"""
Topological Sort

Topological ordering/sort is something done on a directed graph or describes a directed 
graph - linear ordering of the vertices of the graph so long as for every directed edge 
from two vertices(x --> y), so long as x comes before y in the final ordering.

practical application of topological sort:
 given a list of jobs as [1,2,3,4]. And you can think of these jobs as tasks -things 
 that need to be done. You are also given dependencies([[1,2],[1,3],[3,2],[4,2],[4,3]]),
  where are pairs of jobs where some jobs are prerequisites to other jobs. 
  The task is to find the order in which we can complete these jobs that would respect the
  dependencies we are given.

[1,2,3,4][[1,2],[1,3],[3,2],[4,2],[4,3]]

Answer(topological orderings/sorts)= [1,4,3,2] or [4,1,3,2]

Time Complexity: O(j + d)
Space Complexity: O(j + d )

"""
# O(j + d) time | O(j + d) space  - depth first search
def topologicalSort(jobs, deps):
    jobGraph =createJobGraph(jobs,deps)
    return getOrderedJobs(jobGraph)

def createJobGraph(jobs, deps):
    graph = JobGraph(jobs)
    for prereq, job in deps:
        graph.addPrereq(job, prereq)
    return graph

def getOrderedJobs(graph):
    orderedJobs =[]
    nodes = graph.nodes
    while len(nodes):
        node = node.pop()
        containsCycle = depthFirstTraverse(node, orderedJobs)
        if containsCycle:
            return []
    return orderedJobs

def depthFirstTraverse(node, orderedJobs):
    if node.visited:
        return False
    if node.visiting:
        return True
    node.visiting = True
    for prereqNode in node.prereqs:
        containsCycle = depthFirstTraverse(prereqNode, orderedJobs)
        if containsCycle:
            return True
    node.visited = True
    node.visiting = False
    orderedJobs.append(node.job)
    return False

class JobGraph:
    def __init__(self,jobs) -> None:
        self.nodes =[]
        self.graph ={}

        for job in jobs:
            self.addNode(job)

    def addPrereq(self, job, prereq):
        jobNode = self.getNode(job)
        prereqNode = self.getNode(prereq)
        jobNode.prereqs.append(prereqNode)

    def addNode(self, job):
        self.graph[job] = JobNode(job)
        self.nodes.append(self.graph[job])

    def getNode(self, job):
        if job not in self.graph:
            self.addNode(job)
        return self.graph[job]

class JobNode:
    def __init__(self,job) -> None:
        self.job =job
        self.prereqs =[]
        self.visited = False
        self.visiting = False # node in the process of being visited


"""
Approach 2:

"""
# O(j + d) time | O(j + d) space
def topologicalSortTwo(jobs, deps):
    jobGraph =createJobGraph(jobs, deps)
    return getOrderedJobs(jobGraph)

def createJobGraph(jobs, deps):
    graph = JobGraph(jobs)
    for job, dep in deps:
        graph.addDep(job,dep)
    return graph

def getOrderedJobs(graph):
    orderedJobs =[]
    nodesWithNoPrereqs = list(filter(lambda node: node.numOfPrereqs == 0, graph.nodes))
    while len(nodesWithNoPrereqs):
        node = nodesWithNoPrereqs.pop()
        orderedJobs.append(node.job)
        removeDeps(node, nodesWithNoPrereqs)
    graphHasEdges =any(node.numOfPrereqs for node in graph.nodes)
    return [] if graphHasEdges else orderedJobs

def removeDeps(node, nodesWithNoPrereqs):
    while len(node.deps):
        dep = node.deps.pop()
        dep.numOfPrereqs -=1
        if dep.numOfPrereqs == 0:
            nodesWithNoPrereqs.append(dep)

class JobGraph:
    def __init__(self,jobs) -> None:
        self.nodes =[]
        self.graph ={}
        for job in jobs:
            self.addNode(jobs)

    def addDep(self, job, dep):
        jobNode = self.getNode(job)
        depNode = self.getNode(dep)
        jobNode.deps.append(depNode)
        depNode.numOfPrereqs += 1

    def addNode(self, job):
        self.graph[job] = JobNode(job)
        self.nodes.append(self.graph[job])

    def getNode(self,job):
        if job not in self.graph:
            self.addNode(job)
        return self.graph[job]

class JobNode:
    def __init__(self,job) -> None:
        self.job = job
        self.deps =[]
        self.numOfPrereqs = 0



my_jobs=[1,2,3,4]
my_dependencies=[[1,2],[1,3],[3,2][4,2],[4,3]]
print(topologicalSortTwo(my_jobs,my_dependencies))