l = []
graph = {}
n = int(input("Enter the number of nodes: "))
for i in range(n):
    item = int(input("Enter the name of the node: "))
    l.append(item)
    n1= int(input("Enter the number of adjacent nodes: "))
    l1 = []
    for j in range(n1):
        ele = int(input("Enter the adjacent node: "))
        l1.append(ele)
    graph[item] = l1
m = []
print(graph)
cost ={}
for i in range(n):
    for j in range(n):
        print("Enter the cost btw node ",l[i]," and ",l[j])
        c = int(input())
        cost[str(l[i])+"-"+str(l[j])] = c
for i in range(n):
    l1 = []
    for j in range(n):
        l1.append(cost[str(l[i])+"-"+str(l[j])])
    m.append(l1)
slist = [l[0]]
min_spanning_tree = {}
while(len(slist)<n):
    l2 = []
    li = []
    lj = []
    for j in slist:
        i= l.index(j)
        for x in range(len(l)):
            if(l[x] not in slist):
                l2.append(m[i][x])
                li.append(i)
                lj.append(x)
    mini = l2[0]
    for k in range(len(l2)):
        if(l2[k]<mini and l2[k]!=0):
            mini = l2[k]
    ind = l2.index(mini)
    slist.append(l[lj[ind]])
    min_spanning_tree[str(l[li[ind]])+"-"+str(l[lj[ind]])] = mini
print(min_spanning_tree)
        
    
