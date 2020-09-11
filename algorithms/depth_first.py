GRAPH = { "A" : ["B", "D", "E"],  "B" : ["A", "C", "D"], "C" : ["B", "G"],
          "D" : ["A", "B", "E", "F"], "E" : ["A", "D"], "F" : ["D"], "G" : ["C"] }

visitedList  = []

def dfs(graph, currentVertex, visited):
    visited.append(currentVertex)
    for vertex in graph[currentVertex]:
        if vertex not in visited:
            dfs(graph, vertex, visited)
        print(visited)
    return visited

traversal = dfs(GRAPH, "A", visitedList)
print("Nodes visited in this order ", traversal)
