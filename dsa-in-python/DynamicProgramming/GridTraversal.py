# https://www.youtube.com/watch?v=oBt53YbR9Kk&t=1332s


def grid_traversal(row, col, memo={}):
    key1 = f"{str(row)},{str(col)}"
    key2 = f"{str(col)},{str(row)}"
    if key1 in memo:
        return memo[key1]
    if key2 in memo:
        return memo[key2]
    if row == 0 or col == 0:
        return 0
    if row == 1 and col == 1:
        return 1
    result = grid_traversal(row - 1, col, memo) + grid_traversal(row, col - 1, memo)
    memo[key1] = result
    return memo[key1]


# def grid_traversal(row, col):
#     if row == 0 or col == 0:
#         return 0
#     if row == 1 and col == 1:
#         return 1
#     return grid_traversal(row - 1, col) + grid_traversal(row, col - 1)


if __name__ == '__main__':
    print(grid_traversal(1, 2))
    print(grid_traversal(2, 0))
    print(grid_traversal(2, 3))
    print(grid_traversal(3, 2))
    print(grid_traversal(3, 3))
    print(grid_traversal(18, 18))
