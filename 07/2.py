import numpy as np
file = open("input.txt")
data = file.readline().rstrip()
file.close()

def calc_cost(pos, target):
  d = int(abs(pos - target))
  return (d*(d + 1) / 2)

data = data.split(",")
positions = [int(i) for i in data]
m = max(positions)
costs = []
for x in range(m + 1):
  fuel = 0
  for pos in positions:
    fuel += calc_cost(pos, x)
  costs.append(fuel)

res = int(min(costs))
print(res)