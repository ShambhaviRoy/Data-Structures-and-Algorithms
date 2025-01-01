# Check Subtree: T1 and T2 are two very large binary trees, with T1 much bigger than T2. Create an
# algorithm to determine if T2 is a subtree of T1.
# A tree T2 is a subtree of T1 if there exists a node n in T1 such that the subtree of n is identical to T2.
# That is, if you cut off the tree at node n, the two trees would be identical.

# Assume T1 has n nodes and T2 has m nodes, then n >> m

# Approach 1: Compare pre-order traversals of both trees, if smaller tree's traversal is a substring of the bigger tree's traversal, it's a subtree
# Time Complexity = O(n+m)
# Space Complexity = O(n+m)
def get_order_string(root, order):
    if not root:
        order += 'X'
        return
    order += root.value
    get_order_string(root.left, order)
    get_order_string(root.right, order)
    

def check_subtree_1(t1, t2):
    if not t2:
        return True
    order1 = get_order_string(t1, '')
    order2 = get_order_string(t2, '')
    return order2 in order1

    
# Approach 2: Traverse t1 to find a node equal to t2's root, then check whether that node's subtree matches t2
# Time Complexity = O(mn) --> actually it is O(n + km) where k is the no. of occurrences of T2's root in T1
# Space Complexity = O(log m + log n)
def contains_tree(t1, t2):
    if not t2:
        return True
    return subtree(t1, t2)

def subtree(t1, t2):
    if not t1:
        return False
    elif(t1.value == t2.value and match_tree(t1, t2)):
        return True
    return subtree(t1.left, t2) or subtree(t1.right, t2)

def match_tree(t1, t2):
    if not t1 and not t2:
        return True
    elif not t1 or not t2:
        return False
    elif t1.value != t2.value:
        return False
    else:
        return match_tree(t1.left, t2.left) and match_tree(t1.right, t2.right) 

    


