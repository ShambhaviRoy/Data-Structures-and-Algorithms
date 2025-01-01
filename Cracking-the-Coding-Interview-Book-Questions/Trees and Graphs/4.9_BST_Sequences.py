# BST Sequences: A binary search tree was created by traversing through an array from left to right
# and inserting each element. Given a binary search tree with distinct elements, print all possible
# arrays that could have led to this tree.

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def all_sequences(node):
    if not node:
        return [[]]
    
    result = []
    prefix = [node.data]
    left = all_sequences(node.left)
    right = all_sequences(node.right)
    for le in left:
        for re in right:
            weaved = []
            weave_lists(le, re, weaved, prefix)
            result.extend(weaved)
    
    return result


def weave_lists(first, second, weaved, prefix):
    if not first or not second:
        weaved.append(prefix + first + second)
        return
    # Recurse with the head of the first list added to the prefix
    head_first = first[0]
    weave_lists(first[1:], second, weaved, prefix + [head_first])

    # Recurse with the head of the second list added to the prefix
    head_second = second[0]
    weave_lists(first, second[1:], weaved, prefix + [head_second])
    



tree = TreeNode(2)
tree.left = TreeNode(1)
tree.right = TreeNode(3)

ans = all_sequences(tree)
print(ans)