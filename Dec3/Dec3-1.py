import string
chars = string.ascii_lowercase + string.ascii_uppercase
psum = 0
p_prev = 0
with open('Dec3/input.txt') as input:
    for line in input:
        line_length = len(line.strip())
        c1 = line[0:int(line_length/2)]
        c2 = line[int(line_length/2):line_length]
        for character in c1:
            if character in c2:
                if chars.rfind(character)+1 != p_prev:
                    psum = psum + chars.rfind(character)+1
                p_prev = chars.rfind(character)+1
        p_prev = 0
print(psum)
# Time complexity:
# O(n*
