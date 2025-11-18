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
            return 0  # Reached the end of the list, x not found.
        if a[index] == x:
            return 1  # Found x, return 1.
        return helper(index + 1)  # To the next element.

    if not a:
        return 0  # If the list is empty, x is not found.
    return helper(0)  # Start searching from index 0.


def main() -> None:
    """
    Reads a list of integers and a number x,
    prints 1 if x is in the list, otherwise 0.
    """
    try:
        a = list(map(int, input().split()))  # Read the list of integers.
        x = int(input())  # Read the number x.
        result = search(a, x)  # Check if x exists in the list.
        print(result)
    except ValueError:
        print("Invalid input.")


if __name__ == "__main__":
    main()
