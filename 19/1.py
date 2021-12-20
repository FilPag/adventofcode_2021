import numpy as np
from numpy.linalg import matrix_power

rot90_x = np.array([[1, 0, 0], [0, 0, -1], [0, 1, 0]])
rot90_y = np.array([[0, 0, 1], [0, 1, 0], [-1, 0, 0]])
rot90_z = np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]])
rotations= [rot1@rot2
        for rot1 in [matrix_power(rot90_x, i) for i in range(4)]
        for rot2 in [matrix_power(rot90_y, i) for i in range(4)] + [matrix_power(rot90_z, i) for i in [1, 3]]]

class Scanner:
  def __init__(self, points, id_no):
    self.id = id_no
    self.points = points
    self.no_beacons = len(points)
    self.distances = self.__calc_distances()
    if id_no == 0:
      self.location = (0, 0, 0)
  
  def __str__(self):
    return "Scanner: " + str(self.id)
  
  @property
  def pos(self):
    return self.location

  def __calc_distances(self):
    distances = np.zeros((self.no_beacons, self.no_beacons))
    for i in range(self.no_beacons):
      for j in range(self.no_beacons):
        a = self.points[i]
        b = self.points[j]
        distances[i][j] = beacon_distance(a, b)
    return distances

  def get_overlap(self, other: 'Scanner'):
    overlapping = {}
    for i in range(self.no_beacons):
      for j in range(other.no_beacons):
        if i in overlapping:
          break
        if check_beacon_overlap(self.distances[i], other.distances[j]):
          overlapping[i] = j

    if len(overlapping) >= 12:
      return overlapping
  
  def calc_transform(self, other, overlap):
    pairs = [(self.points[p[0]], other.points[p[1]]) for p in overlap.items()]
    scanner_rotation = None
    for rot in rotations:
      if test_rotation(rot, pairs):
        scanner_rotation = rot
        break
    scanner_offset = pairs[0][0] - (pairs[0][1] @ scanner_rotation)
    return scanner_rotation, scanner_offset

  def transform(self, rotation, offset):
    self.location = offset
    for i in range(self.no_beacons):
      self.points[i] = (self.points[i] @ rotation) + offset

  def get_beacon_set(self):
    beacons = set()
    for beacon in self.points:
      beacons.add(tuple(beacon))
    return beacons
    
def test_rotation(rotation, pairs):
  prev = pairs[0][0] - (pairs[0][1] @ rotation) #Matrix mult
  for (p1, p2) in pairs[1:]:
    res = p1 - (p2 @ rotation)
    if not np.array_equal(prev, res):
      return False
    prev = res
  return True

def beacon_distance(a, b):
  return np.linalg.norm(a - b)

def check_beacon_overlap(b1, b2):
  overlap = np.intersect1d(b1, b2)
  return overlap.size >= 12
  
def offset(l, off):
  new_l = l.copy()
  for i in range(len(l)):
    new_l[i - off] = new_l[l]
  return new_l

def align(aligned, target):
  for a in aligned:
    overlap = a.get_overlap(target)
    if overlap:
      rotation, offset = a.calc_transform(target, overlap)
      target.transform(rotation, offset)
      return True
  return False

def scanner_distance(s1, s2):
  x1, y1, z1 = s1.pos
  x2, y2, z2 = s2.pos
  return abs(x1 - x2) + abs(y1 - y2) + abs(z1 - z2)

if __name__ == "__main__":
  file = open("input.txt", "r")

  scanners = []
  id_counter = 0
  while file.readline() != "":
    points = []
    line = file.readline().rstrip()
    while line != "":
      line = line.split(",")
      line = [int(x) for x in line]
      line = np.asarray(line)
      points.append(line) 
      line = file.readline().rstrip()
    
    points = np.asarray(points)
    scanners.append(Scanner(points,id_counter))
    id_counter += 1
  file.close()

  aligned = [scanners[0]]
  remaining = scanners[1:]

  while len(remaining) != 0:
    s = remaining.pop(0)
    if align(aligned, s):
      aligned.append(s)
    else:
      remaining.append(s)

  no_beacons = len({tuple(b) for s in aligned for b in s.points})
  print("Number of beacons: " + str(no_beacons))

  max_dist = 0
  for i in range(len(scanners)):
    for j in range(len(scanners)):
      dist = scanner_distance(scanners[i], scanners[j])
      if dist > max_dist  :
        max_dist = dist
  
  print("Max distance: " + str(max_dist))

