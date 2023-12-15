import numpy as np


def get_minimum_penalty(x, y, differ_penalty, gap_penalty):
    i, j = 0, 0
    m, n = len(x), len(y)
    matrix = np.zeros([m + 1, n + 1], dtype=int)
    matrix[0:(m + 1), 0] = [i * gap_penalty for i in range(m + 1)]
    matrix[0, 0:(n + 1)] = [i * gap_penalty for i in range(n + 1)]

    i = 1
    while i <= m:
        j = 1
        while j <= n:
            if x[i - 1] == y[j - 1]:
                matrix[i][j] = matrix[i - 1][j - 1]
            else:
                matrix[i][j] = min(matrix[i - 1][j - 1] + differ_penalty,
                                   matrix[i - 1][j] + gap_penalty,
                                   matrix[i][j - 1] + gap_penalty)
            j += 1
        i += 1
    l = n + m
    i = m
    j = n

    H_pos = l
    V_pos = l
    H_matrix = np.zeros(l + 1, dtype=int)
    V_matrix = np.zeros(l + 1, dtype=int)

    while not (i == 0 or j == 0):
        if x[i - 1] == y[j - 1]:
            H_matrix[H_pos] = ord(x[i - 1])
            V_matrix[V_pos] = ord(y[j - 1])
            H_pos -= 1
            V_pos -= 1
            i -= 1
            j -= 1
        elif (matrix[i - 1][j - 1] + differ_penalty) == matrix[i][j]:

            H_matrix[H_pos] = ord(x[i - 1])
            V_matrix[V_pos] = ord(y[j - 1])
            H_pos -= 1
            V_pos -= 1
            i -= 1
            j -= 1

        elif (matrix[i - 1][j] + gap_penalty) == matrix[i][j]:
            H_matrix[H_pos] = ord(x[i - 1])
            V_matrix[V_pos] = ord('-')
            H_pos -= 1
            V_pos -= 1
            i -= 1

        elif (matrix[i][j - 1] + gap_penalty) == matrix[i][j]:
            H_matrix[H_pos] = ord('-')
            V_matrix[V_pos] = ord(y[j - 1])
            H_pos -= 1
            V_pos -= 1
            j -= 1

    while H_pos > 0:
        if i > 0:
            i -= 1
            H_matrix[H_pos] = ord(x[i])
            H_pos -= 1
        else:
            H_matrix[H_pos] = ord('-')
            H_pos -= 1

    while V_pos > 0:
        if j > 0:
            j -= 1
            V_matrix[V_pos] = ord(y[j])
            V_pos -= 1
        else:
            V_matrix[V_pos] = ord('-')
            V_pos -= 1

    id = 1
    i = l
    while i >= 1:
        if (chr(V_matrix[i]) == '-') and chr(H_matrix[i]) == '-':
            id = i + 1
            break

        i -= 1

    print(matrix[m][n])
    i = id
    x_seq = ""
    while i <= l:
        x_seq += chr(H_matrix[i])
        i += 1
    print(x_seq)

    # Y
    i = id
    y_seq = ""
    while i <= l:
        y_seq += chr(V_matrix[i])
        i += 1
    print(y_seq)


with open('rosalind_edta.txt') as f:
    lines = f.readlines()
DNAs = list()
DNA_num = -1
for line in lines:
    if line[0] == '>':
        DNA_num += 1
        DNAs.append("")
    else:
        DNAs[DNA_num] += line.replace('\n', '')
gene1 = DNAs[0]
gene2 = DNAs[1]

mismatch_penalty = 1
gap_penalty = 1
get_minimum_penalty(gene1, gene2, mismatch_penalty, gap_penalty)