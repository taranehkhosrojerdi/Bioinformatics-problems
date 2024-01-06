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


def update(D, i, j, si, sj):
    D = np.copy(D)
    row_i = D[i, :]
    row_j = D[j, :]
    avr_row = (row_i * si + row_j * sj) / (si + sj)
    for x in range(len(D)):
        D[x][i] = avr_row[x]
        D[i][x] = avr_row[x]
    D = np.delete(D, j, 0)
    D = np.delete(D, j, 1)
    for x in range(len(D)):
        D[x][x] = 0
    return D


def upgma(D, n):
    clusters = list(range(0, n))
    age = defaultdict(lambda: 0)
    size = defaultdict(lambda: 1)

    T = {}
    node = n
    while len(clusters) > 1:
        i, j = find_closest_clusters(D)
        ci, cj = clusters[i], clusters[j]

        T[node] = [(ci, D[i, j] / 2 - age[ci]), (cj, D[i, j] / 2 - age[cj])]
        size[node] = size[ci] + size[cj]
        age[node] = D[i][j] / 2

        clusters[i] = node
        clusters.pop(j)
        D = update(D, i, j, size[ci], size[cj])
        node += 1
    return T


with open("rosalind_ba7d.txt") as f:
    lines = f.readlines()
n = int(lines[0])
lines.pop(0)

d_matrix = np.zeros([n, n], dtype=float)
for i, line in enumerate(lines):
    elements = line.split()
    for j, el in enumerate(elements):
        d_matrix[i][j] = int(el)

edges = upgma(d_matrix, n)

outputs = []
for e in sorted(edges):
    for v in edges[e]:
        outputs += [f"{e}->{v[0]}:{v[1]:.3f}"]
        outputs += [f"{v[0]}->{e}:{v[1]:.3f}"]
for o in sorted(outputs):
    print(o)