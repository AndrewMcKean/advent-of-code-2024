'''
https://adventofcode.com/2024/day/2

Puzzle Input: Line seperated, space seperated lists of nums
Puzzle Ouput: Int, the number of valid sequences of numbers. A valid sequence is either increasing or decreasing, and each number must not differ from it's neighbour by more than 3, or less than 1. If removing one number from an invalid sequence makes it valid, it is deemed valid.
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

  variations = []

  is_safe = check_list(num_list)
  
  if is_safe:
    num_safe += 1
    continue
    
  # If it's not safe, get all variations of the list minus one element
  for i in range(len(num_list)):
    copy = num_list.copy()
    copy.pop(i)

    variations.append(copy)

  variation_is_safe = False
  
  for variation in variations:
    safe = check_list(variation)

    if safe:
      variation_is_safe = True
      break
  
  if variation_is_safe:
    num_safe += 1


print(f"There are {num_safe} safe reports")


'''
This also took way too long. I was very close with my 'clever' implementation, and was only one off the right answer. 
Ended up just brute forcing it and by the looks of reddit so did most other people.
'''

