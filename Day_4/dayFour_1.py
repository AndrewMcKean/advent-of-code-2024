# Get data lists & sort them
data = open('puzzleInput.txt', 'r').read().split("\n")

TARGET = 'XMAS'

total = 0

def getValidDirections(line_index, char_index):
    curr_line_length = len(data[line_index])

    directions = []

    can_go_north = line_index >= 3
    can_go_east = curr_line_length > char_index + 3 
    can_go_west = char_index - 3 >= 0
    can_go_south = line_index + 3 < len(data)

    if can_go_north:
        directions.append('n')
    if can_go_east:
        directions.append('e')
    if can_go_west:
      directions.append('w')
    if can_go_south:
        directions.append('s')

    if can_go_north and can_go_east:
        directions.append('ne')
    
    if can_go_north and can_go_west:
        directions.append('nw')
    
    if can_go_south and can_go_east:
        directions.append('se')
    
    if can_go_south and can_go_west:
        directions.append('sw')
    
    return directions
        
def checkNorth(line_index, char_index):
    first_char = data[line_index][char_index]
    second_char = data[line_index-1][char_index]
    third_char = data[line_index-2][char_index]
    fourth_char = data[line_index-3][char_index]

    test_string = first_char + second_char + third_char + fourth_char

    if test_string == TARGET:
        global total
        total += 1

def checkEast(line_index, char_index):
    first_char = data[line_index][char_index]
    second_char = data[line_index][char_index+1]
    third_char = data[line_index][char_index+2]
    fourth_char = data[line_index][char_index+3]

    test_string = first_char + second_char + third_char + fourth_char

    if test_string == TARGET:
        global total
        total += 1

def checkSouth(line_index, char_index):
    first_char = data[line_index][char_index]
    second_char = data[line_index+1][char_index]
    third_char = data[line_index+2][char_index]
    fourth_char = data[line_index+3][char_index]

    test_string = first_char + second_char + third_char + fourth_char

    if test_string == TARGET:
        global total
        total += 1

def checkWest(line_index, char_index):
    first_char = data[line_index][char_index]
    second_char = data[line_index][char_index-1]
    third_char = data[line_index][char_index-2]
    fourth_char = data[line_index][char_index-3]

    test_string = first_char + second_char + third_char + fourth_char

    if test_string == TARGET:
        global total
        total += 1

def checkNorthEast(line_index, char_index):
    first_char = data[line_index][char_index]
    second_char = data[line_index-1][char_index+1]
    third_char = data[line_index-2][char_index+2]
    fourth_char = data[line_index-3][char_index+3]

    test_string = first_char + second_char + third_char + fourth_char

    if test_string == TARGET:
        global total
        total += 1

def checkNorthWest(line_index, char_index):
    first_char = data[line_index][char_index]
    second_char = data[line_index-1][char_index-1]
    third_char = data[line_index-2][char_index-2]
    fourth_char = data[line_index-3][char_index-3]

    test_string = first_char + second_char + third_char + fourth_char

    if test_string == TARGET:
        global total
        total += 1

def checkSouthEast(line_index, char_index):
    first_char = data[line_index][char_index]
    second_char = data[line_index+1][char_index+1]
    third_char = data[line_index+2][char_index+2]
    fourth_char = data[line_index+3][char_index+3]

    test_string = first_char + second_char + third_char + fourth_char

    if test_string == TARGET:
        global total
        total += 1

def checkSouthWest(line_index, char_index):
    first_char = data[line_index][char_index]
    second_char = data[line_index+1][char_index-1]
    third_char = data[line_index+2][char_index-2]
    fourth_char = data[line_index+3][char_index-3]

    test_string = first_char + second_char + third_char + fourth_char

    if test_string == TARGET:
        global total
        total += 1
  
    
for line_index in range(len(data)):
    line = data[line_index]

    for char_index in range(len(data[line_index])):
        char = line[char_index]

        valid_directions = []

        if char == 'X':
            valid_directions = getValidDirections(line_index, char_index)

            if 'n' in valid_directions:
                checkNorth(line_index, char_index)
            if 'e' in valid_directions:
                checkEast(line_index, char_index)
            if 's' in valid_directions:
                checkSouth(line_index, char_index)
            if 'w' in valid_directions:
                checkWest(line_index, char_index)

            if 'ne' in valid_directions:
                checkNorthEast(line_index, char_index)
            if 'nw' in valid_directions:
                checkNorthWest(line_index, char_index)
            if 'se' in valid_directions:
                checkSouthEast(line_index, char_index)
            if 'sw' in valid_directions:
                checkSouthWest(line_index, char_index)


print(total)

    