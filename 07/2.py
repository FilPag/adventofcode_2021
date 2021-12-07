import numpy as np
file = open("input.txt")
data = file.readline().rstrip()
file.close()

def calc_cost(pos, target):
  d = int(abs(pos - target))
  return int((d*(d + 1) / 2))

data = data.split(",")
positions = [int(i) for i in data]
mean = sum(positions) / len(positions)
mean = int(mean)
fuel = 0
for pos in positions:
  fuel += calc_cost(pos, mean)

print(fuel)