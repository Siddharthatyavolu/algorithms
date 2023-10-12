class bellman:
    def __init__(self,n):
        self.max = 999
        self.n = n
        self.distances = []
    def calculate(self,s,adj):
        for i in range(self.n):
            self.distances.append(self.max)
        self.distances[s-1] = 0
        for i in range(self.n-1):
            for j in range(self.n):
                for k in range(self.n):
                    if(self.distances[k]>self.distances[j] + adj[j][k]):
                        self.distances[k]=self.distances[j] + adj[j][k]
        for i in range(n):
            print("The distance from source to ",i+1," is: ",self.distances[i])
n = int(input("Enter the number of vertices: "))
s = int(input("Enter the source vertex:: "))
print("Enter the adj: ")
adj = []
for i in range(n):
    l1 = []
    for j in range(n):
        l1.append(int(input()))
    adj.append(l1)
b = bellman(n)
b.calculate(s,adj)
