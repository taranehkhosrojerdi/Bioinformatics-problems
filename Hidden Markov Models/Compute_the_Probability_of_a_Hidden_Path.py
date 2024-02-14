import numpy as np

with open('rosalind_ba10a.txt') as f:
    lines = f.readlines()
lines = [line.replace('\n', '') for line in lines]
hidden_path = lines[0]
lines.pop(0)
lines.pop(0)
states = lines[0].split()
lines.pop(0)
lines.pop(0)
n = len(states)
trans_matrix = np.zeros((n, n))
for i in range(1, n + 1):
    for j in range(1, n + 1):
        trans_matrix[i - 1][j - 1] = lines[i].split()[j]

integered_path = [int(states.index(s)) for s in hidden_path]
prob = 1 / len(states)
curr = integered_path[0]
for i in range(1, len(integered_path)):
    next = integered_path[i]
    prob *= trans_matrix[curr][next]
    curr = next
print(f"{prob:.11e}")