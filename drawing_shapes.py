# Get shapes
def get_shape():
    global shapes, shape_colors

    return Piece(5,0, random.choice(shapes))

# Change shape format
def change_shape_format(shape):
    positions = []
    format = shape.shape[shape.rotation % len(shape.shape)]

    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == '0':
                positions.append((shape.x + j, shape.y+ i))
        for i, pos in enumerate(positions):
            positions[i] = (pos[0] - 2, pos[1]-4)
        return positions

# Draw next shape
def draw_next_shape(shape,surface):
    sx = top_left_x + play_width + 50
    sy = top_left_y + play_height/2 -100
    format = shape.shape[shape.rotation % len(shape.shape)]

    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == '0':
                pygame.draw.rect(surface, shape.color(sx+j*30, 30, 30), 0)
