w = [0]
p =[0]
s = [0]
f= [0]
n = int(input("Enter the number of items: "))
for i in range(1,n+1):
    start = int(input("Enter the starting time: "))
    s.append(start)
    finish = int(input("Enter the finish time: "))
    f.append(finish)
    weight = int(input("Enter the weight: "))
    w.append(weight)
for i in range(1,n+1):
    for j in range(i-1,-1,-1):
        if(s[i]>=f[j]):
            p.append(j)
            break
f.sort()
m = [0]
for i in range(1,n+1):
    m.append(0)
def compute_opt(j):
    if(j==0):
        return 0
    elif(m[j]!=0):
        return m[j]
    else:
        m[j] = max(compute_opt(p[j])+w[j],compute_opt(j-1))
        return m[j]
def findsol(j):
    if(j==0):
        return
    elif(m[p[j]]+w[j]>m[j-1]):
        print(j)
        findsol(p[j])
    else:
        findsol(j-1)
print(compute_opt(n))
findsol(n)
    
