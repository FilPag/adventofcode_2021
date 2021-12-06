class School:
  def __init__(self):
    file = open("input.txt")
    ages = file.readline().rstrip()
    file.close()
    ages = ages.split(",")
    ages = [int(i) for i in ages]
    self.fish = ages

  def next_day(self):
    for i in range(len(self.fish)):
      if self.fish[i] == 0:
        self.fish[i] = 6
        self.fish.append(8)
      else:
        self.fish[i] -= 1
  @property
  def no_fish(self):
    return len(self.fish)
        



school = School()
print(school.no_fish)


for i in range(80):
  school.next_day()

print(school.no_fish)
