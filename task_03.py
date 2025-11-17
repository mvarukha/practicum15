def progress(a1: float, r: float, n: int) -> float:
    """
    Recursively calculates the n-th term of an arithmetic progression.
    a1 is the first term, r is the common difference, n is the term number.
    """
    if n == 1:
        return a1
    return r + progress(a1, r, n - 1)


def main() -> None:
    """
    Reads a1, r, and n, prints the n-th term of the arithmetic progression.
    """
    try:
        a1 = float(input())
        r = float(input())
        n = int(input())
        if n < 1:
            print("Error: n must be a positive integer.")
            return
        result = progress(a1, r, n)
        print(result)
    except ValueError:
        print("Error: invalid input.")


if __name__ == "__main__":
    main()
