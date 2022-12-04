with open('AdventOfCode/Dec1/input.txt', 'r') as input:
    s = 0
    calories = []
    for line in input:
        if line != "\n":
            s = s + int(line.strip())
        else:
            calories.append(s)
            s = 0
    calories.sort()
    calories = calories[-3:]
    print(sum(calories))    
