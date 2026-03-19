maze = [
    [1, 0, 1, 1],
    [1, 0, 0, 1],
    [1, 1, 0, 1],
]
def draw_maze(maze):
    WALL = "\033[47m  \033[0m"   # white background
    PATH = "\033[40m  \033[0m"   # black background

    for row in maze:
        for cell in row:
            if cell == 1:
                print(WALL, end="")
            else:
                print(PATH, end="")
        print()

draw_maze(maze)