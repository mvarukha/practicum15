def pownum(a: float, n: int) -> float:
    """
    Recursively calculates a raised to the
    power of n using exponentiation by squaring.
    a is a real number, n is a natural number.
    """
    if n < 0:
        raise ValueError("n must be a natural number.")
    if n == 0:
        return 1
    half_n = n // 2
    half_power = pownum(a, half_n)
    if n % 2 == 0:
        return half_power * half_power
    else:
        return a * half_power * half_power


def main() -> None:
    """
    Reads a and n, validates input,
    and prints the result of a^n.
    """
    try:
        a = float(input())
        n = int(input())
        result = pownum(a, n)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
