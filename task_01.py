def pownum(a: float, n: int) -> float:
    """
    Recursively calculates a raised to the
    power of n using exponentiation by squaring.
    a is a real number, n is a natural number.
    """
    if n < 0:
        raise ValueError("n must be a natural number.")
    if n == 0:
        return 1  # Base case: a^0 = 1.
    half_n = n // 2  # Dividing the degree in half.
    half_power = pownum(a, half_n)  # Calculating a^(n//2).
    if n % 2 == 0:
        return half_power * half_power  # If n is even: (a^(n/2))^2.
    else:
        return a * half_power * half_power  # If n is odd: a * (a^((n-1)/2))^2.


def main() -> None:
    """
    Reads a and n, validates input,
    and prints the result of a^n.
    """
    try:
        a = float(input())  # Reading the base.
        n = int(input())  # Reading the degree.
        result = pownum(a, n)  # a^n.
        print(result)
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
