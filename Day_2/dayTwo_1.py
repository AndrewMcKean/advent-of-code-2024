'''
https://adventofcode.com/2024/day/2

Puzzle Input: Line seperated, space seperated lists of nums
Puzzle Ouput: Int, the number of valid sequences of numbers. A valid sequence is either increasing or decreasing, and each number must not differ from it's neighbour by more than 3, or less than 1.
'''
from functools import reduce

# Get data lists & sort them
data = open('puzzleInput.txt', 'r').read().split('\n')

def check_if_safe(curr, next, ascending):
  if ascending:
    # Check direction
    if curr >= next:
      return False
    
    return 0 < (next - curr) < 4
  
  else:
    if curr <= next:
      return False
    
    return 0 < (curr - next) < 4
    
def check_list(num_list):
    is_safe = False
    is_ascending = None

    for i in range(len(num_list) - 1):
      curr = num_list[i]
      next = num_list[i + 1]

      if is_ascending is None:
        is_ascending = curr < next

      is_safe = check_if_safe(curr, next, ascending=is_ascending)

      if not is_safe:
        break

    return is_safe

num_safe = 0

for line_index in range(len(data)):
  # Convert list to nums
  num_list = list(map(lambda x: int(x), data[line_index].split(' ')))

  is_safe = check_list(num_list)
  
  if is_safe:
    num_safe += 1
    

print(f"There are {num_safe} safe reports")


'''
My head logic was right from the start, but I made a bunch of silly mistakes with the loop.
This took way too long. Should probably do these at the start of the day instead of the end lol.
'''

