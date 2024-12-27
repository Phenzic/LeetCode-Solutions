class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
                # Build a directed graph
        graph = {i: [] for i in range(numCourses)}
        for a, b in prerequisites:
            graph[b].append(a)
        
        # Use DFS to detect cycles
        visited = set()  # Tracks nodes visited in the current path
        cycle = set()    # Tracks nodes in a completed DFS path
        
        def hasCycle(course):
            if course in visited:  # Cycle detected
                return True
            if course in cycle:    # Already processed and no cycle
                return False
            
            visited.add(course)
            for neighbor in graph[course]:
                if hasCycle(neighbor):
                    return True
            visited.remove(course)
            cycle.add(course)
            return False
        
        # Check all courses for cycles
        for i in range(numCourses):
            if hasCycle(i):
                return False
        
        return True
       
        # src = 0
        # dst = numCourses - 1

        # def to_graph(node):
        #     graph = {}
        #     for i in node:
        #         a, b = i
        #         if a not in graph:
        #             graph[a] = []
        #         if b not in graph:
        #             graph[b] = []
        #         graph[a].append(b)
        #         graph[b].append(a)
        #     print(graph)
        #     return graph
        
        # def hasPath(graph, src, dst, numCourses, visited = None, cycle = None):
        #     if visited is None:
        #         visited = set()
        #     if src == dst and numCourses > 0:
        #         return True
        #     numCourses = numCourses - 1
        #     if src in visited:
        #         return False
        #     visited.add(src)
        #     print(numCourses,visited)
        #     for i in graph[src]:
        #         print(i)
        #         if hasPath(graph, i, dst, numCourses, visited):
        #             return True
        #     return False
            
        # graph = to_graph(prerequisites)
        # result = hasPath(graph, src, dst, numCourses)
        # return result




        