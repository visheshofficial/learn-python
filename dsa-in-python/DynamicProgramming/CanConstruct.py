def canConstruct(target, word_bank, memo={}):
    if target in memo:
        return memo[target]
    if target == "":
        return True

    for word in word_bank:
        if target.startswith(word):
            result = canConstruct(target.replace(word, ""), word_bank, memo)
            if result == True:
                memo[target] = True
                return True
    memo[target] = False
    return False


# def canConstruct(target, word_bank):
#     if target == "":
#         return True
#
#     for word in word_bank:
#         if target.startswith(word):
#             result = canConstruct(target.replace(word, ""), word_bank)
#             if result == True:
#                 return True
#     return False


if __name__ == '__main__':
    print(canConstruct("", ["ab", "abc", "cd", "def", "abcd"]))  # true
    print(canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))  # true
    print(canConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))  # false
    print(canConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))  # true
    print(canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
                       ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"]))  # false
