import numpy as np

with open('rosalind_ba10b.txt') as f:
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
lines.pop(0)
lines.pop(0)
n, m = len(states), len(alphabet)
emission_probs = np.zeros((n, m))
for i in range(1, n + 1):
    for j in range(1, m + 1):
        emission_probs[i - 1][j - 1] = lines[i].split()[j]

pr = 1
for i in range(len(path)):
    state = path[i]
    c = x[i]
    i1 = states.index(state)
    i2 = alphabet.index(c)
    pr *= emission_probs[i1][i2]

print(f"{pr:.11e}")