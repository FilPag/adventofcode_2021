def octo_tick(x, y, grid):

  if x >= 10 or x < 0 or y >= 10 or y < 0:
    return 0

  energy, flashed = grid[x][y]

  if flashed:
    return 0
  
  energy += 1

  counter = 0
  if energy > 9:
    counter += 1
    grid[x][y] = (energy, True)
    
    for x_diff in range(-1, 2):
      for y_diff in range(-1, 2):
        counter += octo_tick(x + x_diff, y + y_diff, grid)

  else:
    grid[x][y] = (energy, False)
  return counter

def tick(grid):
  tick_counter = 0
  for i in range(10):
    for j in range(10):
      tick_counter += octo_tick(i, j, grid)

  for i in range(10):
    for j in range(10):
      _ , flashed = grid[i][j]
      if flashed:
        grid[i][j] = (0, False)

  return tick_counter



if __name__ == "__main__":
  file = open("input.txt")
  grid = []

  for line in file:
    line = line.rstrip()
    line = [(int(i), False) for i in line]
    grid.append(line)
  
  total_counter = 0
  for day in range(100):
    total_counter += tick(grid)

  print(total_counter)