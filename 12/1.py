edges = []

def find_neighbors(n):
  neighbors = []
  for e in edges:
    a, b = e
    if a == n:
      neighbors.append(b)
    elif b == n:
      neighbors.append(a)
  return neighbors

def add_edge(a, b):
  edge = (a, b)

  if edge not in edges:
    edges.append(edge)

def count_paths(s, t, path):

  if s == t:
    return 1

  if s in path and s.islower():
    return 0
  
  path.append(s)
  neighbors = find_neighbors(s)
  c = 0
  for n in neighbors:
    n_path = path.copy()
    c += count_paths(n, t, n_path)
  return c


if __name__ == "__main__":
  file = open("input.txt", "r")

  for l in file:
    l = l.rstrip()
    l = l.split("-")
    add_edge(l[0], l[1])

  path = []
  no_paths = count_paths("start", "end", path)

  print(no_paths)