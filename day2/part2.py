with open("input.txt", "r") as file:
    lines = file.readlines()

lines = [line.strip().replace(':', '', 1).split() for line in lines]

lines = [(line[0].split('-')[0], line[0].split('-')[1], line[1], line[2])
         for line in lines]

summ = 0
for line in lines:
    first_position = int(line[0]) - 1
    second_position = int(line[1]) - 1
    letter = line[2]
    word = line[3]
    summ += (word[first_position] == letter) ^ (word[second_position] == letter)

print(summ)
