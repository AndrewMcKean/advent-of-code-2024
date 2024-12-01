'''
Puzzle Input: Two unsorted list of nums
Puzzle Ouput: Int, the summed distance between the smallest -> largest nums in both lists. i.e first[0] - second[0] + first[1] - second[1] etc.
'''

data = open('puzzleInput.txt', 'r').read().split('\n')

first = []
second = []

for i in range(len(data)):
  nums = data[i].split('   ')
  first.append(int(nums[0]))
  second.append(int(nums[1]))

first.sort()
second.sort()

differences = []

for i in range(len(first)):
  temp = [first[i], second[i]]
  
  temp.sort()

  print(temp)
  
  differences.append(int(temp[1]) - int(temp[0]))


sum = 0

for i in range(len(differences)):
  sum += differences[i]

print(f"The total is: {sum}")


'''
Simple enough.
Inefficient solution though.
'''

