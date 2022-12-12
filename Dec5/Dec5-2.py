def init_stacks():
    with open('Dec5/exinput.txt') as input:
        for line in input:
            if line.startswith(" 1"):
                line = line.strip("\n")
                stackIndexes = [character for character in line]
                stacks = [[] for _ in range(int(line.strip(" ")[-1]))]
                break
    return stackIndexes, stacks
def fill_stacks(stackIndexes, stacks):
    with open('Dec5/exinput.txt') as input:
        for line in input:
            if line.startswith(" 1"):
                break
            else:
                for i, character in enumerate(line):
                    if character.isalpha():
                        i = int(stackIndexes[i])-1
                        stacks[i].append(character)
    return stacks
def move_boxes(stacks):
    moves = []
    tmp = []
    with open('Dec5/exinput.txt') as input:
        for line in input:
            line = line.strip("\n")
            if line.startswith("move"):
                for idx, word in enumerate(line.split()):
                    if word.isnumeric() and idx != len(line.split()):
                        moves.append(word)
                print(moves)
                for k in range(0, int(moves[0])):
                    tmp.append(stacks[int(moves[1])-1][0])
                    del stacks[int(moves[1])-1][0]
                for n in tmp[::-1]:
                    stacks[int(moves[2])-1].insert(0, n)
                moves = []
                tmp = []
                print(stacks)
        return stacks
stackIndexes, stacks = init_stacks()
stacks = fill_stacks(stackIndexes, stacks)
stacks = move_boxes(stacks)
ans = ""
for k in range(len(stacks)):
    ans = ans + stacks[k][0]
print(ans)