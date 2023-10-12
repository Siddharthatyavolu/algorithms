class unionfind:
    def __init__(self,n):
        self.parent = list(range(n))
        self.rank = [0]*n
    def find(self,x):
        if(self.parent[x]!=x):
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self,x,y):
        rootx = self.find(x)
        rooty = self.find(y)
        if(rootx==rooty):
            return
        if(self.rank[rootx]<self.rank[rooty]):
            self.parent[rootx] =rooty
        elif(self.rank[rootx]>self.rank[rooty]):
            self.parent[rooty] =rootx
        else:
            self.parent[rooty] = rootx
            self.rank[rootx] = self.rank[rootx]+1
def kruskals(graph):
    def find_mst():
        mst = []
        graph.sort(key=lambda x:x[2])
        for edge in graph:
            u,v,w = edge
            if(uf.find(u)!=uf.find(v)):
                uf.union(u,v)
                mst.append(edge)
        return mst
    numv = max(max(edge[0],edge[1]) for edge in graph)+1
    uf = unionfind(numv)
    tree = find_mst()
    print(tree)
n = int(input("Enter the number of edges: "))
graph = []
for i in range(n):
    u= int(input("Enter v1: "))
    v = int(input("Enter v2: "))
    w = int(input("Enter the cost: "))
    graph.append((u,v,w))
kruskals(graph)
