with open("input.txt", "r") as file:
    values = [int(x) for x in file.read().split()]


def main():
    for i in range(len(values)):
        for j in range(len(values)):
            for k in range(len(values)):
                if (values[i]+values[j]+values[k] == 2020 and i != j
                        and j != k and i != k):
                    return values[i]*values[j]*values[k]


print(main())
