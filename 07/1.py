import numpy as np
file = open("input.txt")
data = file.readline().rstrip()
file.close()

data = data.split(",")
positions = [int(i) for i in data]
positions = np.array(positions)
#s = sum(positions)
#s = s / len(positions)
med = np.median(positions)

fuel = 0
for pos in positions:
  fuel += abs(med - pos)

print(fuel)