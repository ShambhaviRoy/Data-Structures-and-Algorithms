# Given two (singly) linked lists, determine if the two lists intersect. 
# Return the intersecting node. Note that the intersection is defined based on reference, not value. That is, if the kth
# node of the first linked list is the exact same node (by reference) as the jth node of the second
#linked list, then they are intersecting

from linked_list import LinkedList
    
    
    
def intersection(l1, l2):
    len1 = l1.lengthList()
    len2 = l2.lengthList()
    print(len1)
    print(len2)

    
    diff = 0
    if len1 > len2:
        longer = l1
        shorter = l2
        
    else:
        longer = l2
        shorter = l1
    
    print(longer.head.data)
    print(shorter.head.data)
    
    diff = longer.lengthList() - shorter.lengthList()
    print('diff:',diff)
    
    last1 = l1.getLastNode()
    last2 = l2.getLastNode()
    
    print(last1.data)
    print(last2.data)
    
    if last1!= last2:
        return None
    
    longerHead = longer.head
    print(longerHead.data)
    
    while diff > 0:
        diff = diff - 1
        longerHead = longerHead.next
        
    shorterHead = shorter.head
    print(shorterHead.data)
    
    while longerHead != shorterHead:
        longerHead = longerHead.next
        shorterHead = shorterHead.next
        
    return longerHead
    
    


    
l1 = LinkedList()
l1.append(7)
l1.append(1)
l1.append(6)
l1.append(5)
l1.append(2)
l1.append(3)

l2 = LinkedList()
l2.append(4)
l2.append(8)
l2.append(5)
l2.append(2)
l2.append(3)


if intersection(l1, l2) == None:
    print('No intersection')
else:
    print('Intersection')

         
        
            
        
        
        
            
        
