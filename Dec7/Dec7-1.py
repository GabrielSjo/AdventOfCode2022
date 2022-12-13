save = {}
current_dir = ""
with open('Dec7/input.txt') as input:
    def listdir_indir():
        for line in input:
            if line.startswith('$'):
                if line.startswith('$ cd'):
                    if line == ('cd /'):
                        # dir is name is / (home)
                        pass
                    elif line == ('cd ..'):
                        #dir name same as previous dir name
                        pass
                    else:
                        pass
                        #read dir name and save
                elif line.startswith('$ ls'):
                    listdir_indir()
                elif line.startswith('dir'):
                    save.append(line)
                elif line[0].isdigit():
                    for idx, word in enumerate(line.split())
                        if word.isnumeric() and idx != len(sample.split()):
                            save[current_dir] = word
