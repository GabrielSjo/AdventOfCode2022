print(test)
with open('AdventOfCode/Dec1/input.txt', 'r') as input:
    sum = 0
    calories = 0
    for line in input:
        if line != "\n":
            sum = sum + int(line.strip())
        else:
            if sum > calories:
                calories = sum 
            sum = 0
    print(calories)
    