d={5:[(7,2),(3,1)],7:[(5,2),(4,3),(3,4)],4:[(7,3),(8,2),(2,6)],8:[(2,4),(3,1),(4,2)],3:[(5,2),(7,4),(8,1)],2:[(4,6),(8,4)]}
def all_paths_cost(start,end,s,c):
    s.append(start)
    if start==end:
        print(s,c)
        s.pop()
    else:
        for i in d[start]:
            if i[0] not in s:
                c+=i[1]
                all_paths_cost(i[0],end,s,c)
                c-=i[1]
        s.pop()
all_paths_cost(5,2,[],0)
def min_cost(start,end,s,c,m):
    s.append(start)
    if start==end:
        if c<m:
            m=c
        s.pop()
        return m
    for i in d[start]:
        if i[0] not in s:
            c+=i[1]
            m=min_cost(i[0],end,s,c,m)
            c-=i[1]
    s.pop()
    return m
print(min_cost(5,2,[],0,99999))
def min_cost_path(start,end,s,c,res,m):
    s.append(start)
    if start==end:
        if c<m:
            res=s.copy()
            m=c
        s.pop()
        return res,m
    for i in d[start]:
        if i[0] not in s:
            c+=i[1]
            res,m=min_cost_path(i[0],end,s,c,res,m)
            c-=i[1]
    s.pop()
    return res,m
print(min_cost_path(5,2,[],0,[],999))