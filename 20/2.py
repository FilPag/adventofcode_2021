def process_image(image, enhancement, lit = False):
  new_image = {}
  to_visit = []
  new_image["mid"] = image["mid"]
  to_visit.append(image["mid"])

  while len(to_visit) != 0:
    pos = to_visit.pop(0)
    if pos in new_image:
      continue

    grid = get_grid(pos, image, lit)
    index = get_binary_index(grid)
    new_image[pos] = enhancement[index]

    if index == 0 and not lit:
      continue
    elif index == 511 and lit:
      continue

    diffs = [-1, 0, 1]
    x, y = pos
    for x_diff in diffs:
      for y_diff in diffs:
        n_pos = (x + x_diff, y + y_diff)
        to_visit.append(n_pos)

  return new_image

def get_grid(pos, image, lit):
  x, y = pos
  diffs = [-1, 0, 1]
  grid = []
  void = ""
  if lit:
    void = "#"
  else:
    void = "."

  for x_diff in diffs:
    row = ""
    for y_diff in diffs:
      n_pos = (x + x_diff, y + y_diff)
      if n_pos in image:
        row += image[n_pos]
      else:
          row += void
    grid.append(row)
  return grid

def get_binary_index(grid):
  string = ""
  for row in grid:
    for c in row:
      if c == "#":
        string += "1"
      else:
        string += "0"
  return int(string, base=2)

if __name__ == "__main__":
  file = open("input.txt", "r") 

  enhancement = file.readline().rstrip()
  image = []

  line = file.readline()
  while line != "":
    if line != "\n":
      line = line.rstrip()
      image.append(line)
    line = file.readline()
  file.close()

  img_dict = {}
  for i in range(len(image)):
    for j in range(len(image[i])):
      img_dict[(i, j)] = image[i][j]


  mid = (len(image) + 1) / 2
  mid = int(mid)
  start = (mid, mid)

  image = img_dict
  image["mid"] = start

  for i in range(50):
    lit = i % 2 == 1
    image = process_image(image, enhancement, lit)

  counter = 0
  for c in image.values():
      if c == "#":
        counter += 1
  print(counter)
