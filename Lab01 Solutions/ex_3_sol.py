def f3_1(L: list[int]) -> None:
    """
    Removes elements from L using a while loop and remove method.
    Checks from right to left, removing elements smaller than their successors.
    """
    while len(L) > 1 and L[-2] < L[-1]:
        L.remove(L[-2])
    print(L)


def f3_2(L: list[int]) -> None:
    """
    Removes elements from L using a while loop and remove method.
    Checks from right to left, removing elements smaller than their successors.
    Uses TWO loops (one backward scan + one filter) but overall O(n).
    Prints the filtered list.
    """
    e = L[-1]  # last element
    to_delete = set()  # values to remove

    # collect suffix values < e
    i = len(L) - 2
    while i >= 0 and L[i] < e:
        to_delete.add(L[i])
        i -= 1

    # filter them out from the list
    result = [x for x in L if x not in to_delete]
    print(result)
