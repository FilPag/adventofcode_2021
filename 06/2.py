class School:
  def __init__(self):
    file = open("input.txt")
    self.fish = [0 for _ in range(9)]

    ages = file.readline().rstrip()
    file.close()
    ages = ages.split(",")
    ages = [int(i) for i in ages]
    for age in ages:
      self.fish[age] += 1

  def next_day(self):
    age_groups = list(range(9))
    age_groups.reverse()
    prev = 0
    for age in age_groups:
      temp = self.fish[age]
      if age == 0:
        self.fish[8] = temp
        self.fish[6] += temp

      self.fish[age]= prev
      prev = temp

  @property
  def no_fish(self):
    counter = 0
    for n in self.fish:
      counter += n
    return counter
        



school = School()
print(f"Day 0: {school.no_fish} fish")
DAYS = 256 
for i in range(DAYS):
  school.next_day()

print(f"Day {DAYS}: {school.no_fish} fish")
