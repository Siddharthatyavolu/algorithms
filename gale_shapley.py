lm= [['a',{'x':1,'y':2,'w':3,'z':4}],['b',{'z':1,'x':2,'y':3,'w':4}],['c',{'y':1,'z':2,'x':3,'w':4}],['d',{'y':1,'w':2,'x':3,'z':4}]]
lw =[['w',{'c':1,'a':2,'b':3,'d':4}],['x',{'b':1,'d':2,'a':3,'c':4}],['y',{'a':1,'d':2,'c':3,'b':4}],['z',{'c':1,'d':2,'a':3,'b':4}]]
unemen = ['a','b','c','d']
pm = []
pw =[]
while(unemen):
    m = unemen[0]
    for i in range(len(lm)):
        if(m in lm[i]):
            index = lm[i].index(m)
            break
    s = i
    d = lm[s][index+1]
    l = list(d.keys())
    if(l[0] not in pw):
        unemen.remove(m)
        pm.append(m)
        pw.append(l[0])
    if(l[0] in pw):
        i = pw.index(l[0])
        pman = pm[i]
        for i in range(len(lw)):
            if(l[0] in lw[i]):
                ind = lw[i].index(l[0])
                break
        d =lw[i][ind+1]
        if(d[m]<d[pman]):
            i = pm.index(pman)
            pm[i] =m
            unemen.remove(m)
            unemen.append(pman)
        else:
            del lm[s][index+1][l[0]]
for i in range(len(pm)):
    print(pm[i],"-",pw[i])
