from collections import defaultdict
with open('word_list_space.txt', 'r') as f:
    lines = f.readlines()

data = defaultdict(list)
for line in lines:
    data[line[0]].append(line)

for key, value in data.items():
    file = 'word_list\\word_list_' + key + '.txt'
    with open(file, 'w+') as f:
        f.writelines(value)
