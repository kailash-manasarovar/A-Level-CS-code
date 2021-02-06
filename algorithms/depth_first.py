graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}

visitedList  = []

def dfs(visited, graph, node):
    visited.append(node)
    for edge in graph[node]:
        if edge not in visited:
            dfs(visited, graph, edge)
        print(visited)
    return visited

traversal = dfs(visitedList, graph, "A")
print("Nodes visited in this order ", traversal)
