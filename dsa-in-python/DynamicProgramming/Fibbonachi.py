def Fib(n, memo=dict()):
    if n in memo:
        return memo[n]
    if n <= 1:
        return 1
    memo[n] = Fib(n - 1,memo) + Fib(n - 2,memo)
    return memo[n]


if __name__ == '__main__':
    # for n in range(10):
    #     print(Fib(n))

    print(Fib(50))
