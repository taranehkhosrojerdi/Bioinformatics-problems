import numpy as np


def find_limb_length(n: int, j: int, D):
    limb_length = float('inf')
    for i in range(n):
        for k in range(i + 1, n):
            if i != k and j != k and j != i:
                limb_length = min(limb_length, (D[j][i] + D[j][k] - D[i][k]) // 2)

    return int(limb_length)


with open("rosalind_ba7b.txt") as f:
    lines = f.readlines()
n = int(lines[0])
J = int(lines[1])

d_matrix = np.zeros((n, n))
for i in range(n):
    elements = lines[i + 2].split()
    for j in range(n):
        d_matrix[i][j] = elements[j]

print(find_limb_length(n, J, d_matrix))