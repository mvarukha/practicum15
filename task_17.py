def function1(x: int) -> int:
    """
    Recursively determines if a natural number x is prime.
    Returns 1 if prime, 0 otherwise.
    """
    if x < 2:
        return 0  # Bc numbers less than 2 are not prime.

    def is_prime(divisor: int) -> int:
        """
        Helper function to recursively
        check for divisors.
        """
        if divisor * divisor > x:
            return 1  # If the divisor is more than the root, x is prime.
        if x % divisor == 0:
            return 0  # The divisor has been found => x is not prime.
        return is_prime(divisor + 1)

    return is_prime(2)


def main() -> None:
    """
    Reads a natural number and prints
    1 if it is prime, otherwise 0.
    """
    try:
        x = int(input())
        if x < 0:
            print("x must be a natural number.")
            return
        result = function1(x)
        print(result)
    except ValueError:
        print("Invalid input.")


if __name__ == "__main__":
    main()
