# Paint Fill: Implement the "paint fill" function that one might see on many image editing programs.
# That is, given a screen (represented by a two-dimensional array of colors), a point, and a new color,
# fill in the surrounding area until the color changes from the original color.

from enum import Enum

class Color(Enum):
    WHITE = 0
    RED = 1
    BLUE = 2
    GREEN = 3
    YELLOW = 4



def fill_paint(screen, point, new_color):
    row, col = point
    if screen[row][col] == new_color:
        return False
    return fill_points(screen, row, col, screen[row][col], new_color)



def fill_points(screen, row, col, old_color, new_color):
    if row < 0 or row >= len(screen) or col < 0 or col >= len(screen[0]):
        return False
    
    if screen[row][col] == old_color:
        screen[row][col] = new_color
        fill_points(screen, row-1, col, old_color, new_color)
        fill_points(screen, row+1, col, old_color, new_color)
        fill_points(screen, row, col-1, old_color, new_color)
        fill_points(screen, row, col+1, old_color, new_color)

    return True



    
    

screen = [[Color.RED, Color.RED, Color.RED, Color.RED],
          [Color.BLUE, Color.BLUE, Color.RED, Color.RED],
          [Color.RED, Color.RED, Color.GREEN, Color.GREEN],
          [Color.RED, Color.YELLOW, Color.RED, Color.YELLOW]]

print(fill_paint(screen, (2, 2), Color.YELLOW))
    
for row in screen:
    print(row)