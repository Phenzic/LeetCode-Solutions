class Solution(object):
    

    def validPath(self, n, edges, source, destination):
        def to_graph(edge):
            graph = {}
            for i in edge:
                a, b = i
                if a not in graph:
                    graph[a] = []
                if b not in graph:
                    graph[b] = []
                graph[a].append(b)
                graph[b].append(a)
            
            print(graph)
            return graph

        def hasPath(graph, src, dst, visited = None):
            if visited is None:
                visited = set()

            if src == dst:
                return True
            if src in visited:
                return False
            visited.add(src)

            for p in graph[src]:
                if hasPath(graph, p, dst, visited):
                    return True
            return False

        result = to_graph(edges)
        ans = hasPath(result, source, destination, visited=None)
        return ans


