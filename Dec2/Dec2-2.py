win = 6
draw = 3
loss = 0
points = 0

with open('Dec2/input.txt') as input:
    for line in input:
        score = 0
        line = line.strip().split(' ')
        if line[0] == 'A':
            if line[1] == 'X':
                score = loss + 3
            elif line[1] == 'Y':
                score = draw + 1
            elif line[1] == 'Z':
                score = win + 2
        elif line[0] == 'B':
            if line[1] == 'X':
                score = loss + 1
            elif line[1] == 'Y':
                score = draw + 2
            elif line[1] == 'Z':
                score = win + 3
        elif line[0] == 'C':
            if line[1] =='X':
                score = loss + 2
            elif line[1] == 'Y':
                score = draw + 3
            elif line[1] == 'Z':
                score = win + 1
        points = points + score
    print(points)