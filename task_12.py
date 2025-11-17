def search(a: list[int], x: int) -> int:
    """
    Recursively checks if x exists in the list a.
    Returns 1 if found, 0 otherwise.
    """
    def helper(index: int) -> int:
        """
        Helper function to recursively
        search for x using index.
        """
        if index == len(a):
            return 0
        if a[index] == x:
            return 1
        return helper(index + 1)

    if not a:
        return 0
    return helper(0)


def main() -> None:
    """
    Reads a list of integers and a number x,
    prints 1 if x is in the list, otherwise 0.
    """
    try:
        a = list(map(int, input().split()))
        x = int(input())
        result = search(a, x)
        print(result)
    except ValueError:
        print("Error: invalid input.")


if __name__ == "__main__":
    main()
