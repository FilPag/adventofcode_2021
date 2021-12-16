def read_literal(sequence):
  value , sequence= trim_n_bits(sequence, 5)
  leading = value[0]
  value = value[1:]

  counter = 12
  while leading != "0":
    counter += 5

    next_group, sequence = trim_n_bits(sequence, 5)
    leading = next_group[0]
    next_group = next_group[1:]
    value += next_group
  
  remainder = counter % 4
  #_, sequence = trim_n_bits(sequence, remainder)
  return int(value, base=2), sequence


def trim_n_bits(sequence, n):
  trim =  sequence[:n]
  sequence =  sequence[n:]

  return trim, sequence

def read_header(sequence):
  version, sequence = trim_n_bits(sequence, 3)
  type_id, sequence = trim_n_bits(sequence, 3)
  
  version = int(version, base=2)
  type_id= int(type_id, base=2)

  return version, type_id, sequence

def expand_char(c):
  int_value = int(c, base=16)
  string = str(bin(int_value))[2:]
  return string.zfill(4)

def process_packet(sequence):
  v, tid, sequence =  read_header(sequence)

  if tid == 4:
    value, sequence = read_literal(sequence)
  else:
    mode, sequence = trim_n_bits(sequence, 1)

    if mode == '0':
      no_bits, sequence = trim_n_bits(sequence, 15)
      no_bits = int(no_bits, base=2)
      subs, sequence = trim_n_bits(sequence, no_bits)
      while subs != "":
        sub_v, subs = process_packet(subs)
        v += sub_v
    else:
      no_packets, sequence = trim_n_bits(sequence, 11)
      no_packets = int(no_packets, base=2)
      for _ in range(no_packets):
        sub_v, sequence = process_packet(sequence)
        v += sub_v
  return v, sequence


if __name__ == "__main__":
  file = open("input.txt", "r")

  sequence = ""
  line = file.readline().rstrip()
  for c in line:
    sequence += expand_char(c)
  
  #sequence = "110100101111111000101000"
  #sequence = "00111000000000000110111101000101001010010001001000000000"
  #sequence = "00111000000000000110111101000101001010010001001000000000"
  tot_version = process_packet(sequence)
  print(tot_version)
  file.close()