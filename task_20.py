def comp(a: str, b: str, m: int, n: int) -> int:
    """
    Recursively calculates the length of the longest
    common subsequence (LCS) of two strings a and b.
    m and n are the lengths of the strings a and b respectively.
    """
    if m == 0 or n == 0:
        return 0  # If one of the lines is empty, LCS = 0.
    if a[m - 1] == b[n - 1]:
        # If the last characters match, add 1 and move on.
        return 1 + comp(a, b, m - 1, n - 1)
    else:
        # If they don't match, we check both options and choose the maximum.
        return max(comp(a, b, m - 1, n), comp(a, b, m, n - 1))


def main() -> None:
    """
    Reads two strings and their lengths, prints the length of their LCS.
    """
    try:
        a = input()
        b = input()
        m = int(input())
        n = int(input())
        if len(a) != m or len(b) != n:
            print("Lengths do not match the input strings.")
            return
        result = comp(a, b, m, n)
        print(result)
    except ValueError:
        print("Invalid input.")


if __name__ == "__main__":
    main()
