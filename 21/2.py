import os

def move(pos, steps):
  pos = (pos + steps) % 10
  if pos == 0:
    pos = 10
  return pos

def calc_outcomes(positions, scores, turn):
  start_pos = positions[turn]
  outcomes = []
  new_scores = []
  possible_rolls = [1, 2, 3]
  rolls = [(x, y, z) for x in possible_rolls for y in possible_rolls for z in [1,2,3]]

  for r in rolls:
    new_pos = move(start_pos, sum(r))
    if turn == 0:
      outcome = (new_pos, positions[1])
      score = (scores[0] + new_pos, scores[1])
    else:
      outcome = (positions[0], new_pos)
      score = (scores[0], scores[1] + new_pos)
    outcomes.append(outcome)
    new_scores.append(score)
  return outcomes, new_scores


def count_max_wins(positions, scores, turn, dp_dict):
  gamestate = (positions, scores, turn)

  if gamestate in dp_dict:
    return dp_dict[gamestate]

  if scores[0] > 20:
    return (1, 0)
  if scores[1] > 20:
    return (0, 1)

  outcomes, new_scores = calc_outcomes(positions, scores, turn)
  p1_wins = 0
  p2_wins = 0
  turn = (turn + 1) % 2
  for o, s in zip(outcomes, new_scores):
    w1, w2 = count_max_wins(o, s, turn, dp_dict)
    p1_wins += w1
    p2_wins += w2

  wins = (p1_wins, p2_wins)
  dp_dict[gamestate] = wins
  return wins

if __name__ == "__main__":
  directory = os.path.dirname(__file__)
  file = open(directory + "\input.txt",)
  starts = []
  for line in file:
    line = line.rstrip()
    pos = int(line.split(" ")[-1])
    starts.append(pos)
  file.close()

  dp_dict = {}
  starts = tuple(starts)
  wins = count_max_wins(starts, (0, 0), 0, dp_dict)
  print(max(wins))
  