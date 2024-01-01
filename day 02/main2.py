powers = []
min_r = 1
min_g = 1
min_b = 1
nr = 0

with open("data.txt", mode="r") as data:
    data = data.readlines()
    for line in data:
        line = line.split()[2:]
        for elem in line:
            try:
                nr = int(elem)
            except ValueError:
                if elem[0] == "r" and nr > min_r:
                    print(f"czerwony {nr}")
                    min_r = nr
                elif elem[0] == "g" and nr > min_g:
                    print(f"zielony {nr}")
                    min_g = nr
                elif elem[0] == "b" and nr > min_b:
                    print(f"niebieski {nr}")
                    min_b = nr

        print(f"red {min_r} green {min_g} blue {min_b}")
        powers.append(min_r * min_g * min_b)
        min_r, min_g, min_b = 1, 1, 1

    print(sum(powers))
