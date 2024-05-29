# Find Duplicates: You have an array with all the numbers from 1 to N, where N is at most 32,000. The
# array may have duplicate entries and you do not know what N is. With only 4 kilobytes of memory
# available, how would you print all duplicate elements in the array?

class BitSet:
    def __init__(self, size):
        self.bitset = [0]*size

    def set_bit(self, i):
        self.bitset[i] = 1

    def get_bit(self, i):
        return self.bitset[i]
    

if __name__ == "__main__":
    bitset = BitSet(32000)

    arr = [1, 4, 5, 6, 8, 90, 30, 20, 30, 3200]

    for i in range(len(arr)):
        num = arr[i]
        if bitset.get_bit(num-1) == 1:
            print(num)
        else:
            bitset.set_bit(num-1)