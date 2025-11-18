def combin(n: int, k: int) -> int:
    """
    Recursively calculates the binomial coefficient
    C(n, k) = n!/(k!(n-k)!) without helper functions.
    """
    if k > n or k < 0:
        return 0  # If k > n or k < 0, C(n, k) = 0.
    if k == 0 or k == n:
        return 1  # If C(n, 0) = C(n, n) = 1.
    return combin(n - 1, k - 1) + combin(n - 1, k)  # Pascal's triangle formula.


def main() -> None:
    """
    Reads n and k, prints the binomial coefficient C(n, k).
    """
    try:
        n = int(input())
        k = int(input())
        if n < 0 or k < 0:
            print("n and k must be non-negative integers.")
            return
        result = combin(n, k)  # C(n, k).
        print(result)
    except ValueError:
        print("Invalid input.")


if __name__ == "__main__":
    main()
