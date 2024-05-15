# Stack of Boxes: You have a stack of n boxes, with widths Wi' heights hi' and depths d1• The boxes
# cannot be rotated and can only be stacked on top of one another if each box in the stack is strictly
# larger than the box above it in width, height. and depth. Implement a method to compute the
# height of the tallest possible stack. The height of a stack is the sum of the heights of each box.

from functools import cmp_to_key

class Box:
    def __init__(self, w, h, d):
        self.width = w
        self.height = h
        self.depth = d

    def compare(self, box):
        return self.height - box.height
    
    def can_be_above(self, bottom):
        return ((self.width < bottom.width) and
                (self.height < bottom.height) and 
                (self.depth < bottom.depth))
    

def create_tallest_stack(boxes):
    boxes = sorted(boxes, key = cmp_to_key(Box.compare))
    return create_stack(boxes, None, 0, [0]*len(boxes))

def create_stack(boxes, bottom, offset, stack_map):
    if offset >= len(boxes):
        return 0
    
    new_bottom = boxes[offset]
    height_with_bottom = 0
    
    if(not bottom or new_bottom.can_be_above(bottom)):
        if(stack_map[offset] == 0):
            stack_map[offset] = create_stack(boxes, new_bottom, offset+1, stack_map)
            stack_map[offset] += new_bottom.height
        height_with_bottom = stack_map[offset]

    height_without_bottom = create_stack(boxes, bottom, offset+1, stack_map)

    return max(height_with_bottom, height_without_bottom)


boxes = [Box(1, 1, 1), Box(2, 2, 2), Box(3, 3, 4), Box(5, 3, 2)]
print(create_tallest_stack(boxes))