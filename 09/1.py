file = open("input.txt", "r")

heightmap = []

for line in file:
  line = line.rstrip()
  line = [int(c) for c in line]
  heightmap.append(line)

height = len(heightmap[0])
width = len(heightmap)

def check_neighbors(i, j):
  current = heightmap[i][j]
  h_neighbors = [j + 1, j - 1]
  v_neighbors = [i + 1, i - 1 ]

  lowest = True
  for n in v_neighbors:
    if n >= 0 and n < height:
      lowest = lowest and current < heightmap[n][j]

  for n in h_neighbors:
    if n >= 0 and n < width:
      lowest = lowest and current < heightmap[i][n]
  
  if lowest:
    return 1 + current
  else:
    return 0

total_risk = 0
for i in range(height):
  for j in range(width):
    total_risk += check_neighbors(i, j)

print(total_risk)
