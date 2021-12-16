def add_to_dict(pos, risk, D):
  if not pos in D:
    D[pos] = risk
  else:
    if D[pos] > risk:
      D[pos] = risk
    else:
      return False
  return True
    
from queue import PriorityQueue
def dijkstra(start, target, grid):
  visited = set()
  queue = PriorityQueue()
  queue.put((0, start))
  D = {}
  
  while not queue.empty():
    current = queue.get()
    risk, (x, y) = current
    visited.add(current)

    neighbors = [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]
    for n in neighbors:
      x1, y1 = n
      if n in visited:
        continue
      if x1 >= 0 and x1 < 100 and y1 >= 0 and y1 < 100:
        n_risk = grid[x1][y1] + risk
        if n == target:
          return n_risk
        if add_to_dict(n, n_risk, D):
          queue.put((n_risk, n))
  

if __name__ == "__main__":
  file = open("input.txt", "r")
  
  grid = []
  for line in file:
    line = line.rstrip()
    line = [int(c) for c in line]
    grid.append(line)

queue = PriorityQueue()
lowest_risk = dijkstra((0, 0), (99, 99), grid)
print(lowest_risk)