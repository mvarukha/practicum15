def fib(k: int) -> int:
    """
    Recursively calculates the k-th Fibonacci number.
    k is a natural number (1-based index).
    """
    if k <= 2:
        return 1
    return fib(k - 1) + fib(k - 2)


def main() -> None:
    """
    Reads k and prints the k-th Fibonacci number.
    """
    try:
        k = int(input())
        if k < 1:
            print("k must be a positive integer.")
            return
        result = fib(k) # The k-th F. number.
        print(result)
    except ValueError:
        print("Invalid input.")


if __name__ == "__main__":
    main()
