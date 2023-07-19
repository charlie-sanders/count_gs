with open('en_US.txt') as x:
    lines = x.readlines()


g_lines = []
for line in lines:
    if line[0] == 'g' and line[1] == 'i':
        g_lines.append(line)


with open('g_lines.txt', 'w') as x:
    for line in g_lines:
        x.write(line)


# Open g lines and count every occurence of  the letters 'ɡɪ'
hard_g_count = 0
soft_g_count = 0
all_gs = 0
with open('g_lines.txt') as x:
    lines = x.readlines()
    all_gs = len(lines)
    for line in lines:
        for i in range(len(line)):
            if line[i] == 'ɡ' and line[i + 1] == 'ɪ' or \
                    line[i] == 'ʒ' and line[i + 1] == 'ɪ':
                hard_g_count += 1

# Just assume everything not hard is soft
soft_g_count = all_gs - hard_g_count

print('Hard G count: ', hard_g_count)
print('Soft G count: ', soft_g_count)
print('All Gs: ', all_gs)