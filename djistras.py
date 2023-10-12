import heapq
def djistras(graph,start):
    distances = {node:float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0,start)]
    while priority_queue:
        a,b = heapq.heappop(priority_queue)
        if(a>distances[b]):
            continue
        for c,d in graph[b].items():
            t = a+d
            if(t<distances[c]):
                distances[c] = t
                heapq.heappush(priority_queue,(t,c))
    return distances
graph = {1:{2:10,5:100},2:{1:10,3:50},3:{2:50,5:10,4:20},4:{3:20,5:60},5:{1:100,3:10,4:60}}
start = 1
distances = djistras(graph,start)
print(distances)
    
