import random

#this function takes no input and randomly selects a type of tetris piece
    #it outputs the starting coordinates within the grid of all 4 squares and what color they should be
def piece_generator():
    piece_type = random.randint(1,8)
    if piece_type == 1: #cyan straight horizontal line ("I")
        starting_position = [[0, 3], [0, 4], [0, 5], [0,6]] #starting coordinates of this piece
        color = [] #cyan
    elif piece_type == 2: #royal blue left L
        starting_position = [[1,4], [1,5], [1,6], [0,6]]
        color = [] #royal blue
    elif piece_type == 3: #orange right L
        starting_position = [[1,4], [1,5], [1,6], [0,4]]
        color = [] #orange
    elif piece_type == 4: #yellow square
        starting_position = [[0,4], [1,4], [0,5], [1,5]]
        color = [] #yellow
    elif piece_type == 5: #green parallelogram-type shape
        starting_position = [[1,4], [0,5], [1,5], [0,6]]
        color = [] #green
    elif piece_type == 6: #red parallelogram-type shape
        starting_position = [[0,4], [0,5], [1,5], [1,6]]
        color = [] #red
    elif piece_type == 7: #purple T
        starting_position = [[0,4], [0,5], [1,5], [0,6]]
        color = [] #purple
    return stating_position, color
