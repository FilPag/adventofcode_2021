def fold_left(axis, points):
  max_x = (axis * 2)
  new_points = set()
  for point in points:
    x, y = point
    if x > axis:
      new_x = max_x - x
      #print(f"new: {new_x}")
      point = (new_x, y)
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

  axis = folds[0][1]
  points = fold_left(axis, points)
  print(len(points))