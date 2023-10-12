def Merge(A,B):
    b = []
    h = 0
    j = 0
    r = 0
    while(h<=len(A)-1 and j<=len(B)-1):
        if(A[h] < B[j]):
            b.append(A[h])
            h += 1
        else:
            b.append(B[j])
            j += 1
            r += len(A)-h
    if(h > len(A)-1):
        for i in range(j,len(B)):
            b.append(B[i])
    else:
        for i in range(h,len(A)):
            b.append(A[i])
    return [r,b]

def Sort_And_Count(l1):
    if(len(l1) == 1):
        r = 0
        ra = 0
        rb = 0
    elif(len(l1) == 2):
        if(l1[0] > l1[1]):
            r = 1
            ra = 0
            rb = 0
        else:
            ra = 0
            rb = 0
            r = 0
        l1.sort()
    else:
        A = []
        B = []
        mid = int(len(l1)/2)
        for i in range(0,mid):
            A.append(l1[i])
        for i in range(mid,len(l1)):
            B.append(l1[i])
        t = Sort_And_Count(A)
        ra = t[0]
        la = t[1]
        t= Sort_And_Count(B)
        rb = t[0]
        lb = t[1]
        t = Merge(la,lb)
        r = t[0]
        l1 = t[1]
    return [ra+rb+r,l1]
t1 = Sort_And_Count([5,4,3,2,1])
print("Number of inversions: ", t1[0])
print("Sorted list: ", t1[1])
