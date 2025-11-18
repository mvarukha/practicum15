def ten_to_n(x: int, n: int) -> str:
    """
    Recursively converts a natural number x
    from decimal to base n (2 <= n <= 16).
    Returns the result as a string.
    """
    if n < 2 or n > 16:
        raise ValueError("Base n must be between 2 and 16.")

    digits = "0123456789ABCDEF"

    def helper(num: int) -> str:
        """
        Helper function to recursively build the n-ary representation.
        """
        if num == 0:
            return ""
        return helper(num // n) + digits[num % n]  # Add a number to the result.

    if x == 0:
        return "0"
    return helper(x)


def main() -> None:
    """
    Reads x and n, prints the n-ary representation of x.
    """
    try:
        x = int(input())  # The number.
        n = int(input())  # The base of the number.
        if x < 0:  # Checking that x is a natural number.
            print("x must be a natural number.")
            return
        result = ten_to_n(x, n)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
