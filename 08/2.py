def add_char_count(source, target, mapping):
  for c in source:
    for c2 in target:
      mapping[c][c2] += 1

def process_signal_base(signal,mapping):
  
  match len(signal):
    case 2:
      mapping[1] = signal
    case 3:
      mapping[7] = signal
    case 4:
      mapping[4] = signal
    case 7:
      mapping[8] = signal

def get_overlap(s1, s2):
  return [c for c in s1 if c in s2]

def process_signal_rest(signal, mapping):

  print(mapping[4] in signal)
  print(signal)
  if len(signal) == 5:
    if mapping[1] in signal:
      mapping[3] = signal
    elif len(get_overlap(signal, mapping[4])) == 3:
      mapping[5] == signal
    else:
      mapping[2] == signal
  elif len(signal) == 6:
    if mapping[4] in signal:
      mapping[9] == signal
    elif len(get_overlap(signal, mapping[1])) == 2:
      mapping[0] == signal
    else:
      mapping[6] = signal
      
    
def decode_signal(signal, mapping):
  for part in signal:
    process_signal_base(part, mapping)

  for part in signal:
    process_signal_rest(part, mapping)

def get_encoding(mapping):
  print(mapping)


  
file = open("input.txt", "r")

signals = []
outputs = []

for line in file:
  line = line.rstrip()
  line = line.split(" | ")

  signal = line[0]
  output = line[1]

  signal = signal.split(" ")
  output = output.split(" ")

  signals.append(signal)
  outputs.append(output)


#total = signals + outputs
mapping = ["" for _ in range(10)]
decode_signal(signals[0], mapping)
get_encoding(mapping)

