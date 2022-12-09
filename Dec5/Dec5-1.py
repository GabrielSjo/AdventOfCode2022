def init_stacks():
    with open('Dec5/exinput.txt') as input:
        for line in input:
            if line.startswith(" 1"):
                line = line.strip("\n")
                stackIndexes = [character for character in line]
                stacks = [[]]*int(line.strip(" ")[-1])
                print(stacks)
                print(stackIndexes)
                break
    input.close()
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
                        stacks[0][i].append(character)
    input.close()
stackIndexes, stacks = init_stacks()
stacks = fill_stacks(stackIndexes, stacks)
