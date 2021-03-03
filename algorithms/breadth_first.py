# graph = {
#   'A' : ['B','C'],
#   'B' : ['D', 'E'],
#   'C' : ['F'],
#   'D' : [],
#   'E' : ['F'],
#   'F' : []
# }
#
# graph_2d_list = [["A", "B", "C"],
#                  ["B", "D", "E"],
#                  ["C", "F", ""],
#                  ["D", "",  ""],
#                  ["E", "F", ""],
#                  ["F", "",  ""]]
# # #
# visited = [] # List to keep track of visited nodes.
# queue = []   # Initialize a queue
# #
# def bfs(visited, graph, node):
#   visited.append(node)
#   queue.append(node)
#
#   while queue:
#     s = queue.pop(0)
#     print (s, end = " ")
#
#     for neighbour in graph[s]:
#       if neighbour not in visited:
#         visited.append(neighbour)
#         queue.append(neighbour)
#
#
# bfs(visited, graph, "A")
# RESULT = A B C D E F

import data_structures.queue

big_graph = [['A', 'B', 'C'], ['B', 'D', 'E'], ['C', 'F'], ['D'], ['E', 'F'], ['F']]
visited = []  # List to keep track of visited nodes.
#queue = []  # Initialize a queue
queue = data_structures.queue.Queue()
#print(queue)
## etc...

def bfs_lists(visited, graphs, node):
    visited.append(node)
    queue.enqueue(node)
    print(queue)

    # while queue:
    #     s = queue.dequeue()
    #     print(s, end=" ")
    #
    #     for graph in graphs:
    #         for node in graph:
    #             if node not in visited:
    #                 #print("Appending ", node)
    #                 visited.append(node)
    #                 queue.enqueue(node)

print(big_graph[0][0])
bfs_lists(visited, big_graph, big_graph[0][0])
# RESULT = A F E D C B  ??