with open("input.txt", "r") as file:
    values = [int(x) for x in file.read().split()]


def main():
    length = len(values)
    for i in range(length):
        for j in range(length):
            if (values[i]+values[j] == 2020) and (i != j):
                return values[i] * values[j]


print(main())
