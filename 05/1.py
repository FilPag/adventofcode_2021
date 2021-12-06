class Grid:
  def __init__(self):
    self.grid = {}

  def _add_to_grid(self, x:int, y:int):
    assert(x >= 0 and y >= 0)
    key = str(x) + "," + str(y)
    if key in self.grid:
      self.grid[key] += 1
    else:
      self.grid[key] = 1

  def add_line(self, start, stop):
    x1, y1 = start
    x2, y2 = stop

    if x1 == x2:
      dy = int(abs(y2 - y1) + 1)
      sign = int(abs(y2 - y1) / (y2 - y1))

      for y in range(int(dy)):
        self._add_to_grid(x1, y1 + sign * y)

    elif y1 == y2:
      dx = int(abs(x2 - x1) + 1)
      sign = int(abs(x2 - x1) / (x2 - x1))

      for x in range(int(dx)):
        self._add_to_grid(x1 + sign * x , y1)

  def get_no_crossings(self):
    counter = 0
    #print(len(self.grid.values()))
    for entry in self.grid.values():
      if entry > 1:
        counter += 1
    return counter

file = open("./input.txt", "r")

def string_to_point(string):
  x, y = string.split(",")
  return (int(x), int(y))

lines = []
grid = Grid()

for line in file:
  line = line.rstrip()
  start_string, _ , stop_string = line.split(" ")
  start = string_to_point(start_string)
  stop = string_to_point(stop_string)
  grid.add_line(start, stop)

print(grid.get_no_crossings())
file.close()
