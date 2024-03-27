def canSum(target_sum, numbers, memo={}):
    # print(target_sum)
    if target_sum == 0:
        return True
    # if target_sum < 0:
    #     return False
    if target_sum in memo:
        return memo[target_sum]
    for number in numbers:
        reminder = target_sum - number
        if reminder >= 0:
            if canSum(reminder, numbers, memo):
                return True
    memo[reminder]=False
    return False


# def canSum(target_sum, numbers):
#     if target_sum == 0:
#         return True
#     if target_sum < 0:
#         return False
#     for number in numbers:
#         if canSum(target_sum - number, numbers) == True:
#             return True
#     return False


if __name__ == '__main__':
    print(canSum(7, [2, 3]))
    print(canSum(7, [5, 3, 4, 7]))
    print(canSum(7, [2, 4]))
    print(canSum(8, [2, 3, 5]))
    print(canSum(300, [7, 14]))
