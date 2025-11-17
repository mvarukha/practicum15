def odd_list(a: list[int], n: int) -> list[int]:
    """
    Recursively returns a list of even values
    from the first n elements of list a.
    Правда непонятно: в задании функция
    odd - по сути, нечетные числа,
    а функция требуется как к четным
    """
    def helper(index: int, result: list[int]) -> list[int]:
        """
        Helper function to recursively
        build the list of even numbers.
        """
        if index == n:
            return result
        if a[index] % 2 == 0:
            result.append(a[index])
        return helper(index + 1, result)

    return helper(0, [])


def main() -> None:
    """
    Reads a list of integers and n, prints the 
    list of even values from the first n elements.
    """
    try:
        a = list(map(int, input().split()))
        n = int(input())
        if n < 0 or n > len(a):
            print("n must be between 0 and the length of the list.")
            return
        result = odd_list(a, n)
        print(result)
    except ValueError:
        print("Invalid input.")


if __name__ == "__main__":
    main()
