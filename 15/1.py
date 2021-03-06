from queue import PriorityQueue

def in_bounds(pos, grid):
  x, y = pos
  return x >= 0 and x < len(grid) and y >= 0 and y < len(grid)

def add_to_dict(pos, risk, D):
  if not pos in D:
    D[pos] = risk
  else:
    if D[pos] > risk:
      D[pos] = risk
    else:
      return False
  return True
    
def dijkstra(start, target, grid):
  visited = set()
  queue = PriorityQueue()
  queue.put((0, start))
  risk_dict = {}
  
  while not queue.empty():
    current = queue.get()
    risk, (x, y) = current
    visited.add(current)

    neighbors = [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]
    for n in neighbors:
      if n not in visited and in_bounds(n, grid):
        x1, y1 = n
        n_risk = grid[x1][y1] + risk
        if n == target:
          return n_risk

        if add_to_dict(n, n_risk, risk_dict):
          queue.put((n_risk, n))
  

if __name__ == "__main__":
  file = open("input.txt", "r")
  
  grid = []
  for line in file:
    line = line.rstrip()
    line = [int(c) for c in line]
    grid.append(line)

lowest_risk = dijkstra((0, 0), (99, 99), grid)
print(lowest_risk)