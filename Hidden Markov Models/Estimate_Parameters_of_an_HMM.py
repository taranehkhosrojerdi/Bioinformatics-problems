import numpy as np


def find_trans_probs(path, Q):
    n = len(Q)
    trans_probs = np.zeros((n, n), dtype=float)
    for i in range(len(path) - 1):
        q1 = path[i]
        q2 = path[i + 1]
        i1 = Q.index(q1)
        i2 = Q.index(q2)
        trans_probs[i1][i2] += 1
    for i in range(n):
        s = sum(trans_probs[i])
        for j in range(n):
            if s != 0:
                trans_probs[i][j] = round(trans_probs[i][j] / s, 3)
            else:
                trans_probs[i][j] = round(1 / n, 3)
    return trans_probs


def find_emission_probs(seq, alph, path, Q):
    emission_probs = np.zeros((len(Q), len(alphabet)))
    for i in range(len(seq)):
        state = path[i]
        emission = seq[i]
        i1 = states.index(state)
        i2 = alph.index(emission)
        emission_probs[i1][i2] += 1
    for i in range(len(Q)):
        s = sum(emission_probs[i])
        for j in range(len(alph)):
            if s != 0:
                emission_probs[i][j] = round(emission_probs[i][j] / s, 3)
            else:
                emission_probs[i][j] = round(1 / len(alph), 3)
    return emission_probs


with open('rosalind_ba10h.txt') as f:
    lines = f.readlines()
lines = [line.replace('\n', '') for line in lines]
x = lines[0]
lines.pop(0)
lines.pop(0)
alphabet = lines[0].split()
lines.pop(0)
lines.pop(0)
path = lines[0]
lines.pop(0)
lines.pop(0)
states = lines[0].split()

transition_matrix = find_trans_probs(path, states)
for s in states:
    print(s, end='\t')
print()
for i in range(len(states)):
    print(states[i], end='\t')
    for p in transition_matrix[i]:
        print(p, end=' ')
    print()
print('--------')

emission_matrix = find_emission_probs(x, alphabet, path, states)
print('\t')
for a in alphabet:
    print(a, end='\t')
print()

for i in range(len(states)):
    print(states[i], end='\t')
    for p in emission_matrix[i]:
        print(p, end='\t')
    print()