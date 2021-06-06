def findThreeLargestNumbers(array):
    result = array[:3]
    result.sort()
    for index in range(3, len(array)):
        if array[index] > result[2]:
            shift_values(array, array[index], 2)
        elif array[index] > result[1]:
            shift_values(array, array[index], 1)
        elif array[index] > result[0]:
            shift_values(array, array[index], 0)
    return result


def shift_values(array, num, index):
    for i in range(index + 1):
        array[i] = array[i + 1]
    array[index] = num
