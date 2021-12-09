file = open("input.txt", "r")

heightmap = []

for line in file:
  line = line.rstrip()
  line = [int(c) for c in line]
  heightmap.append(line)

height = len(heightmap[0])
width = len(heightmap)

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
basin_sizes = []
for i in range(width):
  for j in range(height):
    current = (i, j)
    if current not in visited:
      size = check_basin(current, visited)
      basin_sizes.append(size)

basin_sizes = sorted(basin_sizes)
basin_sizes = basin_sizes[-3:]
prod = basin_sizes[0] * basin_sizes[1] * basin_sizes[2]
print(prod)

