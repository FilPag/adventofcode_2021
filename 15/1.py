def print_matrix(dp_matrix):
  for row in dp_matrix:
    row_s = ""
    for col in row:
      row_s += str(col) + " "
    print(row_s)

def find_min_risk(pos, p_map, dp_matrix):
  x, y = pos
  if pos == (len(p_map) - 1, len(p_map) - 1):
    return 0
  
  if dp_matrix[x][y] is not None:
    return dp_matrix[x][y]
  
  neighbors = [(x, y + 1), (x + 1, y)]
  risks = []
  for i in range(len(neighbors)):
    x1, y1 = neighbors[i]
    if x1 < len(p_map) and y1 < len(p_map):
      neighbor_risk = p_map[x1][y1] + find_min_risk(neighbors[i], p_map, dp_matrix)
      risks.append(neighbor_risk)
  
  lowest_risk = min(risks)
  dp_matrix[x][y] = lowest_risk
  return lowest_risk
  

if __name__ == "__main__":
  file = open("input.txt", "r")
  
  p_map = []
  for line in file:
    line = line.rstrip()
    line = [int(c) for c in line]
    p_map.append(line)
  
  dp_matrix = [[None for _ in range(len(p_map))] for _ in range(len(p_map))]

  risk = find_min_risk((0, 0), p_map, dp_matrix)
  #print_matrix(dp_matrix)
  print(risk)