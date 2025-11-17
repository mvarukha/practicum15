def degree5(n: int) -> int:
    """
    Recursively checks if n is a power of 5.
    Returns the exponent if true, otherwise returns -1.
    """
    if n == 1:
        return 0  # 5^0 = 1
    if n % 5 != 0:
        return -1  # n is not divisible by 5, so not a power of 5.
    result = degree5(n // 5)
    if result == -1:
        return -1
    return result + 1


def main() -> None:
    """
    Reads n and prints the exponent if n 
    is a power of 5, otherwise prints -1.
    """
    try:
        n = int(input())
        if n <= 0:
            print("n must be a positive integer.")
            return
        result = degree5(n)
        print(result)
    except ValueError:
        print("Invalid input.")


if __name__ == "__main__":
    main()
