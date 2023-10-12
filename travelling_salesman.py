W = []
n = int(input("Enter the number of nodes: "))
for i in range(n):
    l = []
    for j in range(n):
        l.append(int(input()))
    W.append(l)
s = int(input("Enter the source vertex: "))
S =list(range(n))
S.remove(s)
se = set(S)
memo = {}
def g(i,l1):
    if((i,frozenset(l1)) in memo):
        return memo[(i,frozenset(l1))]
    if(len(l1)==0):
        return W[i][s],[s]
    if(len(l1)==1):
        return W[i][list(l1)[0]]+W[list(l1)[0]][s],[i,list(l1)[0],s]
    else:
        min_path = []
        min_cost = float('inf')
        for a in l1:
            cost,path = g(a,l1-{a})
            total_cost = W[i][a] + cost
            if(total_cost<min_cost):
                min_cost = total_cost
                min_path = [i]+path
        memo[(i,frozenset(l1))] = (min_cost,min_path)
        return min_cost,min_path
cost,path = g(s,se)
print("The min_cost: ",cost)
print("The min_path: ",path)
