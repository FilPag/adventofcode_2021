import os
def get_sign(cmd):
  if cmd == "on":
    return 1
  else:
    return -1

def get_coords(line):
  line = line.split(",")
  coords = []
  for segment in line:
    segment = segment[2:]
    segment = segment.split("..")
    segment = [int(x) for x in segment]
    segment = sorted(segment)
    coords.append(tuple(segment))
  return tuple(coords)

def check_overlap(c1, c2):
  _, q1 = c1
  _, q2 = c2
  
  (x, x1), (y, y1), (z, z1) = q1
  (a, a1), (b, b1), (c, c1) = q2

  if not (x <= a1 and x1 >= a):
    return False
  if not (y <= b1 and y1 >= b):
    return False
  if not (z <= c1 and z1 >= c):
    return False
   
  return True

def get_overlap(c1, c2):
  s1, q1 = c1
  s2, q2 = c2

  (x, x1), (y, y1), (z, z1) = q1
  (a, a1), (b, b1), (c, c1) = q2

  ox = max(x, a)
  ox1 = min(x1, a1)
  oy = max(y, b)
  oy1 = min(y1, b1)
  oz = max(z, c)
  oz1 = min(z1, c1)
  
  sign = s1 * s2

  if s1 == s2:
    sign = -s1
  elif s1 == 1 and s2 == -1:
    sign = 1

  return sign,((ox, ox1), (oy, oy1), (oz, oz1))

def get_vol(q):
  (x, x1), (y, y1), (z, z1) = q
  dx = abs(x1 - x + 1)
  dy = abs(y1 - y + 1)
  dz = abs(z1 - z + 1)

  return dx * dy * dz

if __name__ == "__main__":
  directory = os.path.dirname(__file__)
  file = open(directory + "/input.txt",)
  commands = []
  for line in file:
    line = line.rstrip()
    cmd, line = line.split(" ")
    sign = get_sign(cmd)
    coords = get_coords(line)
    commands.append((sign, coords))
  file.close()  

  cuboids = []
  for i, c in enumerate(commands):
    intersect_area = 0
    overlaps = []
    for cuboid in cuboids:
      if check_overlap(c, cuboid):
        o = get_overlap(c, cuboid)
        overlaps.append(o)
    for o in overlaps:
      cuboids.append(o)
    
    if c[0] == 1:
      cuboids.append(c)


  tot_vol= 0
  for sign, c in cuboids:
    tot_vol += get_vol(c) * sign
  print(tot_vol)
