GRAPH = {
    "A": {"colour": "White", "neighbours": ["B", "D", "E"]},
    "B": {"colour": "White", "neighbours": ["A", "D", "C"]},
    "C": {"colour": "White", "neighbours": ["B", "G"]},
    "D": {"colour": "White", "neighbours": ["A", "B", "E", "F"]},
    "E": {"colour": "White", "neighbours": ["A", "D"]},
    "F": {"colour": "White", "neighbours": ["D"]},
    "G": {"colour": "White", "neighbours": ["C"]},

}

def bfs(graph, vertex):
    queue = []
    visited = []
    queue.append(vertex)
    while len(queue) > 0:
        currentNode = queue.pop()
        currentNode = "Black"
        visited.append(currentNode)

        for neighbour in currentNode:
            if neighbour == "White":
                queue.append(neighbour)
                neighbour = "Grey"

    return visited


visited = bfs(GRAPH, "A")
print("List of nodes visited ", visited)