'''
https://adventofcode.com/2024/day/1

Puzzle Input: Two unsorted list of nums
Puzzle Ouput: Int, the summed distance between the smallest -> largest nums in both lists. i.e first[0] - second[0] + first[1] - second[1] etc.
'''
import functools

# Get data lists & sort them
data = open('puzzleInput.txt', 'r').read().split('\n')

first = []
second = []

for i in range(len(data)):
  nums = data[i].split('   ')
  first.append(int(nums[0]))
  second.append(int(nums[1]))

first.sort()
second.sort()

# Define function for getting the difference
def get_difference(index):
  temp = [first[index], second[index]]

  temp.sort()

  return temp[1] - temp[0]

# Get the sum of the differences
better_sum = functools.reduce(lambda acc, index_value_pair: acc + get_difference(index_value_pair[0]), enumerate(first), 0)


print(f"The total is: {better_sum}")

'''
Simple enough.
Improved the solution a bit.
Reduce is neat in python, using enumerate allows me to get an index like I would in JS. Leave the 0 off the end tripped me up a little. 
Seems you need to initalize the acc with 0 otherwise the reduce will think you want to reduce to a tuple.
'''

