import sys


def collatz_length(n):
    length = 1
    while n != 1:
        if n % 2 == 1:
            n = 3 * n + 1
        else:
            n = n // 2
        length += 1
    return length


def max_collatz_length(m, n):
    if m > n:
        m, n = n, m

    max_length = 0
    for i in range(m, n + 1):
        current_length = collatz_length(i)
        max_length = max(max_length, current_length)

    return max_length


if __name__ == "__main__":
    for line in sys.stdin:
        m, n = map(int, line.split())
        result = max_collatz_length(m, n)
        print(f'{m} {n} {result}')
