class School:
  def __init__(self):
    file = open("input.txt")
    self.fish = {}
    for i in range(9):
      self.fish[i] = 0

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
    for key in age_groups:
      temp = self.fish[key]
      if key  == 0:
        self.fish[8] = temp
        self.fish[6] += temp

      self.fish[key]= prev
      prev = temp

  @property
  def no_fish(self):
    counter = 0
    for n in self.fish.values():
      counter += n
    return counter
        



school = School()
print(school.no_fish)
for i in range(256):
  school.next_day()

print(school.no_fish)
