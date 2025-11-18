def progress(a1: float, r: float, n: int) -> float:
    """
    Recursively calculates the n-th term of an arithmetic progression.
    a1 is the first term, r is the common difference, n is the term number.
    """
    if n == 1:
        return a1  # The first term.
    return r + progress(a1, r, n - 1)  # Add the common difference and recurse to the previous term.


def main() -> None:
    """
    Reads a1, r, and n, prints the n-th term of the arithmetic progression.
    """
    try:
        a1 = float(input())  # Reads the first term.
        r = float(input())  # Reads the common difference.
        n = int(input())  # Reads the term number.
        if n < 1:
            print("n must be a positive integer.")
            return
        result = progress(a1, r, n)
        print(result)
    except ValueError:
        print("Invalid input.")


if __name__ == "__main__":
    main()
