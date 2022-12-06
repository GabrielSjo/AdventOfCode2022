stacks = []
with open('Dec5/exinput.txt') as input:
    for line in input:
        print(len(line.strip('\n')))
        print(len(line)-len(line.lstrip(' ')))
        for character in line:
            pass
        break
