def fibonacci(n):
    if n <= 0:
        return "Input should be a positive integer"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


dic = {}


def fibonacci_with_DP(n):
    if n <= 0:
        return "Input should be a positive integer"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        if n in dic:
            return dic[n]
        else:
            result = fibonacci_with_DP(n - 1) + fibonacci_with_DP(n - 2)
            dic[n] = result
            return result


# print(fibonacci(100))
print(fibonacci_with_DP(100))
