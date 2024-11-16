# Find words in a M*N grid, words can be spelled forwards or backwards but not diagonally
# Input:
# C A T
# C O T
# T U H
# words = ["CAT", "HUT", "TOM"] --> answer = [True, True, False]


from collections import deque


directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def is_word_in_grid(grid, word):
    first_char = word[0]
    source = (-1, -1)

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == first_char:
                source = (i, j)

    if(source == (-1, -1)):
        return False
    return grid_BFS(grid, word, source)


def is_valid_coordinate(x, y, grid):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0])

def grid_BFS(grid, word, source):
    queue = deque()
    visited = set()
    x, y = source
    queue.append((grid[x][y], source))
    visited.add(source)

    while queue:
        char, location = queue.popleft()
        x, y = location
        if len(word) == 0:
            return True
        if len(word) > 0 and char == word[0]:
            word = word[1:]
        if len(word) > 0 and char == word[-1]:
            word = word[:-2]
        for dx, dy in directions:
            new_x = x + dx
            new_y = y + dy
            if is_valid_coordinate(new_x, new_y, grid) and (new_x, new_y) not in visited:
                visited.add((new_x, new_y))
                queue.append((grid[new_x][new_y], (new_x, new_y)))

    return False


def find_words(grid, words):
    n = len(words)
    answer = [False] * n
    for i in range(len(words)):
        if is_word_in_grid(grid, words[i]):
            answer[i] = True
    return answer

grid = [['C', 'A', 'T'], ['C', 'O', 'T'], ['T', 'U', 'H']]
words = ["CAT", "HUT", "TOM"]

print(find_words(grid, words))
