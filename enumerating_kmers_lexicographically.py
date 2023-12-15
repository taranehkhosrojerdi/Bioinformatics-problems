def find_lex(i, n, str, alphabet):
    if i == n:
        print(str)
    elif i < n:
        for a in alphabet:
            find_lex(i + 1, n, str + a, alphabet)


alphabet = input().split()
alphabet.sort()
n = int(input())
find_lex(0, n, "", alphabet)