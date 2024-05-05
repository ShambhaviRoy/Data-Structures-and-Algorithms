# Towers of Hanoi: In the classic problem of the Towers of Hanoi, you have 3 towers and N disks of
# different sizes which can slide onto any tower. The puzzle starts with disks sorted in ascending order
# of size from top to bottom (Le., each disk sits on top of an even larger one). You have the following
# constraints:
# (1) Only one disk can be moved at a time.
# (2) A disk is slid off the top of one tower onto another tower.
# (3) A disk cannot be placed on top of a smaller disk.
# Write a program to move the disks from the first tower to the last using Stacks.


class Tower:
    def __init__(self, i):
        self.disks = []
        self.index = i
    
    def add_to(self, d):
        if(len(self.disks) > 0):
            top = self.disks[-1]
            if(top <= d):
                print('Error')
        self.disks.append(d)

    def move_top_to(self, tower):
        top = self.disks.pop()
        tower.add_to(top)

    def move_disks(self, n, destination, buffer):
        if n <= 0:
            return 
        
        self.move_disks(n-1, buffer, destination)
        self.move_top_to(destination)
        buffer.move_disks(n-1, destination, self)


if __name__ == "__main__":
    towers = []
    for i in range(3):
        towers.append(Tower(i))

    for i in reversed(range(4)):
        towers[0].disks.append(i)


    print('Start:')
    print('Source: towers[0]:', towers[0].disks)
    print('Buffer: towers[1]:', towers[1].disks)
    print('Destination: towers[2]:', towers[2].disks)

    towers[0].move_disks(4, towers[2], towers[1])

    print('End:')
    print('Source: towers[0]:', towers[0].disks)
    print('Buffer: towers[1]:', towers[1].disks)
    print('Destination: towers[2]:', towers[2].disks)


    

            




