def countConstruct(target, word_bank, memo={}):
    if target in memo:
        return memo[target]
    if target == "":
        return 1
    count = 0
    for word in word_bank:
        if target.startswith(word):
            result = countConstruct(target.replace(word, ""), word_bank)
            count += result
    memo[target] = count
    return count


# def countConstruct(target, word_bank):
#     print(target)
#     if target == "":
#         return 1
#     count = 0
#     for word in word_bank:
#         if target.startswith(word):
#             result = countConstruct(target.replace(word, ""), word_bank)
#             count += result
#     return count


if __name__ == '__main__':
    # print(countConstruct("purple", ["purp", "p", "ur", "le", "purpl"]))  # 2
    # print(countConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))  # 1
    # print(countConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd","ef","c"]))  # 1
    print(countConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))  # 0
    print(countConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))  # 1
    # print(countConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
    #                      ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"]))  # 0
