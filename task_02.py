def count(n: int) -> int:
    """
    Recursively calculates the number
    of digits in a natural number n.
    """
    if n < 10:
        return 1  # Base case: if n < 10, then it has 1 digit.
    return 1 + count(n // 10)  # We add 1 and move on to the next digit.


def main() -> None:
    """
    Reads a natural number and
    prints the count of its digits.
    """
    try:
        n = int(input())
        if n < 0:
            print("n must be a natural number.")
            return
        # In case "n = 0".
        if n == 0:
            print(1)  # The number 0 is one digit.
            return
        result = count(n)
        print(result)
    except ValueError:
        print("Invalid input.")  # Обрабатываем ошибку ввода.


if __name__ == "__main__":
    main()
