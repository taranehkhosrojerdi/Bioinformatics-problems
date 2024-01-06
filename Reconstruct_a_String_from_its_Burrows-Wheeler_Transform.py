with open("rosalind_ba9j.txt") as f:
    lines = f.readlines()
bwt = ""
for line in lines:
    bwt += line.replace('\n', '')

# l = len(bwt_string)
# bwt_sorted = sorted(bwt_string)
#
# shifted = [0] * l
# shift_list_arr = [[] for i in range(128)]
#
# for i in range(l):
#     unicode = ord(bwt_string[i])
#     shift_list_arr[unicode].append(i)
#
# for i in range(l):
#     unicode = ord(bwt_sorted[i])
#     shifted[i] = shift_list_arr[unicode].pop(0)
#
# x = 3
# initial_string = [''] * l
# for i in range(l):
#     x = shifted[x]
#     initial_string[l-1-i] = bwt_string[x]
#
# output = ''.join(initial_string)
# output = output[::-1]
# print(output)

l = len(bwt)
table = ["" for i in range(l)]

for repeat in range(l):
    for ri in range(l):
        table[ri] = bwt[ri] + table[ri]
    table.sort()

for s in table:
    if s[l - 1] == '$':
        print(s)