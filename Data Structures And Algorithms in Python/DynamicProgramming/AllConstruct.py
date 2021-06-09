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
        if target.startswith(word):
            suffix = target.replace(word, "")
            suffix_ways = allConstruct(suffix, word_bank)
            target_ways = []
            for x in suffix_ways:
                a = [word]
                a.extend(x)
                target_ways.append(a)
            if target_ways:
                result.extend(target_ways)

    return result

import pprint
if __name__ == '__main__':
    print(allConstruct("purple", ["purp", "p", "ur", "le", "purpl"]))  # 2
    # print(countConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))  # 1
    pprint.pprint(allConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"]))  # 4
    # print(allConstruct("abcdefg", ["ab", "abc", "cd", "def", "abcd", "ef", "c"]))  # 4
    # print(allConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))  # 0
    print(allConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))  # 1
    print(allConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee",
                         ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"]))  # 0
