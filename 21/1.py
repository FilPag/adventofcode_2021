import os

class Die:
  def __init__(self):
    self.next_roll = 1
    self.rolls = 0

  def roll_and_sum(self, rolls):
    s = 0
    for _ in range(rolls):
      self.rolls += 1
      s += self.next_roll
      self.next_roll += 1

      if self.next_roll > 100:
        self.next_roll = 1
    return s

class Player:
  def __init__ (self, start):
    self.pos = start
    self.score = 0
  
  def move(self, steps):
    self.pos = (self.pos + steps) % 10
    if self.pos == 0:
      self.pos = 10
    self.score += self.pos

def checkwin(players):
  for i, player in enumerate(players):
    if player.score >= 1000:
      return i

if __name__ == "__main__":
  directory = os.path.dirname(__file__)
  file = open(directory + "\input.txt",)
  players = []
  for line in file:
    line = line.rstrip()
    pos = int(line.split(" ")[-1])
    players.append(Player(pos))
  file.close()

  die = Die()
  winner = None
  turn = 0

  while winner is None:
    roll = die.roll_and_sum(3)
    players[turn].move(roll)
    winner = checkwin(players)
    turn = (turn + 1) % 2

  if winner == 0:
    loser_score = players[1].score
  else:    
    loser_score = players[0].score
  
  print(loser_score * die.rolls)
  