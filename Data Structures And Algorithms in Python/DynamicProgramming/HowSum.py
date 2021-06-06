# https://www.youtube.com/watch?v=oBt53YbR9Kk&t=1332s

# def howSum(target_sum, numbers, memo={}):
#     # print(target_sum)
#     if target_sum == 0:
#         return True
#     # if target_sum < 0:
#     #     return False
#     if target_sum in memo:
#         return memo[target_sum]
#     for number in numbers:
#         reminder = target_sum - number
#         if reminder >= 0:
#             if howSum(reminder, numbers, memo):
#                 return True
#     memo[reminder] = False
#     return False
def howSum(target_sum, numbers, memo={}):
    # print(target_sum)
    if target_sum in memo:
        return memo[target_sum]
    if target_sum == 0:
        return []
    if target_sum < 0:
        return None
    for number in numbers:
        remainder = target_sum - number
        result = howSum(remainder, numbers, memo)
        # print(result)
        if result is not None:
            result.append(number)
            memo[target_sum] = result
            return memo[target_sum]

    memo[target_sum] = None
    return memo[target_sum]


# def howSum(target_sum, numbers):
#     if target_sum == 0:
#         return []
#     if target_sum < 0:
#         return None
#     for number in numbers:
#         remainder = target_sum - number
#         result = howSum(remainder, numbers)
#         if result is not None:
#             result.append(number)
#             return result
#     return None


if __name__ == '__main__':
    print(howSum(7, [2, 3], {}))  # [3,2,2]
    print(howSum(7, [5, 3, 4, 7], {}))  # [7] OR [3,4]
    print(howSum(7, [2, 4], {}))  # None
    print(howSum(8, [2, 3, 5], {}))  # [2,2,2,2] or [3,5]
    print(howSum(300, [7, 14], {})) # None
