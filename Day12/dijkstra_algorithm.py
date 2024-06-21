g={1:[[2,3],[5,4]],2:[[1,3],[3,1],[4,1]],3:[[2,1],[4,2]],4:[[2,1],[3,2],[5,5]],5:[[1,4],[4,5]]}
def dijkstra(start,v,nv):
    if not nv:
        return d
    for i in g[start]:
        if i[0] not in v:
            if d[i[0]]>i[1]+d[start]:
                d[i[0]]=i[1]+d[start]
            if i not in nv:
                nv.append(i[0])	
    v.append(start)
    nv.remove(start)
    mn=99999
    k=0
    #print(nv)
    for i in nv:
        if mn>d[i]:
            mn=d[i]
            k=i
    dijkstra(k,v,nv)
start=int(input("Enter the starting node:"))
d=dict()
for i in g:
    if i==start:
        d[i]=0
    else:
        d[i]=99999
dijkstra(start,[],[start])
print(d)