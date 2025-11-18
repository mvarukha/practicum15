def simmetr(s: str, i: int, j: int) -> bool:
    """
    Recursively checks if the substring s[i:j+1] is symmetric (palindrome).
    Returns True if symmetric, False otherwise.
    """
    if i >= j:
        return True  # If i >= j, the row is symmetric.
    if s[i] != s[j]:
        return False  # The row is not symmetrical.
    return simmetr(s, i + 1, j - 1)  # Checking the rest part of the row.


def main() -> None:
    """
    Reads a string and indices i, j, prints True if the substring is symmetric, otherwise False.
    """
    try:
        s = input()
        i = int(input())
        j = int(input())
        if i < 0 or j >= len(s) or i > j:  # Checking the correctness of the indexes.
            print("Invalid indexes.")
            return
        result = simmetr(s, i, j)
        print(result)
    except ValueError:
        print("Invalid input.")


if __name__ == "__main__":
    main()
