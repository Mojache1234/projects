with open('word_list.txt', 'r') as f:
    lines = f.readlines()

data = []
for line in lines:
    data.append(line.replace(' ', '\n'))

with open('word_list/word_list_space.txt', 'w+') as f:
    f.writelines(data)
