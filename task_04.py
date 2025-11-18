def sum_progress(a1: float, r: float, n: int) -> float:
    """
    Recursively calculates the sum of the first 
    n terms of an arithmetic progression.
    a1 is the first term, r is the common 
    difference, n is the number of terms.
    """
    if n == 1:
        return a1  # Returns the first term.
    current_term = a1 + (n - 1) * r  # Calculate the n-th term of progression.
    return current_term + sum_progress(a1, r, n - 1)  # Add current term and recurse for the rest.


def main() -> None:
    """
    Reads a1, r, and n, prints the sum of the
    first n terms of the arithmetic progression.
    """
    try:
        a1 = float(input())  # Reads the first term.
        r = float(input())  # Reads the common difference.
        n = int(input())  # Reads the number of terms.
        if n < 1:
            print("n must be a positive integer.")
            return
        result = sum_progress(a1, r, n)  # Calculates the sum of first n terms.
        print(result)
    except ValueError:
        print("Invalid input.")


if __name__ == "__main__":
    main()
