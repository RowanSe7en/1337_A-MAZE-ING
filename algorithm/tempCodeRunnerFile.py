
def emoji_render():
    path_coords = set()
    cur = exit_

    while cur in parents:
        py, px, _ = parents[cur]
        path_coords.add(cur)
        cur = (py, px)

    path_coords.add(entry)

    for i in range(1, 10):
        print(f"{i}\uFE0F\u20E3", end=" ")
    for i in range(0, 6):
        print(f"{i}\uFE0F\u20E3", end=" ")
    print()

    for y in range(height):

        print("⬛", end="")
        
        for x in range(width):
            if maze[y][x] & (1 << 0):
                print("⬛⬛", end="")
            else:
                xx = 1 if x < width - 1 else 0
                if (y, x) in path_coords and ((y - 1, x) in path_coords or (y - 1, x) == entry):
                    print("🟩⬛", end="")
                elif maze[y][x] == 16:          # <-- FIXED
                    print("🟦⬛", end="")        # <-- FIXED
                else:
                    print("⬜⬛", end="")
        print("")

        for x in range(width):
            if (y, x) in path_coords and ((y, x - 1) in path_coords or (y, x - 1) == entry) and not maze[y][x] & 1 << 3:
                left = "🟩"
            elif (maze[y][x] == 15 or maze[y][x] & 1 << 3):
                left = "⬛"
            elif (maze[y][x] == 16):
                left = "🟦"
            else:
                left = "⬜"

            if (y, x) == entry:
                content = "🟦"
            elif (y, x) == exit_:
                content = "🟪"
            elif (y, x) in path_coords:
                content = "🟩"
            elif maze[y][x] == 16:              # <-- FIXED
                content = "🟦"
            else:
                content = "⬜"

            print(left + content, end="")

        right = "⬛" if maze[y][width - 1] & (1 << 1) else ""
        print(right)

    for x in range(width):
        if maze[height - 1][x] & (1 << 2):
            print("⬛⬛", end="")
        else:
            print("⬜⬜", end="")
    print("⬛")
