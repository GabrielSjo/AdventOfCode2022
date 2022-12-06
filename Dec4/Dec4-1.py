count = 0
with open('Dec4/input.txt') as input:
    for line in input:
        line = line.strip().split(',')
        section = []
        for elf in line:
            section.append(elf.split('-'))
        section = [list(map(int,i)) for i in section]
        if section[0][0] >= section[1][0] and section[0][1] <= section[1][1]:
            count += 1
        elif section[0][0] <= section[1][0] and section[0][1] >= section[1][1]:
            count += 1
    print(count)
