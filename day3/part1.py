with open("input.txt", "r") as file:
    tree_map = [line.strip() for line in file.readlines()]

trees_count = 0
position_x = 0
position_y = 0
column_count = len(tree_map[0])

while position_y != len(tree_map)-1:
    position_x = (position_x+3) % column_count
    position_y += 1
    if tree_map[position_y][position_x] == "#":
        trees_count += 1

print(trees_count)
