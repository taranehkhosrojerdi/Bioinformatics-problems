import numpy as np


def calc_penalty(c):
    pen = 0
    for i in range(len(c)):
        for j in range(i + 1, len(c)):
            if c[i] != c[j]:
                pen -= 1
    return pen


def find_max_for_each_cell(matrix, directions, indices, seqs):
    s1, s2, s3, s4 = seqs[0], seqs[1], seqs[2], seqs[3]
    i, j, k, q = indices[0], indices[1], indices[2], indices[3]
    v = []
    dir_guide = []
    if i > 0 and j > 0 and k > 0 and q > 0:
        v.append(matrix[i - 1][j - 1][k - 1][q - 1] + calc_penalty([s1[i - 1], s2[j - 1], s3[k - 1], s4[q - 1]]))
        dir_guide.append(0)
    if i > 0 and j > 0 and k > 0:
        v.append(matrix[i - 1][j - 1][k - 1][q] + calc_penalty([s1[i - 1], s2[j - 1], s3[k - 1], '-']))
        dir_guide.append(1)
    if i > 0 and j > 0 and q > 0:
        v.append(matrix[i - 1][j - 1][k][q - 1] + calc_penalty([s1[i - 1], s2[j - 1], '-', s4[q - 1]]))
        dir_guide.append(2)
    if i > 0 and k > 0 and q > 0:
        v.append(matrix[i - 1][j][k - 1][q - 1] + calc_penalty([s1[i - 1], '-', s3[k - 1], s4[q - 1]]))
        dir_guide.append(3)
    if j > 0 and k > 0 and q > 0:
        v.append(matrix[i][j - 1][k - 1][q - 1] + calc_penalty(['-', s2[j - 1], s3[k - 1], s4[q - 1]]))
        dir_guide.append(4)
    if k > 0 and q > 0:
        v.append(matrix[i][j][k - 1][q - 1] + calc_penalty(['-', '-', s3[k - 1], s4[q - 1]]))
        dir_guide.append(5)
    if j > 0 and q > 0:
        v.append(matrix[i][j - 1][k][q - 1] + calc_penalty(['-', s2[j - 1], '-', s4[q - 1]]))
        dir_guide.append(6)
    if j > 0 and k > 0:
        v.append(matrix[i][j - 1][k - 1][q] + calc_penalty(['-', s2[j - 1], s3[k - 1], '-']))
        dir_guide.append(7)
    if i > 0 and q > 0:
        v.append(matrix[i - 1][j][k][q - 1] + calc_penalty([s1[i - 1], '-', '-', s4[q - 1]]))
        dir_guide.append(8)
    if i > 0 and k > 0:
        v.append(matrix[i - 1][j][k - 1][q] + calc_penalty([s1[i - 1], '-', s3[k - 1], '-']))
        dir_guide.append(9)
    if i > 0 and j > 0:
        v.append(matrix[i - 1][j - 1][k][q] + calc_penalty([s1[i - 1], s2[j - 1], '-', '-']))
        dir_guide.append(10)
    if q > 0:
        v.append(matrix[i][j][k][q - 1] + calc_penalty(['-', '-', '-', s4[q - 1]]))
        dir_guide.append(11)
    if k > 0:
        v.append(matrix[i][j][k - 1][q] + calc_penalty(['-', '-', '-', s3[k - 1]]))
        dir_guide.append(12)
    if j > 0:
        v.append(matrix[i][j - 1][k][q] + calc_penalty(['-', '-', s2[j - 1], '-']))
        dir_guide.append(13)
    if i > 0:
        v.append(matrix[i - 1][j][k][q] + calc_penalty([s1[i - 1], '-', '-', '-']))
        dir_guide.append(14)

    if i != 0 or j != 0 or k != 0 or q != 0:
        idx = v.index(max(v))
        matrix[i][j][k][q] = v[idx]
        directions[i][j][k][q] = dir_guide[idx]


def fill_matrix(matrix, directions, seq1, seq2, seq3, seq4):
    for i in range(len(seq1) + 1):
        for j in range(len(seq2) + 1):
            for k in range(len(seq3) + 1):
                for q in range(len(seq4) + 1):
                    find_max_for_each_cell(matrix, directions, (i, j, k, q), [seq1, seq2, seq3, seq4])


def trace_back(directions, seq1, seq2, seq3, seq4):
    i, j, k, q = len(seq1), len(seq2), len(seq3), len(seq4)
    s1, s2, s3, s4 = [], [], [], []
    while i != 0 or j != 0 or k != 0 or q != 0:
        if directions[i][j][k][q] == 0:
            s1.append(seq1[i - 1])
            s2.append(seq2[j - 1])
            s3.append(seq3[k - 1])
            s4.append(seq4[q - 1])
            i -= 1
            j -= 1
            k -= 1
            q -= 1
        elif directions[i][j][k][q] == 1:
            s1.append(seq1[i - 1])
            s2.append(seq2[j - 1])
            s3.append(seq3[k - 1])
            s4.append('-')
            j -= 1
            k -= 1
            i -= 1
        elif directions[i][j][k][q] == 2:
            s1.append(seq1[i - 1])
            s2.append(seq2[j - 1])
            s3.append('-')
            s4.append(seq4[q - 1])
            i -= 1
            j -= 1
            q -= 1
        elif directions[i][j][k][q] == 3:
            s1.append(seq1[i - 1])
            s2.append('-')
            s3.append(seq3[k - 1])
            s4.append(seq4[q - 1])
            i -= 1
            k -= 1
            q -= 1
        elif directions[i][j][k][q] == 4:
            s1.append('-')
            s2.append(seq2[j - 1])
            s3.append(seq3[k - 1])
            s4.append(seq4[q - 1])
            j -= 1
            k -= 1
            q -= 1
        elif directions[i][j][k][q] == 5:
            s1.append('-')
            s2.append('-')
            s3.append(seq3[k - 1])
            s4.append(seq4[q - 1])
            k -= 1
            q -= 1
        elif directions[i][j][k][q] == 6:
            s1.append('-')
            s2.append(seq2[j - 1])
            s3.append('-')
            s4.append(seq4[q - 1])
            j -= 1
            q -= 1
        elif directions[i][j][k][q] == 7:
            s1.append('-')
            s2.append(seq2[j - 1])
            s3.append(seq3[k - 1])
            s4.append('-')
            j -= 1
            k -= 1
        elif directions[i][j][k][q] == 8:
            s1.append(seq1[i - 1])
            s2.append('-')
            s3.append('-')
            s4.append(seq4[q - 1])
            i -= 1
            q -= 1
        elif directions[i][j][k][q] == 9:
            s1.append(seq1[i - 1])
            s2.append('-')
            s3.append(seq3[k - 1])
            s4.append('-')
            i -= 1
            k -= 1
        elif directions[i][j][k][q] == 10:
            s1.append(seq1[i - 1])
            s2.append(seq2[j - 1])
            s3.append('-')
            s4.append('-')
            i -= 1
            j -= 1
        elif directions[i][j][k][q] == 11:
            s1.append('-')
            s2.append('-')
            s3.append('-')
            s4.append(seq4[q - 1])
            q -= 1
        elif directions[i][j][k][q] == 12:
            s1.append('-')
            s2.append('-')
            s3.append(seq3[k - 1])
            s4.append('-')
            k -= 1
        elif directions[i][j][k][q] == 13:
            s1.append('-')
            s2.append(seq2[j - 1])
            s3.append('-')
            s4.append('-')
            j -= 1
        elif directions[i][j][k][q] == 14:
            s1.append(seq1[i - 1])
            s2.append('-')
            s3.append('-')
            s4.append('-')
            i -= 1

    s1.reverse()
    s2.reverse()
    s3.reverse()
    s4.reverse()
    print("".join(s1))
    print("".join(s2))
    print("".join(s3))
    print("".join(s4))


with open('rosalind_mult.txt') as f:
    lines = f.readlines()

DNAs = []
DNA_num = -1
for line in lines:
    if line[0] == '>':
        DNA_num += 1
        DNAs.append("")
    else:
        DNAs[DNA_num] += line.replace('\n', '')

m, n, l, p = len(DNAs[0]), len(DNAs[1]), len(DNAs[2]), len(DNAs[3])
matrix = np.zeros((m + 1, n + 1, l + 1, p + 1))
directions = np.zeros((m + 1, n + 1, l + 1, p + 1))
for i in range(m + 1):
    for j in range(n + 1):
        for k in range(l + 1):
            for q in range(p + 1):
                directions[i][j][k][q] = -np.inf

fill_matrix(matrix, directions, DNAs[0], DNAs[1], DNAs[2], DNAs[3])

print(int(matrix[m][n][l][p]))
trace_back(directions, DNAs[0], DNAs[1], DNAs[2], DNAs[3])