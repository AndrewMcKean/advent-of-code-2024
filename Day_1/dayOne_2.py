'''
https://adventofcode.com/2024/day/1

Puzzle input: Two lists of unsorted nums
Puzzle output: Int representing the similarity between the two lists

Puzzle desc: Figure out the similarity score as so.
Add up each number of the first list after multiplying each element by the number of times it appears in the right list.

'''
import functools

data = open('puzzleInput.txt', 'r').read().split('\n')

# Build lists
first = []
second = []

for i in range(len(data)):
  nums = data[i].split('   ')
  first.append(int(nums[0]))
  second.append(int(nums[1]))

# Build list of similarity scores
counts = []

for i in range(len(first)):
  counts.append(first[i] * second.count(first[i]))

# Get total similarity score
total = functools.reduce(lambda acc, value: acc + value, counts)


print(f"The total is: {total}")

'''
Again, easy enough. Slightly better solution I think here, than in puzzle 1.
'''




