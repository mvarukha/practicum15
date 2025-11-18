def mod_number(a: int, b: int) -> int:
    """
    Recursively calculates the 
    remainder of a divided by b.
    a and b are natural numbers.
    """
    if a < b:
        return a  # Remainder is a.
    return mod_number(a - b, b)


def main() -> None:
    """
    Reads a and b, prints the 
    remainder of a divided by b.
    """
    try:
        a = int(input())  # Reads the dividend.
        b = int(input())  # Reads the divisor.
        if a < 0 or b <= 0:
            print("a must be non-negative, b must be positive.")
            return
        result = mod_number(a, b)  # Calculates the remainder.
        print(result)
    except ValueError:
        print("Invalid input.")


if __name__ == "__main__":
    main()
