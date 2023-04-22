from cmath import log
import heapq
from queue import PriorityQueue
from typing import List, Tuple
from math import floor, inf, log2

def floyd_warshall(graph):
    n = len(graph)
    dist = [[float('inf') for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        dist[i][i] = 0
        
    for i in range(n):
        for j,w in graph[i]:
            dist[i][j] = w
                
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
                
    return dist
    
def Dijkstra(n, graph, cool_nodes):
    d = [0 for _ in range(n)]
    for node in cool_nodes:
        d[node] = dijkstra(n, graph, node)
        
    return d

def dijkstra(n, graph, start):
    distances = [inf for _ in range(n)]
    distances[start] = 0
    pq = [(0, start)]
    
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        
        if current_distance > distances[current_node]:
            continue
            
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
                
    return distances
            
    

def solve(n : int, edges: List[Tuple[int, int, int]], Q : List[Tuple[int, int, int]]):

    m = len(edges)
    G = [[] for _ in range(n)]
    for x,y,w in edges:
        G[x].append((y, w))
        G[y].append((x, w))
    
    cool_nodes = set()
    for q in Q:
        cool_nodes.add(q[0])
        cool_nodes.add(q[1])
    
    if m * log2(m) < n**2:
        d = Dijkstra(n, G, cool_nodes)
    else:
        d = floyd_warshall(G)
    ans = 0
    for x,y,w in edges:
        for u,v,l in Q:
            if d[u][x] + d[v][y] + w <= l or d[v][x] + d[u][y] + w <= l:
                ans+=1
                break    
            
    return ans
        
n = 7
edges = [(0,1,9),
         (4,1,6),
         (0,3,33),
         (0,4,12),
         (5,2,8),
         (6,1,5),
         (0,5,7)
         ]   

Q = [(0, 2, 80)]
print(solve(n,edges,Q))