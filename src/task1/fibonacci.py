from time import perf_counter_ns

from src.utils.decorators import memoized


def recursive_fibonacci(x):
    if x in {0, 1}:
        return x
    return recursive_fibonacci(x - 1) + recursive_fibonacci(x - 2)


def iterative_fibonacci(x):
    prev, res = 0, 1
    for _ in range(2, x + 1):
        prev, res = res, res + prev
    return res


@memoized
def cached_fibonacci(x):
    return iterative_fibonacci(x)


if __name__ == "__main__":
    n = 20

    tick = perf_counter_ns()
    print(recursive_fibonacci(n))
    print(perf_counter_ns() - tick)
    print("\n")

    tick = perf_counter_ns()
    print(iterative_fibonacci(n))
    print(perf_counter_ns() - tick)
    print("\n")

    tick = perf_counter_ns()
    print(cached_fibonacci(n))
    print(perf_counter_ns() - tick)
