# https://www.youtube.com/watch?v=oBt53YbR9Kk&t=1332s

def bestSum(target_sum, numbers, memo={}):
    print(target_sum)
    if target_sum in memo:
        return memo[target_sum]
    if target_sum == 0:
        return []
    if target_sum < 0:
        return None
    shortest_result = None
    for number in numbers:
        remainder = target_sum - number
        result = bestSum(remainder, numbers, memo)
        if result is not None:
            combination = result + [number]
            if shortest_result is None or (len(combination) < len(shortest_result)):
                shortest_result = combination
    memo[target_sum] = shortest_result  # if shortest_result is not None else None
    return shortest_result


# def bestSum(target_sum, numbers):
#     if target_sum == 0:
#         return []
#     if target_sum < 0:
#         return None
#
#     shortest_result = None
#     for number in numbers:
#         remainder = target_sum - number
#         result = bestSum(remainder, numbers)
#         if result is not None:
#             result.append(number)
#             if shortest_result is None or len(result) < len(shortest_result):
#                 shortest_result = result
#
#     return shortest_result


if __name__ == '__main__':
    # print(bestSum(7, [2, 3], {}))  # [3,2,2]
    # print(bestSum(7, [5, 3, 4, 7], {}))  # [7]
    # print(bestSum(7, [2, 4], {}))  # None
    # print(bestSum(8, [2, 5, 3], {}))  # [3,5]
    # print(bestSum(8, [1, 4, 5], {}))  # [4,4]
    print(bestSum(100, [1, 2, 5, 25], {}))  # [25,25,25,25]
