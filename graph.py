from collections import defaultdict, deque
import heapq

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    # adding a vertext to graph
    def insert_vertex(self, v):
        if v not in self.graph:
            self.graph[v] = []

    # function for adding edge between two points, you'll choose what two vertexes
    # end up constructing graph however you want
    def insert_edge(self, u, v):

        # can only insert an edge among existing nodes
        if u not in self.graph or v not in self.graph:
            raise ValueError("Both vertices must exist in graph!")
        self.graph[u].append(v)
        self.graph[v].append(u)

    # iterative method of dfs 
    def dfs(self, s):

           # can only insert an edge among existing nodes
        if s not in self.graph:
            raise ValueError("Vertex must exist in graph!")
        
        visited = set()
        stack = [s]
        visited.add(s)
        result = []

        # uses a stack to traverse
        # dfs goes "straight through" then on way back collects rest
        while stack:
            v = stack.pop()
            result.append(v)
            for neighbor in self.graph[v]:
                if neighbor not in visited:
                    stack.append(neighbor)
                    visited.add(neighbor)        
        return result
    
    def bfs(self, s):
        
           # can only insert an edge among existing nodes
        if s not in self.graph:
            raise ValueError("Vertex must exist in graph!")
        
        visited = set()
        q = []
        result = []

        # starting point
        q.append(s)
        visited.add(s)

        while q:
            v = q.pop(0)
            for neighbor in self.graph[v]:
                if neighbor not in visited:
                    # append a tuple as it helps track the edges
                    result.append((v, neighbor))
                    q.append(neighbor)
                    visited.add(neighbor)
        return result
    
    def dijkstra(self, s):

        # can only insert an edge among existing nodes
        if s not in self.graph:
            raise ValueError("Vertex must exist in graph!")
        
        # dictionary to set all the distances to inf
        # that way we can later update to real # else leave it inf
        distances = {v: float('inf') for v in self.graph}
        distances[s] = 0

        # make a priority queue, starting from start
        pq = [(0, s)]

        while pq:
            curr_dist, curr_vertex = heapq.heappop(pq)
            if curr_dist > distances[curr_vertex]:
                continue
            for neighbor in self.graph[curr_vertex]:
                # our graph implementation isnt gonna have weights
                # so we are just gonna say each edge "weight" = 1
                distance = curr_dist + 1

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor))

        return distances
    
    def find_path(self, u, v):

        # can only insert an edge among existing nodes
        if u not in self.graph or v not in self.graph:
            raise ValueError("Both vertices must exist in graph!")
        
        # dictionary to hold path of vertices
        path = {}

        # using a BFS approach so using a queue system
        q = deque([u])

        while q:
            # pop from queue
            curr = q.popleft()

            # test case if this is the path
            if curr == v:
                path_list = [v]
                # since we have found destination we trace back to the start
                while v != u:
                    # this will move back through the dictionary
                    v = path[v]
                    # add path to list
                    path_list.append(v)
                    # since we iterated backwards (v to u)
                    # we need to reverse the list so its (u to v)
                return path_list[::-1] # this returns it backwards, reverse() doesnt
            
            # if the pop wasnt the end goal we starting looking at neighbors
            for neighbor in self.graph[curr]:
                if neighbor not in path:
                    path[neighbor] = curr
                    q.append(neighbor)

        # if a path never gets found
        return None

if __name__ == "__main__":

    graph = Graph()

    # add verteces
    graph.insert_vertex('a')
    graph.insert_vertex('b')
    graph.insert_vertex('c')
    graph.insert_vertex('d')
    graph.insert_vertex('e')

    # add edges
    graph.insert_edge('a', 'b')
    graph.insert_edge('a', 'c')
    graph.insert_edge('b', 'd')
    graph.insert_edge('b', 'e')
    graph.insert_edge('d', 'e')

    print("BFS: ", graph.bfs('a'))
    print("DFS: ", graph.dfs('a'))
    print("Dijkstra: ", graph.dijkstra('a'))
    print("Path from a - e:", graph.find_path('a', 'e'))
    print("Path from b - d:", graph.find_path('b', 'd'))
    #print("Path from x - y:", graph.find_path('x', 'y')) # error case
    #print("Path from a - b:", graph.find_path('a', 'b'))