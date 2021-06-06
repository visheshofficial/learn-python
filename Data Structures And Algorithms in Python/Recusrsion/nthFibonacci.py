'''
def fib(n: int) -> int:
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)

'''


def fib(n: int, memo={1: 0, 2: 1}) -> int:
    if n in memo:
        return memo[n]
    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]


def fib_iter(n: int) -> int:
    last_two = [0, 1]
    i = 3
    while i <= n:
        next_sum = last_two[0] + last_two[1]
        last_two[0] = last_two[1]
        last_two[1] = next_sum
        i += 1
    if n == 1:
        return last_two[0]
    return last_two[1]


import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(fib(6), 5)
        self.assertEqual(fib_iter(6), 5)



