import numpy as np


def calculate_dist(str1, str2):
    counter = 0
    for i in range(max(len(str1), len(str2))):
        if str1[i] is not None and str2[i] is not None and str1[i] == str2[i]:
            pass
        else:
            counter += 1
    return counter / (max(len(str1), len(str2)))


with open('rosalind_pdst.txt') as f:
    lines = f.readlines()

DNAs = list()
DNA_num = -1
for line in lines:
    if line[0] == '>':
        DNA_num += 1
        DNAs.append("")
    else:
        DNAs[DNA_num] += line.replace('\n', '')

mat = np.empty((DNA_num + 1, DNA_num + 1))
for i in range(DNA_num + 1):
    for j in range(DNA_num + 1):
        mat[i][j] = calculate_dist(DNAs[i], DNAs[j])
        print("{:.5f}".format(mat[i][j]), end=" ")
    print("")