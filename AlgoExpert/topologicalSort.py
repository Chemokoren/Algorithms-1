# O(j + d) time | O(j + d) space -Solution 1
def topogologicalSort1(jobs, deps):
    """
    Performs topological sorting to determine the order of jobs' execution.

    Args:
        jobs (List[str]): List of job names.
        deps (List[Tuple[str, str]]): List of tuples representing job dependencies.

    Returns:
        List[str]: Ordered list of job names in the order they should be executed.
                  An empty list is returned if a cycle is detected, indicating impossibility of sorting.

    Time Complexity: O(V + E), where V is the number of jobs and E is the number of dependencies.
    Space Complexity: O(V + E) for storing the job graph and temporary data during traversal.
    """
    jobGraph = createJobGraph(jobs, deps)
    return getOrderedJobs(jobGraph)


def createJobGraph(jobs, deps):
    """
    Creates a job graph with the given jobs and their dependencies.

    Args:
        jobs (List[str]): List of job names.
        deps (List[Tuple[str, str]]): List of tuples representing job dependencies.

    Returns:
        JobGraph: The constructed job graph containing job nodes and their dependencies.
    """
    graph = JobGraph(jobs)
    for prereq, job in deps:
        graph.addPrereq(job, prereq)
    return graph


def getOrderedJobs(graph):
    """
    Performs depth-first traversal to determine the order of jobs' execution.

    Args:
        graph (JobGraph): Job graph containing job nodes and their dependencies.

    Returns:
        List[str]: Ordered list of job names in the order they should be executed.
                  An empty list is returned if a cycle is detected, indicating impossibility of sorting.
    """
    orderedJobs = []
    nodes = graph.nodes
    while len(nodes):
        node = nodes.pop()
        containsCycle = depthFirstTraverse(node, orderedJobs)
        if containsCycle:
            return []
    return orderedJobs


def depthFirstTraverse(node, orderedJobs):
    """
    Performs depth-first traversal to detect cycles and determine the order of jobs' execution.

    Args:
        node (JobNode): Current job node being visited.
        orderedJobs (List[str]): List to store the ordered job names.

    Returns:
        bool: True if a cycle is detected, False otherwise.
    """
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
    node.visiting = False  # Reset visiting flag (not mandatory)
    orderedJobs.append(node.job)
    return False


class JobGraph:
    """
    Represents a graph of jobs and their dependencies.
    """
    def __init__(self, jobs):
        """
        Initializes the job graph with the given list of job names.

        Args:
            jobs (List[str]): List of job names.
        """
        self.nodes = []
        self.graph = {}
        for job in jobs:
            self.addNode(job)

    def addPrereq(self, job, prereq):
        """
        Adds a prerequisite dependency between two jobs.

        Args:
            job (str): The name of the dependent job.
            prereq (str): The name of the prerequisite job.
        """
        jobNode = self.getNode(job)
        prereqNode = self.getNode(prereq)
        jobNode.prereqs.append(prereqNode)

    def addNode(self, job):
        """
        Adds a new job node to the graph.

        Args:
            job (str): The name of the job to add.
        """
        self.graph[job] = JobNode(job)
        self.nodes.append(self.graph[job])

    def getNode(self, job):
        """
        Retrieves the node corresponding to the given job name.
        Creates a new node if the job does not exist in the graph.

        Args:
            job (str): The name of the job.

        Returns:
            JobNode: The node corresponding to the given job.
        """
        if job not in self.graph:
            self.addNode(job)
        return self.graph[job]


class JobNode:
    """
    Represents a node (job) in the job graph.
    """
    def __init__(self, job):
        """
        Initializes a job node with the given job name.

        Args:
            job (str): The name of the job.
        """
        self.job = job
        self.prereqs = []  # List of prerequisite job nodes
        self.visited = False  # Flag to track visited status during traversal
        self.visiting = False  # Flag to track currently visiting status during traversal


jobs = [1, 2, 3, 4]
deps = [(1, 2), (1, 3), (3, 2), (4, 2), (4, 3)]
actual_result = topogologicalSort1(jobs, deps)
print(f" solution 1:: {actual_result}")

print("------------------- solution 2 ------------------")

# Solution 2

"""
The problem case in the given topological sort problem is when there are cyclic dependencies between 
jobs. 
Cyclic dependencies create a situation where it's impossible to determine a valid execution order 
because each job depends on another job that in turn depends on the first job, 
creating an infinite loop.

To solve this problem, the topological sorting algorithm needs to detect and handle cycles in the graph.
One approach to handle cycles is to perform a depth-first search (DFS) traversal of the graph while 
keeping track of visited nodes and exploring each node's neighbors. 
If a node is encountered that has already been visited, it indicates a cycle in the graph.

Here's a general thought process for handling cycles in the topological sort algorithm:

    Start with the existing implementation of the topological sort algorithm.
    Implement a depth-first search (DFS) traversal function that detects cycles in the graph.
    During the DFS traversal, maintain three states for each node: unvisited, visiting, and visited.
    When visiting a node, mark it as visiting. If any of its neighbors are currently being visited, it indicates a cycle.
    If a cycle is detected during DFS, halt the traversal and report an error.
    After DFS traversal, if no cycles are detected, proceed with the topological sort as usual.

By incorporating cycle detection into the topological sort algorithm, the solution can handle cases where cyclic dependencies exist between jobs, ensuring a valid execution order is returned without entering an infinite loop.

"""
# O(j + d) time | O(j + d) space
# def topogologicalSort1(jobs, deps):
#     """
#     Performs topological sorting to find the order in which jobs should be executed.

#     Args:
#         jobs (List[str]): A list of job names.
#         deps (List[Tuple[str, str]]): A list of tuples representing dependencies between jobs.

#     Returns:
#         List[str]: A list of job names in the order they should be executed.
#     """
#     jobGraph = createJobGraph(jobs, deps)
#     return getOrderedJobs(jobGraph)


# def createJobGraph(jobs, deps):
#     """
#     Creates a job graph with the given jobs and dependencies.

#     Args:
#         jobs (List[str]): A list of job names.
#         deps (List[Tuple[str, str]]): A list of tuples representing dependencies between jobs.

#     Returns:
#         JobGraph: The job graph representing the dependencies between jobs.
#     """
#     graph = JobGraph(jobs)
#     for job, dep in deps:
#         graph.addDep(job, dep)
#     return graph


# def getOrderedJobs(graph):
#     """
#     Performs topological sorting to find the order in which jobs should be executed.

#     Args:
#         graph (JobGraph): The job graph representing the dependencies between jobs.

#     Returns:
#         List[str]: A list of job names in the order they should be executed.
#     """
#     orderedJobs = []
#     nodesWithNoPrereqs = list(filter(lambda node: node.numOfPrereqs == 0, graph.nodes))
#     while len(nodesWithNoPrereqs):
#         node = nodesWithNoPrereqs.pop()
#         orderedJobs.append(node.job)
#         removeDeps(node, nodesWithNoPrereqs)
#     graphHasEdges = any(node.numOfPrereqs for node in graph.nodes)
#     return [] if graphHasEdges else orderedJobs


# def removeDeps(node, nodesWithNoPrereqs):
#     """
#     Removes dependencies of a node and updates the list of nodes with no prerequisites.

#     Args:
#         node (JobNode): The node whose dependencies should be removed.
#         nodesWithNoPrereqs (List[JobNode]): The list of nodes with no prerequisites.
#     """
#     while len(node.deps):
#         dep = node.deps.pop()
#         dep.numOfPrereqs -= 1
#         if dep.numOfPrereqs == 0:
#             nodesWithNoPrereqs.append(dep)





# class JobGraph:
#     """
#     Represents a graph of jobs and their dependencies.

#     Attributes:
#         nodes (List[JobNode]): A list of all nodes (jobs) in the graph.
#         graph (Dict[str, JobNode]): A dictionary mapping job names to JobNode objects.
#     """
#     def __init__(self, jobs):
#         """
#         Initializes the JobGraph with the given list of job names.

#         Args:
#             jobs (List[str]): A list of job names.
#         """
#         self.nodes = []
#         self.graph = {}
#         for job in jobs:
#             self.addNode(job)

#     def addDep(self, job, dep):
#         """
#         Adds a dependency between two jobs.

#         Args:
#             job (str): The name of the dependent job.
#             dep (str): The name of the prerequisite job.
#         """
#         jobNode = self.getNode(job)
#         depNode = self.getNode(dep)
#         jobNode.deps.append(depNode)
#         depNode.numOfPrereqs += 1

#     def addNode(self, job):
#         """
#         Adds a new job node to the graph.

#         Args:
#             job (str): The name of the job to add.
#         """
#         self.graph[job] = JobNode(job)
#         self.nodes.append(self.graph[job])

#     def getNode(self, job):
#         """
#         Retrieves the node (JobNode object) corresponding to the given job name.
#         If the job does not exist in the graph, it creates a new node.

#         Args:
#             job (str): The name of the job.

#         Returns:
#             JobNode: The node corresponding to the given job.
#         """
#         if job not in self.graph:
#             self.addNode(job)
#         return self.graph[job]


# class JobNode:
#     """
#     Represents a node in the job graph.

#     Attributes:
#         job (str): The name of the job.
#         deps (List[JobNode]): A list of dependency nodes.
#         numOfPrereqs (int): The number of prerequisites for the job.
#     """
#     def __init__(self, job):
#         """
#         Initializes a JobNode with the given job name.

#         Args:
#             job (str): The name of the job.
#         """
#         self.job = job
#         self.prereqs = []  # Not used in this implementation
#         self.numOfPrereqs = 0
#         self.deps = []


# import unittest

# class TestTopologicalSort(unittest.TestCase):

#     def test_topological_sort(self):
#         jobs = ["a", "b", "c", "d", "e", "f"]
#         deps = [("a", "d"), ("f", "b"), ("b", "d"), ("f", "a"), ("d", "c")]
#         expected_order = ["f", "e", "b", "a", "d", "c"]
#         self.assertEqual(topogologicalSort1(jobs, deps), expected_order)

#     def test_no_dependencies(self):
#         jobs = ["a", "b", "c", "d", "e"]
#         deps = []
#         expected_order = ["a", "b", "c", "d", "e"]
#         self.assertEqual(topogologicalSort1(jobs, deps), expected_order)

#     def test_circular_dependencies(self):
#         jobs = ["a", "b", "c"]
#         deps = [("a", "b"), ("b", "c"), ("c", "a")]
#         self.assertEqual(topogologicalSort1(jobs, deps), [])

#     def test_duplicate_dependencies(self):
#         jobs = ["a", "b", "c"]
#         deps = [("a", "b"), ("a", "b"), ("b", "c")]
#         expected_order = ["a", "b", "c"]
#         self.assertEqual(topogologicalSort1(jobs, deps), expected_order)

#     def test_empty_jobs(self):
#         deps = [("a", "b"), ("b", "c")]
#         self.assertEqual(topogologicalSort1([], deps), [])

#     def test_empty_dependencies(self):
#         jobs = ["a", "b", "c"]
#         self.assertEqual(topogologicalSort1(jobs, []), ["a", "b", "c"])

# if __name__ == '__main__':
#     unittest.main()

import unittest

class TestTopologicalSort(unittest.TestCase):

    def test_topological_sort(self):
        # Test case with a simple dependency graph
        jobs = [1, 2, 3, 4]
        deps = [(1, 2), (1, 3), (3, 2), (4, 2), (4, 3)]
        expected_results = [[1, 4, 3, 2], [4, 1, 3, 2]]  # List of valid orderings
        actual_result = topogologicalSort1(jobs, deps)
        self.assertIn(actual_result, expected_results)


    def test_topological_sort_empty_deps(self):
        # Test case with no dependencies
        jobs = [1, 2, 3]
        deps = []
        expected_result = {1, 2, 3}  # Use set instead of list
        actual_result = set(topogologicalSort1(jobs, deps))  # Convert the actual result to a set
        self.assertSetEqual(actual_result, expected_result)


    def test_topological_sort_circular_dependency(self):
        # Test case with circular dependency
        jobs = [1, 2, 3]
        deps = [(1, 2), (2, 3), (3, 1)]
        expected_result = []
        self.assertEqual(topogologicalSort1(jobs, deps), expected_result)

    def test_topological_sort_duplicate_deps(self):
        # Test case with duplicate dependencies
        jobs = [1, 2, 3]
        deps = [(1, 2), (1, 2), (2, 3)]
        expected_result = [1, 2, 3]
        self.assertEqual(topogologicalSort1(jobs, deps), expected_result)

if __name__ == "__main__":
    unittest.main()
