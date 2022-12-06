import string
chars = string.ascii_lowercase + string.ascii_uppercase
psum = 0
arr = []
cc = []
with open('Dec3/input.txt') as input:
    for line in input:
        arr.append(line.strip())
        if len(arr) == 3:
            for character in arr[0]:
                if character in arr[1]:
                    if character not in cc:
                        cc.append(character)
            for character in cc:
                if character in arr[2]: 
                    psum = psum + chars.rfind(character)+1
                    break
            cc = []
            arr = []
print(psum)
# N * n^3
        
        

