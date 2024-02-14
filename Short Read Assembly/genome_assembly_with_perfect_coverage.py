def reverse_complement(DNA: str):
    rc = ""
    for i in range(len(DNA) - 1, -1, -1):
        nuc = DNA[i]
        if nuc == 'A':
            rc += 'T'
        elif nuc == 'T':
            rc += 'A'
        elif nuc == 'G':
            rc += 'C'
        else:
            rc += 'G'
    return rc


def hamming_distance(str1: str, str2: str):
    l = len(str1)
    hd = 0
    for i in range(l):
        if str1[i] != str2[i]:
            hd += 1
    return hd


with open('rosalind_corr.txt') as f:
    lines = f.readlines()
DNAs = list()
DNA_num = -1
for line in lines:
    if line[0] == '>':
        DNA_num += 1
        DNAs.append("")
    else:
        DNAs[DNA_num] += line.replace('\n', '')

correct_indices = []
for i in range(0, len(DNAs)):
    for j in range(i + 1, len(DNAs)):
        if DNAs[i] == DNAs[j] or DNAs[i] == reverse_complement(DNAs[j]):
            correct_indices.append(i)
            correct_indices.append(j)

for i in range(len(DNAs)):
    if i not in correct_indices:
        for ci in correct_indices:
            hd = hamming_distance(DNAs[i], DNAs[ci])
            if hd == 1:
                print("%s->%s" % (DNAs[i], DNAs[ci]))
                break
            rc_hd = hamming_distance(DNAs[i], reverse_complement(DNAs[ci]))
            if rc_hd == 1:
                print("%s->%s" % (DNAs[i], reverse_complement(DNAs[ci])))
                break