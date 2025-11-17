def count(a: int, b: int) -> int:
    """
    Recursively calculates the number of squares
    that can be cut from a rectangle of size a x b.
    Each time the largest possible square is cut.
    """
    if a == 0 or b == 0:
        return 0  # If one of the sides = 0, no more squares can be cut off.
    if a < b:
        a, b = b, a  # We swap them so that a >= b.
    return 1 + count(a - b, b)  # We cut off a square b x b, and continue with the remaining part.


def main() -> None:
    """
    Reads sides a and b, prints the number of squares that can be cut.
    """
    try:
        a = int(input())
        b = int(input())
        if a <= 0 or b <= 0:
            print("a and b must be positive integers.")
            return
        result = count(a, b)
        print(result)
    except ValueError:
        print("Invalid input.")


if __name__ == "__main__":
    main()
