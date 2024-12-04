# Get data lists & sort them
data = open('puzzleInput.txt', 'r').read().split("\n")

TARGET = 'XMAS'

total = 0

def canCheckForX(line_index, char_index):
    curr_line_length = len(data[line_index])

    not_on_first = line_index > 0
    not_on_last_char =  char_index < curr_line_length - 1
    not_on_first_char = char_index != 0
    not_on_last = line_index < len(data) - 1

    return not_on_first and not_on_last and not_on_first_char and not_on_last_char

def checkForXMases(line_index, char_index):
    center = data[line_index][char_index]

    top_left = data[line_index-1][char_index-1]
    top_right = data[line_index-1][char_index+1]

    bottom_left = data[line_index+1][char_index-1]
    bottom_right = data[line_index+1][char_index+1]

    first_mas = top_left + center + bottom_right
    second_mas = top_right + center + bottom_left

    if (first_mas == 'MAS' or first_mas == 'SAM') and (second_mas == 'MAS' or second_mas == 'SAM'):
        global total
        total += 1
  
    
for line_index in range(len(data)):
    line = data[line_index]

    for char_index in range(len(data[line_index])):
        char = line[char_index]

        valid_directions = []

        if char == 'A':
            should_check = canCheckForX(line_index, char_index)

            if should_check:
                checkForXMases(line_index, char_index)


print(total)

    