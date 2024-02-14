import numpy as np
from math import log

with open('rosalind_ba10c.txt') as f:
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

start_prob = 1 / n
x_len = len(x)
viterbi_matrix = np.zeros((x_len, n))
back_matrix = np.zeros((x_len, n))

alph_idx = alphabet.index(x[0])
for i, state in enumerate(states):
    viterbi_matrix[0][i] = log(start_prob * emission_probs[i][alph_idx])

for i in range(1, x_len):
    alph_i = alphabet.index(x[i])
    for j in range(n):
        scores = [viterbi_matrix[i - 1][prev_j] + log(trans_probs[prev_j][j]) + log(emission_probs[j][alph_i])
                  for prev_j in range(n)]
        max_prob = max(scores)
        viterbi_matrix[i][j] = max_prob
        back_matrix[i][j] = scores.index(max_prob)


best_prob = max(viterbi_matrix[-1])
best_i = list(viterbi_matrix[-1]).index(best_prob)


output = [states[best_i]]
for i in range(x_len - 1, 0, -1):
    state = states[int(back_matrix[i][best_i])]
    best_i = int(back_matrix[i][best_i])
    output = [state] + output
print(''.join(output))