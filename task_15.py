def ten_to_bin(x: int) -> str:
    """
    Recursively converts a natural number x from decimal to binary.
    Returns the binary representation as a string.
    """
    def helper(n: int) -> str:
        """
        Helper function to recursively
        build the binary representation.
        """
        if n == 0:
            return ""
        return helper(n // 2) + str(n % 2)

    if x == 0:
        return "0"
    return helper(x)


def main() -> None:
    """
    Reads a natural number and prints
    its binary representation.
    """
    try:
        x = int(input())
        if x < 0:
            print("x must be a natural number.")
            return
        result = ten_to_bin(x)
        print(result)
    except ValueError:
        print("Invalid input.")


if __name__ == "__main__":
    main()
