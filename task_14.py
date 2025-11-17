def numbers(x: int) -> None:
    """
    Recursively prints the digits of a natural
    number x in reverse order, one per line.
    """
    if x < 10:
        print(x)
        return
    print(x % 10)
    numbers(x // 10)


def main() -> None:
    """
    Reads a natural number and prints
    its digits in reverse order.
    """
    try:
        x = int(input())
        if x < 0:
            print("x must be a natural number.")
            return
        if x == 0:
            print(0)
            return
        numbers(x)
    except ValueError:
        print("Invalid input.")


if __name__ == "__main__":
    main()
