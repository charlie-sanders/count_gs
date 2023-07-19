with open('en_US.txt') as x:
    lines = x.readlines()


g_lines = []
for line in lines:
    if line[0] == 'g' and line[1] == 'i':
        g_lines.append(line)


with open('g_lines.txt', 'w') as x:
    for line in g_lines:
        x.write(line)


# Open g lines and count every occurrence of hard gs, assume not hard is soft.
hard_g_count = 0
soft_g_count = 0
all_gs = 0
with open('g_lines.txt') as x:
    lines = x.readlines()
    all_gs = len(lines)
    for line in lines:
        # Strip out everything after /'
        line_idx = line.index('/')
        word = line[line_idx+2:-2]
        i = 0

        if word[i] == 'ɡ' and word[i + 1] == 'ɪ' or \
                word[i] == 'ʒ' and word[i + 1] == 'ɪ' or \
                word[i] == 'ɡ' and word[i+1] == 'ɝ':
            hard_g_count += 1
            print(f'Hard g -> {line}')
        else:
            print(f'Soft g -> {line}')

# Just assume everything not hard is soft
soft_g_count = all_gs - hard_g_count

print('Hard G count: ', hard_g_count)
print('\nSoft G count: ', soft_g_count)
print('\nAll words starting in "GI": ', all_gs)
