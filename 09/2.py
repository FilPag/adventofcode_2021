file = open("input.txt", "r")

heightmap = []

for line in file:
  line = line.rstrip()
  line = [int(c) for c in line]
  heightmap.append(line)

height = len(heightmap[0])
width = len(heightmap)

def check_lowpoint(position):
  x, y = position
  current = heightmap[x][y]
  y_neighbors = [x + 1, x - 1 ]
  x_neighbors = [y + 1, y - 1]

  lowest = True
  for n in x_neighbors:
    if n >= 0 and n < width:
      lowest = lowest and current < heightmap[n][j]

  for n in y_neighbors:
    if n >= 0 and n < height:
      lowest = lowest and current < heightmap[i][n]

  return lowest

def check_basin(position, visited):
  x, y = position
  visited.append(position)

  if x < 0 or x >= width or y < 0 or y >= height:
    return 0

  if heightmap[x][y] == 9:
    return 0

  size = 0
  neighbors = [(x, y - 1), (x, y + 1),(x - 1, y),(x + 1, y)]
  
  for n in neighbors:
    if n not in visited:
      size += check_basin(n, visited)

  return 1 + size

visited = []
lowpoints = []
basin_sizes = []
for i in range(width):
  for j in range(height):
    current = (i, j)
    if check_lowpoint(current):
      lowpoints.append(current)

for point in lowpoints:
    size = check_basin(point, visited)
    basin_sizes.append(size)


basin_sizes = sorted(basin_sizes)
basin_sizes = basin_sizes[-3:]
prod = basin_sizes[0] * basin_sizes[1] * basin_sizes[2]
print(prod)

