def reverse_complement(DNA: str):
    rc = ""
    for i in range(len(DNA) - 1, -1, -1):
        nuc = DNA[i]
        if nuc == 'A':
            rc += 'T'
        elif nuc == 'T':
            rc += 'A'
        elif nuc == 'G':
            rc += 'C'
        else:
            rc += 'G'
    return rc


with open('rosalind_gasm.txt') as f:
    DNAs = []
    for line in f.readlines():
        DNAs.append(line.replace('\n', ''))

for k in range(1, len(DNAs[0])):
    graph_edges = set()
    for dna in DNAs:
        for i in range(k):
            graph_edges.add(dna[i:len(dna) + i - k + 1])
            graph_edges.add(reverse_complement(dna[i:len(dna) + i - k + 1]))

    k = len(list(graph_edges)[0])
    directed_edges = []
    for edge in graph_edges:
        directed_edges.append([edge[0: k - 1], edge[1: k]])

    circuits = []
    for cnt in range(2):
        tmp = directed_edges.pop(0)
        circ = tmp[0][-1]
        edge_char_list = []
        for edge in directed_edges:
            edge_char_list.append(edge[0])
        while tmp[1] in edge_char_list:
            circ += tmp[1][-1]
            idx_list = []
            for i, dir_edge in enumerate(directed_edges):
                if dir_edge[0] == tmp[1]:
                    idx_list.append(i)
            tmp = directed_edges.pop(idx_list[0])
        circuits.append(circ)

    if len(directed_edges) == 0:
        break

print(circuits[0])