def command_on(cmd):
  if cmd == "on":
    return True
  else:
    return False
def get_coords(line):
  line = line.split(",")
  coords = []
  for segment in line:
    segment = segment[2:]
    segment = segment.split("..")
    segment = [int(x) for x in segment]
    coords.append(tuple(segment))
  return tuple(coords)

def check_limits(limits):
  for pair in limits:
    for l in pair:
      if l > 50 or l < -50:
        return False
  return True

def apply(on, limits, active_reactors):
  x, y, z = limits
  for i in range(x[0], x[1] + 1):
    for j in range(y[0], y[1] + 1):
      for k in range(z[0], z[1] + 1):
        if on:
          active_reactors.add((i,j,k))
        else:
          if (i,j,k) in active_reactors:
            active_reactors.remove((i,j,k))

if __name__ == "__main__":
  file = open("input.txt", "r")
  commands = []
  for line in file:
    line = line.rstrip()
    cmd, line = line.split(" ")
    cmd = command_on(cmd)
    coords = get_coords(line)
    commands.append((cmd, coords))
  file.close()  

  active_reactors = set()

  for c in commands:
    on, limits = c
    if check_limits(limits):
      apply(on, limits, active_reactors)
    
  print(len(active_reactors))