def print_paper(points):
  max_x = max(points, key = lambda p: p[0])[0] + 1
  max_y = max(points, key = lambda p: p[1])[1] + 1

  paper = [[" " for _ in range(max_x)] for _ in range(max_y)]

  for point in points:
    x, y = point
    paper[y][x] = "#"
  
  for row in paper:
    row = "".join(row)
    print(row)

def fold_op(f, points):
  axis = f[0]
  middle = f[1]
  length = (middle * 2)
  new_points = set()

  for point in points:
    x, y = point
    if axis == "x":
      if x > middle:
        new_x = length - x
        point = (new_x, y)
    else:
      if y > middle:
        new_y = length - y
        point = (x, new_y)
    new_points.add(point)

  return new_points

if __name__ == "__main__":
  file = open("input.txt", "r")

  points = set()
  folds = []
  for line in file:
    line = line.rstrip()
    if "," in line:
      line = line.split(",")
      point = (int(line[0]), int(line[1]))
      points.add(point)
    if "fold" in line:
      line = line.split(" ")
      line = line[2].split("=")
      fold = (line[0], int(line[1]))
      folds.append(fold)

  for f in folds:
      points = fold_op(f, points)

  print("=============CODE CALCULATED=============")
  print_paper(points)
  print("=========================================")
  