from collections import defaultdict


def find_top_bottom(t: int, s: str, sym):
    ti = s.index(sym)
    s.reverse()
    bi = s.index(sym)
    s.reverse()
    return ti + t, len(s) - bi - 1 + t


def index_seq(seq):
    d = defaultdict(int)
    for c in seq:
        yield c, d[c]
        d[c] += 1


def last2first(seq, i):
    first = list(index_seq(sorted(seq)))
    last = list(index_seq(seq))
    return first.index(last[i])


def bwt_matching(last_c, pattern):
    last = list(index_seq(last_c))
    l = len(last)
    top = 0
    bottom = l - 1
    while top <= bottom:
        if pattern:
            symbol = pattern[-1]
            pattern = pattern[:-1]
            cropped_last = list(last_c[top: bottom + 1])
            if symbol in cropped_last:
                top_index, bottom_index = find_top_bottom(top, cropped_last, symbol)
                top = last2first(last, top_index)
                bottom = last2first(last, bottom_index)
            else:
                return 0
        else:
            return bottom - top + 1


with open("rosalind_ba9l.txt") as f:
    last_column, patterns = f.read().splitlines()
l = len(last_column)
first_column = sorted(last_column)

patterns = patterns.split()
for p in patterns:
    print(bwt_matching(last_column, p), end=" ")