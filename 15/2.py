from queue import PriorityQueue

def calc_risk(pos, grid):
  x, y = pos
  x_sector = x // 100
  y_sector = y // 100

  x_red = x % 100
  y_red = y % 100

  risk = grid[x_red][y_red]
  risk = (risk + x_sector + y_sector) % 9
  if risk == 0:
    risk = 9
  return risk

def in_bounds(pos, grid, multiplier = 1):
  x, y = pos
  return x >= 0 and x < multiplier * len(grid) and y >= 0 and y < multiplier * len(grid)

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
      if n not in visited and in_bounds(n, grid, multiplier = 5):
        n_risk = risk + calc_risk(n, grid)
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

lowest_risk = dijkstra((0, 0), (499, 499), grid)
print(lowest_risk)