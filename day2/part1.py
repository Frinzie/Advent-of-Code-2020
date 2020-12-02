with open("input.txt", "r") as file:
    lines = file.readlines()

lines = [line.strip().replace(':', '', 1).split() for line in lines]

lines = [(line[0].split('-')[0], line[0].split('-')[1], line[1], line[2])
         for line in lines]

lines = [1 for line in lines if line[3].count(line[2]) >= int(line[0])
         and line[3].count(line[2]) <= int(line[1])]

print(sum(lines))
