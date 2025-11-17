def nod(a: int, b: int) -> int:
    """
    Recursively calculates the greatest common
    divisor of two natural numbers: a and b.
    """
    if b == 0:
        return a
    return nod(b, a % b)


def main() -> None:
    """
    Reads a and b, prints their 
    greatest common divisor.
    """
    try:
        a = int(input())
        b = int(input())
        if a <= 0 or b <= 0:
            print("a and b must be positive integers.")
            return
        result = nod(a, b)
        print(result)
    except ValueError:
        print("Invalid input.")


if __name__ == "__main__":
    main()
