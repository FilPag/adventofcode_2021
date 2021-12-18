def simulate(vx, vy):
  pos = (0, 0)
  max_y = 0
  hit = False
  while not check_past(pos):
    x, y = pos
    if vy == 0:
      max_y = y

    pos = (x + vx, y + vy)
    if vx != 0:
      drag = int((vx / vx) * -1)
      vx += drag
    vy -= 1 
    hit = hit or check_bound(pos)
    
  return max_y, hit

def check_past(pos):
  x, y = pos
  x_bounds = (124, 174)
  y_bounds = (-123, -86)
  return x > x_bounds[1] or y < y_bounds[0]

def check_bound(pos):
  x, y = pos
  x_bounds = (124, 174)
  y_bounds = (-123, -86)

  return x >= x_bounds[0] and x <= x_bounds[1] and y >= y_bounds[0] and y <= y_bounds[1]

if __name__ == "__main__":

  counter = 0
  for i in range(175):
    for j in range(-123, 124):
      max_y, hit = simulate(i, j)
      if hit:
        counter += 1
  print(counter)

