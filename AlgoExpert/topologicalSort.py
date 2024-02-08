# O(j + d) time | O(j + d) space -Solution 1
# def topogologicalSort(jobs, deps):
#     jobGraph =createJobGraph(jobs, deps)
#     return getOrderedJobs(jobGraph)
#
# def createJobGraph(jobs, deps):
#     graph =JobGraph(jobs)
#     for prereq, job in deps:
#         graph.addPrereq(job, prereq)
#     return graph
#
#
# def getOrderedJobs(graph):
#     orderedJobs =[]
#     nodes =graph.nodes
#     while len(nodes):
#         node =nodes.pop()
#         containsCycle =depthFirstTraverse(node, orderedJobs)
#         if containsCycle:
#             return []
#         return orderedJobs
#
# def depthFirstTraverse(node, orderedJobs):
#     if node.visited:
#         return False
#     if node.visiting:
#         return True
#     node.visiting =True
#     for prereqNode in node.prereqs:
#         containsCycle =depthFirstTraverse(prereqNode,orderedJobs)
#         if containsCycle:
#             return True
#     node.visited =True
#     node.visiting =False # not mandatory
#     orderedJobs.append(node.job)
#     return False
#
#
# class JobGraph:
#     def __init__(self, jobs):
#         self.nodes =[]
#         self.graph ={}
#         for job in jobs:
#             self.addNode(job)
#
#     def addPrereq(self,job, prereq):
#         jobNode =self.getNode(job)
#         prereqNode = self.getNode(prereq)
#         jobNode.prereqs.append(prereqNode)
#
#     def addNode(self,job):
#         self.graph[job] =JobNode(job)
#         self.nodes.append(self.graph[job])
#
#     def getNode(self,job):
#         if job not in self.graph:
#             self.addNode(job)
#         return self.graph[job]
#
# class JobNode:
#     def __init__(self,job):
#         self.job =job
#         self.prereqs =[]
#         self.visited =False
#         self.visiting =False


# Solution 2

# O(j + d) time | O(j + d) space
def topogologicalSort1(jobs, deps):
    """
    Performs topological sorting to find the order in which jobs should be executed.

    Args:
        jobs (List[str]): A list of job names.
        deps (List[Tuple[str, str]]): A list of tuples representing dependencies between jobs.

    Returns:
        List[str]: A list of job names in the order they should be executed.
    """
    jobGraph = createJobGraph(jobs, deps)
    return getOrderedJobs(jobGraph)


def createJobGraph(jobs, deps):
    """
    Creates a job graph with the given jobs and dependencies.

    Args:
        jobs (List[str]): A list of job names.
        deps (List[Tuple[str, str]]): A list of tuples representing dependencies between jobs.

    Returns:
        JobGraph: The job graph representing the dependencies between jobs.
    """
    graph = JobGraph(jobs)
    for job, dep in deps:
        graph.addDep(job, dep)
    return graph


def getOrderedJobs(graph):
    """
    Performs topological sorting to find the order in which jobs should be executed.

    Args:
        graph (JobGraph): The job graph representing the dependencies between jobs.

    Returns:
        List[str]: A list of job names in the order they should be executed.
    """
    orderedJobs = []
    nodesWithNoPrereqs = list(filter(lambda node: node.numOfPrereqs == 0, graph.nodes))
    while len(nodesWithNoPrereqs):
        node = nodesWithNoPrereqs.pop()
        orderedJobs.append(node.job)
        removeDeps(node, nodesWithNoPrereqs)
    graphHasEdges = any(node.numOfPrereqs for node in graph.nodes)
    return [] if graphHasEdges else orderedJobs


def removeDeps(node, nodesWithNoPrereqs):
    """
    Removes dependencies of a node and updates the list of nodes with no prerequisites.

    Args:
        node (JobNode): The node whose dependencies should be removed.
        nodesWithNoPrereqs (List[JobNode]): The list of nodes with no prerequisites.
    """
    while len(node.deps):
        dep = node.deps.pop()
        dep.numOfPrereqs -= 1
        if dep.numOfPrereqs == 0:
            nodesWithNoPrereqs.append(dep)





class JobGraph:
    """
    Represents a graph of jobs and their dependencies.

    Attributes:
        nodes (List[JobNode]): A list of all nodes (jobs) in the graph.
        graph (Dict[str, JobNode]): A dictionary mapping job names to JobNode objects.
    """
    def __init__(self, jobs):
        """
        Initializes the JobGraph with the given list of job names.

        Args:
            jobs (List[str]): A list of job names.
        """
        self.nodes = []
        self.graph = {}
        for job in jobs:
            self.addNode(job)

    def addDep(self, job, dep):
        """
        Adds a dependency between two jobs.

        Args:
            job (str): The name of the dependent job.
            dep (str): The name of the prerequisite job.
        """
        jobNode = self.getNode(job)
        depNode = self.getNode(dep)
        jobNode.deps.append(depNode)
        depNode.numOfPrereqs += 1

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
        Retrieves the node (JobNode object) corresponding to the given job name.
        If the job does not exist in the graph, it creates a new node.

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
    Represents a node in the job graph.

    Attributes:
        job (str): The name of the job.
        deps (List[JobNode]): A list of dependency nodes.
        numOfPrereqs (int): The number of prerequisites for the job.
    """
    def __init__(self, job):
        """
        Initializes a JobNode with the given job name.

        Args:
            job (str): The name of the job.
        """
        self.job = job
        self.prereqs = []  # Not used in this implementation
        self.numOfPrereqs = 0
        self.deps = []


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
        expected_result = [1, 4, 3, 2]
        self.assertEqual(topogologicalSort1(jobs, deps), expected_result)

    def test_topological_sort_empty_deps(self):
        # Test case with no dependencies
        jobs = [1, 2, 3]
        deps = []
        expected_result = [1, 2, 3]
        self.assertEqual(topogologicalSort1(jobs, deps), expected_result)

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
