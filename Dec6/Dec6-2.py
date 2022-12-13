def subroutine():
    with open('Dec6/input.txt') as input:
        tmp = []
        for line in input:
            for i, character in enumerate(line):
                tmp.append(character)
                if len(tmp) == 15:
                    del tmp[0]
                    if len(tmp) == len(set(tmp)):
                        return i+1

ans = subroutine()
print(ans)