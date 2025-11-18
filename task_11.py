def ind_maxlist(a: list[int]) -> int:
    """
    Recursively finds the index of the
    maximum element in a list of integers.
    """
    def helper(index: int, max_index: int) -> int:
        """
        Helper function to recursively find
        the index of the maximum element.
        """
        if index == len(a):
            return max_index  # Reached end of list, return index of max element.
        if a[index] > a[max_index]:
            max_index = index
        return helper(index + 1, max_index)

    if not a:
        raise ValueError("List is empty.")
    return helper(1, 0)  # Start from index 1, with 0 as initial max index.


def main() -> None:
    """
    Reads a list of integers and prints
    the index of the maximum element.
    """
    try:
        a = list(map(int, input().split()))
        if not a:
            print("List is empty.")
            return
        result = ind_maxlist(a)
        print(result)
    except ValueError:
        print("Invalid input.")


if __name__ == "__main__":
    main()
