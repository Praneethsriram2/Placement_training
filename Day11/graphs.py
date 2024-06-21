graph={1:[2,7],2:[1,3,9],3:[2,4],4:[3,5,6,10],5:[4,6,7],6:[4,5,7],7:[1,5,6,8],8:[7,],9:[2,],10:[4,]}
def dfs(graph,stack,node):
    stack.append(node)
    for i in graph[node]:
        if i not in stack:
            dfs(graph,stack,i)
    return stack
def all_paths(graph,start,end,stack):
    stack.append(start)
    if start==end:
        print(stack)
        stack.pop()
        return
    for i in graph[start]:
        if i not in stack:
            all_paths(graph,i,end,stack)
    stack.pop()
def bfs(q,visited):
    while q:
        res=q.pop(0)
        visited.append(res)
        for i in graph[res]:
            if i not in q and i not in visited:
                q.append(i)
    return visited
print("Bfs is:",bfs([5],[]))
print("Dfs is:",dfs(graph,[],5))
print("All possible paths are:")
all_paths(graph,5,2,[])