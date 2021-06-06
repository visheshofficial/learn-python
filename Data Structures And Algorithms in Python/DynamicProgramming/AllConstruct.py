# def countConstruct(target, word_bank, memo={}):
#     if target in memo:
#         return memo[target]
#     if target == "":
#         return 1
#     count = 0
#     for word in word_bank:
#         if target.startswith(word):
#             result = countConstruct(target.replace(word, ""), word_bank)
#             count += result
#     memo[target] = count
#     return count


def allConstruct(target, word_bank):
    # print(target)
    if target == "":
        return [[]]
    result = []

    for word in word_bank:
        # s1=[]
        if target.startswith(word):
            suffix = target.replace(word, "")
            suffix_ways = allConstruct(suffix, word_bank)
            target_ways = []
            for x in suffix_ways:
                a = [suffix]

            result.append(target_ways)

            # if result == [] or result is not None:
            #     s1.append(word)
        # if s1:
        #     sub_array.append(s1)

    return result


if __name__ == '__main__':
    # print(countConstruct("purple", ["purp", "p", "ur", "le", "purpl"]))  # 2
    # print(countConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))  # 1
    # print(allConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"]))  # 4
    print(allConstruct("abcdefg", ["ab", "abc", "cd", "def", "abcd", "ef", "c"]))  # 4
    # print(countConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))  # 0
    # print(countConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))  # 4
    # print(countConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
    #                      ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"]))  # 0
