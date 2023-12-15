DNA = list(input())
for i in range(len(DNA)):
    if DNA[i] == 'T':
        DNA[i] = 'A'
    elif DNA[i] == 'A':
        DNA[i] = 'T'
    elif DNA[i] == "G":
        DNA[i] = 'C'
    elif DNA[i] == 'C':
        DNA[i] = 'G'
for i in range(len(DNA)):
    print(DNA[len(DNA) - i - 1], end="")