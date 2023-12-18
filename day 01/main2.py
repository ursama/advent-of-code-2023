# Unfinished :(

temp = ""
nr = ""
nrs = []
names = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

with open("data.txt", mode="r") as data:
    data = data.readlines()

    for line in data:
        for letter in line:
            if "0" <= letter <= "9":
                temp += letter

        nr += temp[0]
        nr += temp[-1]
        nrs.append(int(nr))
        temp = ""
        nr = ""

    print(sum(nrs))

