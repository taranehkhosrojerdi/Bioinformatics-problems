class Node:
    def __init__(self, name: str):
        self.name = name


class Graph:
    def __init__(self):
        self.nodes = list()
        self.edges = list()

    def get_node_by_name(self, node_name: str):
        for n in self.nodes:
            if n.name == node_name:
                return n
        return None

    def add_node(self, node_name: str):
        if self.get_node_by_name(node_name) is not None:
            return
        node = Node(node_name)
        self.nodes.append(node)

    def add_edge(self, first_node: str, second_node: str):
        for edge in self.edges:
            if edge[0].name == first_node and edge[1].name == second_node:
                return
        node1 = self.get_node_by_name(first_node)
        node2 = self.get_node_by_name(second_node)
        self.edges.append((node1, node2))


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


with open('rosalind_dbru.txt') as f:
    lines = f.readlines()
DNAs = list()
for line in lines:
    DNAs.append(line.replace('\n', ''))

k = len(DNAs[0]) - 1
g = Graph()
for dna in DNAs:
    g.add_node(dna[0: k])
    g.add_node(dna[1: k + 1])
    g.add_edge(dna[0: k], dna[1: k + 1])
    rc = reverse_complement(dna)
    g.add_node(rc[0: k])
    g.add_node(rc[1: k + 1])
    g.add_edge(rc[0: k], rc[1: k + 1])

for edge in g.edges:
    print("(%s, %s)" % (edge[0].name, edge[1].name))