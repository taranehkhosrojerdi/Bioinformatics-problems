import numpy as np


def fill_matrix(pm, matrix, H_matrix, V_matrix, seq1, seq2):
    m, n = len(seq1), len(seq2)

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            H_matrix[i][j] = max(0, H_matrix[i - 1][j] - 1, matrix[i - 1][j] - 11)
            V_matrix[i][j] = max(0, V_matrix[i][j - 1] - 1, matrix[i][j - 1] - 11)
            matrix[i, j] = max(H_matrix[i][j], V_matrix[i][j], matrix[i - 1, j - 1] + pm[(seq1[i - 1], seq2[j - 1])])
    max_i, max_j = np.unravel_index(matrix.argmax(), matrix.shape)
    return max_i, max_j


def trace_back(matrix, H_matrix, V_matrix, seq1, seq2, i, j):
    p1, p2 = [], []
    while i != 0 and j != 0 and matrix[i, j] != 0:
        if matrix[i][j] == H_matrix[i][j]:
            p1.append(seq1[i - 1])
            i -= 1
        elif matrix[i][j] == V_matrix[i][j]:
            p2.append(seq2[j - 1])
            j -= 1
        else:
            p1.append(seq1[i - 1])
            p2.append(seq2[j - 1])
            i -= 1
            j -= 1
    p1.reverse()
    p2.reverse()
    print("".join(p1))
    print("".join(p2))


PM = {}
with open("blossom.txt") as pm:
    pm_lines = pm.readlines()

line_zero_list = pm_lines[0].split()
for i in range(1, len(pm_lines)):
    bl_line_list = pm_lines[i].split()
    for j in range(1, len(pm_lines)):
        PM[(line_zero_list[j - 1], bl_line_list[0])] = int(bl_line_list[j])

with open('rosalind_laff.txt') as f:
    lines = f.readlines()

DNAs = []
DNA_num = -1
for line in lines:
    if line[0] == '>':
        DNA_num += 1
        DNAs.append("")
    else:
        DNAs[DNA_num] += line.replace('\n', '')
seq1 = list(DNAs[0])
seq2 = list(DNAs[1])


m, n = len(seq1), len(seq2)

matrix = np.zeros((m + 1, n + 1), dtype=int)
H_matrix = np.zeros((m + 1, n + 1), dtype=int)
V_matrix = np.zeros((m + 1, n + 1), dtype=int)

max_i, max_j = fill_matrix(PM, matrix, H_matrix, V_matrix, seq1, seq2)

print(int(matrix[max_i, max_j]))

trace_back(matrix, H_matrix, V_matrix, seq1, seq2, max_i, max_j)