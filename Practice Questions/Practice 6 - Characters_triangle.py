import string
from itertools import cycle
"""
More pattern problems, see
https://www.geeksforgeeks.org/c/pattern-programs-in-c/
https://www.geeksforgeeks.org/dsa/pattern-printing-problems/?utm_source=chatgpt.com
https://www.hackerrank.com/contests/pattern-programs/challenges
"""

def solution_6_1():
    """
    Prompts the user for a strictly positive integer n and prints a character triangle of height n.
    This version constructs each line by explicitly adding spaces on the left (using string
    multiplication).

    Example:
        Input: 4
        Output:
               A
              BCB
             DEFED
            GHIJIHG
    """
    n = int(input("Enter a strictly positive integer: "))

    letters = string.ascii_uppercase  # Alphabet A–Z
    iterator = cycle(letters)  # Cycle through alphabet indefinitely
    lines = []

    for i in range(1, n + 1):
        # Build ascending part of row
        line = ""
        for letter in range(i):
            line += next(iterator)
        # [:-1] removes the last letter — because slice stops before the end index.
        # [::-1] reverses the sequence — because a negative step means go backward.
        # Together they make a mirrored pattern, like “ABC” → “ABCBA”.
        line += line[:-1][::-1]
        # Prepend spaces for triangle alignment
        line = " " * (n - i) + line
        lines.append(line)

    for line in lines:
        print(line)


def solution_6_2():
    """
    Prompts the user for a strictly positive integer n and prints a character triangle of height n.
    This version uses str.center() to automatically align the triangle to the center.
    """
    n = int(input("Enter a strictly positive integer: "))

    letters = string.ascii_uppercase
    iterator = cycle(letters)
    lines = []
    spaces = n * 2 - 1 # total width of the last line

    for i in range(1, n + 1):
        # Build row
        # "".join() accepts any iterable, so we can use a generator expression
        # without creating an intermediate list
        line = "".join(next(iterator) for _ in range(i))
        line = line + line[:-1][::-1]
        # Center the string with spaces
        lines.append(line.center(spaces))
        # Or you can use format with ^ to center text
        # lines.append(format(line, f"^{spaces}"))

    for line in lines:
        print(line.rstrip())


"""
#############################################
###              EXTRA QUESTION            ###
#############################################

Problem 1:
    By default the triangle starts from 'A'.
    But what if it should start from ANY given
    uppercase letter (e.g., 'K', 'Z')?

Problem 2:
What if instead of letters, the triangle
should be printed with DIGITS (0–9)?
e.g., rows using 12321, 4567654, etc.

Think about:
    - Use ord() to convert characters to numbers.
    - gap = ord(starting_from) - ord('A').
    - Generate letters with:
          chr(ord('A') + (gap + step) % 26)
    - This way, after 'Z' it wraps back to 'A'.

#############################################
###           END OF EXTRA HINT            ###
#############################################
"""

def print_letter_triangle(height: int, starting_from: str = 'A') -> None:
    """
    Print a symmetric triangle of letters.
    The first row starts from `starting_from`, and letters wrap around after 'Z'.

    Example:
        >>> print_letter_triangle(1, 'A')
        A

        >>> print_letter_triangle(2, 'A')
         A
        BCB

        >>> print_letter_triangle(3, 'A')
          A
         BCB
        CDEDC

        >>> print_letter_triangle(3, 'K')
          K
         LML
        MNONM

        >>> print_letter_triangle(4, 'Y')
           Y
          ZAZ
         ABCBA
        BCDEDCB

        >>> print_letter_triangle(3, 'Z')
          Z
         ABA
        BCDCB
    """
    pass

def print_digit_triangle(height: int, starting_from: int = 0) -> None:
    """
    Print a symmetric triangle of digits.
    Digits wrap around after 9.

    Example:
        >>> print_digit_triangle(1, 0)
        0

        >>> print_digit_triangle(2, 0)
         0
        121

        >>> print_digit_triangle(3, 0)
          0
         121
        23432

        >>> print_digit_triangle(3, 5)
          5
         676
        78987

        >>> print_digit_triangle(4, 8)
           8
          909
         01210
        1234321

        >>> print_digit_triangle(3, 9)
          9
         010
        12321
    """
    pass