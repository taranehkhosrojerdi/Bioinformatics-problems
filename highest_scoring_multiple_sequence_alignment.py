import numpy as np


def fill_matrix(matrix, seq1, seq2, seq3):
    for i in range(1, len(seq1) + 1):
        for j in range(1, len(seq2) + 1):
            for k in range(1, len(seq3) + 1):
                if seq1[i - 1] == seq2[j - 1] and seq2[j - 1] == seq3[k - 1]:
                    matrix[i][j][k] = matrix[i - 1][j - 1][k - 1] + 1
                else:
                    matrix[i][j][k] = max(matrix[i - 1][j - 1][k - 1], matrix[i - 1][j - 1][k],
                                          matrix[i - 1][j][k - 1], matrix[i][j - 1][k - 1],
                                          matrix[i][j][k - 1], matrix[i][j - 1][k], matrix[i - 1][j][k])


def trace_back(matrix, seq1, seq2, seq3):
    i, j, k = len(seq1), len(seq2), len(seq3)
    s1, s2, s3 = [], [], []
    while i != 0 or j != 0 or k != 0:
        if i > 0 and j > 0 and k > 0 and (matrix[i][j][k] == matrix[i - 1][j - 1][k - 1] + 1) and (seq1[i - 1] == seq2[j - 1] and seq2[j - 1] == seq3[k - 1]):
            s1.append(seq1[i - 1])
            s2.append(seq2[j - 1])
            s3.append(seq3[k - 1])
            i -= 1
            j -= 1
            k -= 1
        elif j > 0 and k > 0 and matrix[i][j][k] == matrix[i][j - 1][k - 1]:
            s1.append('-')
            s2.append(seq2[j - 1])
            s3.append(seq3[k - 1])
            j -= 1
            k -= 1
        elif i > 0 and k > 0 and matrix[i][j][k] == matrix[i - 1][j][k - 1]:
            s1.append(seq1[i - 1])
            s2.append('-')
            s3.append(seq3[k - 1])
            i -= 1
            k -= 1
        elif i > 0 and j > 0 and matrix[i][j][k] == matrix[i - 1][j - 1][k]:
            s1.append(seq1[i - 1])
            s2.append(seq2[j - 1])
            s3.append('-')
            i -= 1
            j -= 1
        elif i > 0 and matrix[i][j][k] == matrix[i - 1][j][k]:
            s1.append(seq1[i - 1])
            s2.append('-')
            s3.append('-')
            i -= 1
        elif j > 0 and matrix[i][j][k] == matrix[i][j - 1][k]:
            s1.append('-')
            s2.append(seq2[j - 1])
            s3.append('-')
            j -= 1
        elif k > 0 and matrix[i][j][k] == matrix[i][j][k - 1]:
            s1.append('-')
            s2.append('-')
            s3.append(seq3[k - 1])
            k -= 1
        elif i > 0 and j > 0 and k > 0 and matrix[i][j][k] == matrix[i - 1][j - 1][k - 1]:
            s1.append(seq1[i - 1])
            s2.append(seq2[j - 1])
            s3.append(seq3[k - 1])
            i -= 1
            j -= 1
            k -= 1

    s1.reverse()
    s2.reverse()
    s3.reverse()
    print("".join(s1))
    print("".join(s2))
    print("".join(s3))


DNAs = list()
DNAs.append(input())
DNAs.append(input())
DNAs.append(input())
m, n, l = len(DNAs[0]), len(DNAs[1]), len(DNAs[2])
matrix = np.zeros((m + 1, n + 1, l + 1))
fill_matrix(matrix, DNAs[0], DNAs[1], DNAs[2])

print(int(matrix[m][n][l]))
trace_back(matrix, DNAs[0], DNAs[1], DNAs[2])