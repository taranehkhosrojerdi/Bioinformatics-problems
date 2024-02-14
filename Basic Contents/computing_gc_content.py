def calc_GC_content(DNA):
    return (DNA.count('G') + DNA.count('C')) / len(DNA) * 100


DNA_names = list()
DNAs = list()

with open('rosalind_gc.txt') as f:
    lines = f.readlines()

DNAs = []
DNA_num = -1
for line in lines:
    if line[0] == '>':
        DNA_num += 1
        DNA_names.append(line[1: len(line) - 1])
        DNAs.append("")
    else:
        DNAs[DNA_num] += line.replace('\n', '')

max_index = -1
max_content = 0
for j in range(len(DNAs)):
    if calc_GC_content(DNAs[j]) > max_content:
        max_content = calc_GC_content(DNAs[j])
        max_index = j

print(DNA_names[max_index])
print(max_content.__round__(6))