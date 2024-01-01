game_id = 1
possible = []
is_poss = True
max_r = 12
max_g = 13
max_b = 14
nr = 0

with open("data.txt", mode="r") as data:
    data = data.readlines()
    for line in data:
        line = line.split()[2:]
        for elem in line:
            try:
                nr = int(elem)
            except ValueError:
                if elem[0] == "r" and nr > max_r:
                    is_poss = False
                    break
                elif elem[0] == "g" and nr > max_g:
                    is_poss = False
                    break
                elif nr > max_b:
                    is_poss = False
                    break

        if is_poss:
            possible.append(game_id)
        else:
            is_poss = True
        game_id += 1

    print(sum(possible))
