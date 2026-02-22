def f1_1(m: int, n: int) -> str:
    """
    Creates a pattern of m segments,
    each containing a pair of vertical bars with n underscores between them.
    """
    return ("|" + "_" * n + "|") * m


def f1_2(m: int, n: int) -> str:
    """
    Creates a pattern of m segments, each containing a pair of vertical bars with n underscores between them.
    Implements the solution using a for loop and string concatenation.
    """
    result = ""
    for _ in range(m):
        result += "|" + "_" * n + "|"
    return result
