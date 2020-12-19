# "FIND THE TOWN JUDGE"

from collections import defaultdict

def findJudge(n, trust):
    
    # Handle edge case when N=1
    if N == 1: return 1

    # Init graphs
    g1 = defaultdict(list)
    g2 = defaultdict(list)

    # Add edges to graphs, one normal and one reversed
    for t in trust:
        x, y = t[0], t[1]
        g1[x].append(y)
        g2[y].append(x)
    
    # Scan through all trusted vertices in g2 to find a 
    # vertex that is trusted by all others and trusts none
    for v in g2:
        if len(g2[v]) == n-1 and not g1[v]:
            return v
    
    return -1





# Attempt 1. Correct, but overly complex.

# from collections import defaultdict, deque

# # Directed graph adjacency list class
# class Graph:

#     # Init graph
#     def __init__(self):
#         self.graph = defaultdict(list)
#         self.discovered = defaultdict(bool)
#         self.toporder = deque([])

#     # Add edge
#     def add_edge(self, x, y):
#         self.graph[x].append(y)
    
#     # DFS
#     def dfs(self, v):
#         if self.discovered[v]: return
#         self.discovered[v] = True
#         for y in self.graph[v]:
#             self.dfs(y)
#         self.toporder.appendleft(v)

# # Main program
# def findJudge(n, trust):

#     # Init graphs
#     g1 = Graph()    # Normal
#     g2 = Graph()    # Reverse direction

#     # Add edges to graph
#     for t in trust:
#         x = t[0]
#         y = t[1]
#         g1.add_edge(x, y)
#         g2.add_edge(y, x)

#     # Topsort
#     vertices = g2.graph.copy()
#     for v in vertices:
#         if not g2.discovered[v]:
#             g2.dfs(v)
#     start = g2.toporder[0]
    
#     # Make sure start vertex is trusted by all and trusts no one
#     if len(g2.graph[start]) == n-1 and not g1.graph[start]:
#         return start
#     else:
#         return -1


# n = 4
# trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
# print(findJudge(n, trust))
