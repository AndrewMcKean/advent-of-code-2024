from functools import reduce

# Get data lists & sort them
split_by_dont = open('puzzleInput.txt', 'r').read().split("don't")

valid_strings = []

for string in split_by_dont:
  dos = string.split('do')

  for i in range(len(dos)):
    if i != 0:
      valid_strings.append(dos[i])

data_string = ""

for string in valid_strings:
  data_string += string

data = data_string.split('mul')


OPEN_BRACKET = ['(']
NUMBERS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
NUMBERS_WITH_COMMA = NUMBERS + [',']
CLOSE_BRACKET = [')']  

total = 0

for string in data:
  valid_chars = OPEN_BRACKET
  comma_seen = False
  num_one = ''
  num_two = ''

  for i in range(len(string)):
    char = string[i]

    if char in valid_chars:
        if char == '(':
          valid_chars = NUMBERS

        if char in NUMBERS:
          if comma_seen:
            valid_chars = NUMBERS + CLOSE_BRACKET
            num_two += char
          else:
            valid_chars = NUMBERS_WITH_COMMA
            num_one += char
          
        if char == ',':
          valid_chars = NUMBERS
          comma_seen = True

        if char == ')':
          if comma_seen and ((0 < len(num_one) < 4) and (0 < len(num_two) < 4)):
            total += (int(num_one) * int(num_two))
            break
    else:
      break
            

print(f"The total is {total}")

    