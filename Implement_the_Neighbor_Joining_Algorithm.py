from collections import defaultdict
import numpy as np


def find_closest_clusters(D):
    max_element = D.max()
    D = np.copy(D)
    for i in range(len(D)):
        D[i][i] = max_element + 1
    min_element = D.argmin()
    l = len(D)
    return min_element // l, min_element % l


def construct_neighbor_joining_matrix(D, n):
    D_prim = np.copy(D)
    for i in range(len(D)):
        for j in range(len(D)):
            if i != j:
                ij_sum = 0
                for xx in range(len(D)):
                    ij_sum += (D[i][xx] + D[j][xx])
                D_prim[i, j] = (n - 2) * D[i, j] - ij_sum
    return D_prim


def append_D(D):
    l = len(D)
    AD = np.zeros([l + 1, l + 1], dtype=float)
    for i in range(l + 1):
        for j in range(l + 1):
            if i == l or j == l:
                AD[i][j] = 0
            else:
                AD[i][j] = D[i][j]
    return AD


def neighbor_joining(D, n, names):
    if n == 2:
        T = defaultdict(list)
        T[names[0]].append((names[1], D[0][1]))
        return T

    D_prim = construct_neighbor_joining_matrix(D, n)
    i, j = find_closest_clusters(D_prim)
    i_sum, j_sum = 0, 0
    for xx in range(len(D)):
        i_sum += D[i][xx]
        j_sum += D[j][xx]
    delta = (i_sum - j_sum) / (n - 2)
    limb_length_i = (D[i][j] + delta) / 2
    limb_length_j = (D[i][j] - delta) / 2

    name_i, name_j = names[i], names[j]

    D = append_D(D)
    names = names + [max(names) + 1]
    for k in range(n):
        D[k][n] = (D[k][i] + D[k][j] - D[i][j]) / 2
        D[n][k] = (D[k][i] + D[k][j] - D[i][j]) / 2
    for x in (j, i):
        D = np.delete(D, x, 0)
        D = np.delete(D, x, 1)
        names.pop(x)

    T = neighbor_joining(D, n - 1, names)
    # add new limbs
    ln = names[len(names) - 1]
    T[ln].append((name_i, limb_length_i))
    T[ln].append((name_j, limb_length_j))
    return T


with open("rosalind_ba7e.txt") as f:
    lines = f.readlines()
n = int(lines[0])
lines.pop(0)

d_matrix = np.zeros([n, n], dtype=float)
for i, line in enumerate(lines):
    elements = line.split()
    for j, el in enumerate(elements):
        d_matrix[i][j] = int(el)

edges = neighbor_joining(d_matrix, n, list(range(n)))

outputs = []
for e in sorted(edges):
    for v in edges[e]:
        outputs += [f"{e}->{v[0]}:{v[1]:.3f}"]
        outputs += [f"{v[0]}->{e}:{v[1]:.3f}"]
for o in sorted(outputs):
    print(o)