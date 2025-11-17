def count(n: int) -> int:
    """
    Recursively calculates the number of digits in a natural number n.
    """
    if n < 10:
        return 1
    return 1 + count(n // 10)


def main() -> None:
    """
    Reads a natural number and prints the count of its digits.
    """
    try:
        n = int(input())
        if n < 0:
            print("Error: n must be a natural number.")
            return
        # In case "n = 0".
        if n == 0:
            print(1)
            return
        result = count(n)
        print(result)
    except ValueError:
        print("Error: invalid input.")


if __name__ == "__main__":
    main()
