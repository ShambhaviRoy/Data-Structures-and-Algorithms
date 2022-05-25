# Huffman Coding: Loss-less variable length coding technique

# Time Complexity = O(n log n)

# node of Huffman Tree
class Node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right
        self.huff = ''  # tree direction 0 or 1

# to print each symbol and its code
def print_nodes(node, val = ''):
    new_val = val + str(node.huff)
    if node.left:
        print_nodes(node.left, new_val)
    if node.right:
        print_nodes(node.right, new_val)
    if not node.left and not node.right:
        print(node.symbol + '-->' + new_val)


# given characters and frequencies
chars = ['A', 'B', 'C', 'D', 'E']
freqs = [3, 5, 6, 4, 2]

nodes = []

for x in range(len(chars)):
    nodes.append(Node(freqs[x], chars[x]))

while len(nodes) > 1:
    nodes = sorted(nodes, key = lambda x: x.freq)

    left, right = nodes[0], nodes[1]    # pick 2 smallest nodes

    # assign tree direction
    left.huff = 0
    right.huff = 1

    new_node = Node(left.freq + right.freq, left.symbol + right.symbol, left, right)

    nodes.remove(left)
    nodes.remove(right)
    nodes.append(new_node)

print_nodes(nodes[0])



