def mod_number(a: int, b: int) -> int:
    """
    Recursively calculates the 
    remainder of a divided by b.
    a and b are natural numbers.
    """
    if a < b:
        return a
    return mod_number(a - b, b)


def main() -> None:
    """
    Reads a and b, prints the 
    remainder of a divided by b.
    """
    try:
        a = int(input())
        b = int(input())
        if a < 0 or b <= 0:
            print("Error: a must be non-negative, b must be positive.")
            return
        result = mod_number(a, b)
        print(result)
    except ValueError:
        print("Error: invalid input.")


if __name__ == "__main__":
    main()
