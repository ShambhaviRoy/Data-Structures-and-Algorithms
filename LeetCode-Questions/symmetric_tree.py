# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_palindrome(s):
    if s == []:
        return True
    return s == s[::-1]

def get_children(node):
    children = []
    if node:
        if node.left:
            children.append(node.left)
        else:
            children.append(TreeNode(val=-1))
        if node.right:
            children.append(node.right)
        else:
            children.append(TreeNode(val=-1))
    return children


def BFS(node):
    level = []
    level.append(node)
    while level:
        next_level = []
        for node in level:
            children = get_children(node)
            next_level.extend(children)
        level = next_level
        print('next_level:', [x.val for x in next_level])
        
        if all([x.val == -1 for x in next_level]):
                    return True
        elif is_palindrome([x.val for x in next_level]):
            print('next_level is palindrome')
        else:
            return False

    return True

# Approach 1: Iterative
# BFS to get each level- keep track of childrens' values- are they palindrome?
# Time Complexity = O(n), n = no. of nodes in tree
# Space Complexity = O(n)
def isSymmetricIterative(root) -> bool:
    return BFS(root)

# Approach 2: Recursive  
# Time Complexity = O(n), n = no. of nodes in tree
# Space Complexity = O(n)
def is_symmetric(root):
    return isSymmetricRecursive(root.left, root.right)

def isSymmetricRecursive(left, right):
    if not left and not right:
        return True
    if not left or not right:
        return False
    return (left.val == right.val) and isSymmetricRecursive(left.left, right.right) and isSymmetricRecursive(left.right, right.left)



root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(4)

print(isSymmetricIterative(root))
print(is_symmetric(root))


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)

print(isSymmetricIterative(root))
print(is_symmetric(root))

