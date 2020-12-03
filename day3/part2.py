with open("input.txt", "r") as file:
    tree_map = [line.strip() for line in file.readlines()]

slopes = ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))
column_count = len(tree_map[0])
result = 1

for slope in slopes:
    trees_count = 0
    position_x = 0
    position_y = 0
    while position_y != len(tree_map)-1:
        position_x = (position_x+slope[0]) % column_count
        position_y += slope[1]
        if tree_map[position_y][position_x] == "#":
            trees_count += 1
    result *= trees_count

print(result)
