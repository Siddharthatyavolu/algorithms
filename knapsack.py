weight = []
profit = []
item = []
n = int(input("Enter the number of items: "))
for i in range(n):
    w = int(input("Enter the weight: "))
    weight.append(w)
    p = int(input("Enter the profit: "))
    profit.append(p)
    i = int(input("Enter the item: "))
    item.append(i)
W = int(input("Enter the weight bound: "))
m = []
for i in range(0,n+1):
    l = []
    for j in range(0,W+1):
        l.append(0)
    m.append(l)
for i in range(1,n+1):
    for j in range(1,W+1):
        if(weight[i-1]>j):
            m[i][j] =m[i-1][j]
        else:
            m[i][j] = max(m[i-1][j],profit[i-1]+m[i-1][j-weight[i-1]])
print(m[n][W])
i =n
k = W
subset= []
while(i>0 and k>0):
    if(m[i][k]!=m[i-1][k]):
        subset.append(item[i-1])
        k = k-weight[i-1]
        i =i-1
    else:
        i = i-1
print(subset)
    
            
        
    
