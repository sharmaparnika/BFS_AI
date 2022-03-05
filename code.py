graph = {
    'E':['C','G'],
    'C':['B','D'],
    'G':['H'],
    'B':[],
    'D':['H'],
    'H':[]
}


visited = []
q = []

def Breadth(visited, graph, node):
  visited.append(node)
  q.append(node)

  while q:
    x = q.pop(0)
    print(x, end = " ")

    for adj in graph[x]:
      if adj not in visited:
        visited.append(adj)
        q.append(adj)

print("Breadth First Search")
Breadth(visited, graph, 'E')
