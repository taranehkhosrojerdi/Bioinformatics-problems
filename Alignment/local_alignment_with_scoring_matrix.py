import numpy as np


def fill_matrix(pm, matrix, seq1, seq2):
    matrix[0][0] = 0
    for i in range(1, len(seq1) + 1):
        matrix[i][0] = 0
    for j in range(1, len(seq2) + 1):
        matrix[0][j] = 0

    for i in range(1, len(seq1) + 1):
        for j in range(1, len(seq2) + 1):
            matrix[i][j] = max(0, matrix[i - 1][j] - 5, matrix[i][j - 1] - 5,
                               matrix[i - 1][j - 1] + pm[(seq1[i - 1], seq2[j - 1])])


def find_path(matrix, i, j, seq1, seq2, p1: list, p2: list):
    if matrix[i][j] == 0:
        return
    if matrix[i][j] == matrix[i - 1][j] - 5:
        p1.append(seq1[i - 1])
        find_path(matrix, i - 1, j, seq1, seq2, p1, p2)
    elif matrix[i][j] == matrix[i][j - 1] - 5:
        p2.append(seq2[j - 1])
        find_path(matrix, i, j - 1, seq1, seq2, p1, p2)
    else:
        p1.append(seq1[i - 1])
        p2.append(seq2[j - 1])
        find_path(matrix, i - 1, j - 1, seq1, seq2, p1, p2)


PM = {}
with open("PAM250.txt") as pm:
    pm_lines = pm.readlines()

line_zero_list = pm_lines[0].split()
for i in range(1, len(pm_lines)):
    for j in range(1, len(pm_lines)):
        bl_line_list = pm_lines[i].split()
        PM[(line_zero_list[j - 1], bl_line_list[0])] = int(bl_line_list[j])

# generate an M x N empty matrix and fill it with appropriate transition values
with open('rosalind_loca.txt') as f:
    lines = f.readlines()
DNAs = list()
DNA_num = -1
for line in lines:
    if line[0] == '>':
        DNA_num += 1
        DNAs.append("")
    else:
        DNAs[DNA_num] += line.replace('\n', '')
seq1 = list(DNAs[0])
seq2 = list(DNAs[1])
# input()
# seq1 = list(input())
# input()
# seq2 = list(input())

m = len(seq1)
n = len(seq2)

matrix = np.empty((m + 1, n + 1))
fill_matrix(PM, matrix, seq1, seq2)

max_zero_i = 0
max_zero_j = 0
for i in range(m + 1):
    for j in range(n + 1):
        if matrix[i][j] == 0:
            max_zero_i = i
            max_zero_j = j

max_i = 0
max_j = 0
for i in range(m + 1):
    for j in range(n + 1):
        if matrix[i][j] > matrix[max_i][max_j]:
            max_i = i
            max_j = j
path1 = list()
path2 = list()
find_path(matrix, max_i, max_j, seq1, seq2, path1, path2)
path1.reverse()
path2.reverse()
#
# for i in range(m + 1):
#     for j in range(n + 1):
#         print(matrix[i][j], end=" ")
#     print()
#

print(int(matrix[max_i][max_j]))
for p in path1:
    print(p, end="")
print()
for p in path2:
    print(p, end="")
print()