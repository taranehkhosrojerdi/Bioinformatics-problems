import numpy as np


def find_prob(seq, alph, Q, t_probs, e_probs):
    f_matrix = np.ones((len(seq) + 1, len(Q)))

    ch_i = alph.index(seq[0])
    for i in range(len(Q)):
        f_matrix[0][i] = e_probs[i][ch_i] / len(Q)

    for i in range(1, len(seq)):
        ch_i = alph.index(seq[i])
        for j in range(len(Q)):
            f_matrix[i][j] = sum(t_probs[k][j] * e_probs[j][ch_i] * f_matrix[i - 1][k]
                                 for k in range(len(Q)))

    print(sum(f_matrix[len(seq) - 1, :]))


with open('rosalind_ba10d.txt') as f:
    lines = f.readlines()
lines = [line.replace('\n', '') for line in lines]
x = lines[0]
lines.pop(0)
lines.pop(0)
alphabet = lines[0].split()
lines.pop(0)
lines.pop(0)
states = lines[0].split()
lines.pop(0)
lines.pop(0)

n = len(states)
m = len(alphabet)
trans_probs = np.zeros((n, n))
for i in range(1, n + 1):
    for j in range(1, n + 1):
        trans_probs[i - 1][j - 1] = lines[i].split()[j]
for i in range(n + 2):
    lines.pop(0)
emission_probs = np.zeros((n, m))
for i in range(1, n + 1):
    for j in range(1, m + 1):
        emission_probs[i - 1][j - 1] = lines[i].split()[j]

find_prob(x, alphabet, states, trans_probs, emission_probs)