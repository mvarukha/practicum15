def maxlist(a: list[int]) -> int:
    """
    Recursively finds the maximum element 
    in a list of integers using indices.
    """
    def helper(index: int, current_max: int) -> int:
        """
        Helper function to recursively find max using index.
        """
        if index == len(a):
            return current_max  # Reached end of list, return current max.
        return helper(index + 1, max(current_max, a[index]))  # Updates max and goes to next index.

    if not a:
        raise ValueError("List is empty.")
    return helper(1, a[0])  # Start from index 1, with first element as initial max.


def main() -> None:
    """
    Reads a list of integers and 
    prints the maximum element.
    """
    try:
        a = list(map(int, input().split()))
        if not a:
            print("Error: list is empty.")
            return
        result = maxlist(a)  # The maximum element.
        print(result)
    except ValueError:
        print("Invalid input.")


if __name__ == "__main__":
    main()
