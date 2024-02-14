import numpy as np


def forward_algorithm(seq, Q, alph,  t_probs, e_probs):
    f_matrix = np.ones((len(seq), len(Q)))
    ch_i = alph.index(seq[0])
    for i in range(len(Q)):
        f_matrix[0][i] = e_probs[i][ch_i]

    for i in range(1, len(seq)):
        ch_i = alph.index(seq[i])
        for j in range(len(Q)):
            f_matrix[i][j] = sum(
                t_probs[k][j] * e_probs[j][ch_i] * f_matrix[i - 1][k] for k in range(len(Q))
            )
    return f_matrix


def backward_algorithm(seq, Q, alph, t_probs, e_probs):
    b_matrix = np.ones((len(seq), len(Q)))
    l = len(seq)

    reverse_seq = [seq[x] for x in range(len(seq) - 1, -1, -1)]
    for i, e in enumerate(reverse_seq[:-1], start=1):
        ch_i = alph.index(e)
        for j in range(len(Q)):
            b_matrix[l - 1 - i][j] = sum(
                t_probs[j][k] * e_probs[k][ch_i] * b_matrix[l - i][k] for k in range(len(Q))
            )
    return b_matrix


with open('rosalind_ba10j.txt') as f:
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

mult_matrix = forward_algorithm(x, states, alphabet, trans_probs, emission_probs) * backward_algorithm(x, states, alphabet, trans_probs, emission_probs)
for i in range(len(mult_matrix)):
    row_sum = sum(mult_matrix[i])
    for j in range(len(mult_matrix[i])):
        mult_matrix[i][j] = mult_matrix[i][j] / row_sum


for s in states:
    print(s, end='\t')
print()

for element in np.round(mult_matrix, 4):
    for e in element:
        print(e, end='\t')
    print()