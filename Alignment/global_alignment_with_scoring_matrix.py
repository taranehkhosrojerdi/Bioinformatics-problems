import numpy as np


def fill_matrix(blossom, matrix, seq1, seq2):
    matrix[0][0] = 0
    for i in range(1, len(seq1) + 1):
        matrix[i][0] = matrix[i - 1][0] - 5
    for j in range(1, len(seq2) + 1):
        matrix[0][j] = matrix[0][j - 1] - 5

    for i in range(1, len(seq1) + 1):
        for j in range(1, len(seq2) + 1):
            matrix[i][j] = max(matrix[i - 1][j] - 5, matrix[i][j - 1] - 5,
                               matrix[i - 1][j - 1] + blossom[(seq1[i - 1], seq2[j - 1])])


# put blossom file into a dictionary
blossom = {}
with open("blossom.txt") as bl:
    bl_lines = bl.readlines()

line_zero_list = bl_lines[0].split()
for i in range(1, len(bl_lines)):
    for j in range(1, len(bl_lines)):
        bl_line_list = bl_lines[i].split()
        blossom[(line_zero_list[j - 1], bl_line_list[0])] = int(bl_line_list[j])

# generate an M x N empty matrix and fill it with appropriate transition values
with open('rosalind_glob.txt') as f:
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
fill_matrix(blossom, matrix, seq1, seq2)
print(int(matrix[m][n]))