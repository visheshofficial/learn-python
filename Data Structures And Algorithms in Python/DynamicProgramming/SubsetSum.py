"""

Given a set of non-negative integers, and a value sum,
determine if there is a subset of the given set with sum equal to given sum.

"""


# Driver code
def isSubsetSum(array, array_length, total):
    dp = [[False for i in range(total + 1)] for i in range(array_length + 1)]

    for i in range(array_length + 1):
        dp[i][0] = True

    for row in (dp):
        print(row)

    for array_size in range(1, array_length + 1):
        for cur_total in range(1, total + 1):
            if array[array_size - 1] <= cur_total:
                dp[array_size][cur_total] = dp[array_size - 1][cur_total - array]  # or dp[]
            else:
                dp[array_size][cur_total] = dp[array_size - 1][cur_total - array]

    return dp[array_length][total]


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
