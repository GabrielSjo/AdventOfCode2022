with open('Dec7/input.txt') as input:
    def dir_function(save_dir, current_dir):
        for line in input:
            line = line.strip('\n')
            if line.startswith('$'):
                if line.startswith('$ cd'):
                    if line == ('$ cd /'):
                        # dir is name is / (home)
                        current_dir.insert(0,"/")
                    elif line == ('$ cd ..'):
                        #dir name same as previous dir name
                        current_dir.insert(0,current_dir[1])
                    else:
                        #read dir name and save
                        line = line.replace('$ cd', 'dir')
                        current_dir.insert(0,current_dir[0] + "/" + line)
                    save_dir.setdefault(current_dir[0], [])
                elif line.startswith('$ ls'):
                    dir_function(save_dir, current_dir)
            elif line.startswith('dir'):
                save_dir[current_dir[0]].append(line)
            elif line[0].isdigit():
                for idx, word in enumerate(line.split()):
                    if word.isnumeric() and idx != len(line.split()):
                        save_dir[current_dir[0]].append(int(word))
                        break
        return save_dir
    save_dir = {} 
    current_dir = []
    save_dir = dir_function(save_dir, current_dir)
    print(save_dir)

def sum_size(save_dir, memory_dir, source, children, prev_source):
    for child in children:
        if isinstance(child, str):
            prev_source.append(source)
            source = source + "/" + child
            children = save_dir[source] 
            sum_size(save_dir, memory_dir, source, children, prev_source)
        elif isinstance(child, int):
            for s in prev_source:
                memory_dir[s][0] = memory_dir[s][0] + child
            if len(memory) == len(children):
                source = prev_source
                children = save_dir[source]
                sum_size(save_dir, memory_dir, source, children, prev_source)
memory_dir = save_dir.copy()
for value in memory_dir.values():
    del value[:]
print(memory_dir)
print(save_dir)
memory = []
prev_source = []
for source, children in save_dir.items():
    sum_size(save_dir, memory_dir, source, children, prev_source)
    break
