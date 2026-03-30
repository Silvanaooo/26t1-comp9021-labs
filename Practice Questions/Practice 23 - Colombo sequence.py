def colombo(n: int) -> list:
    """
    Generates the first n terms of the Colombo sequence (also known as the Golomb sequence).

    The Colombo sequence is self-descriptive:
    - It starts with 1, 2, 2
    - Each integer i appears in the sequence exactly sequence[i - 1] times
      (meaning the i-th term gives the count of how many times i occurs)

    Example:
        colombo(10) → [1, 2, 2, 3, 3, 4, 4, 4, 5, 5]

    :param n: Number of terms to generate (positive integer)
    :return: A list containing the first n terms of the Colombo sequence
    """
    # Initialize the sequence with the first few known values.
    # The sequence must start with [1, 2, 2] to follow the self-descriptive pattern.
    sequence = [1, 2, 2]

    # Start constructing from number 3 onward
    i = 3

    # Keep extending the sequence until its length reaches n
    # For each integer i, repeat it 'sequence[i - 1]' times.
    # Example: sequence[2] == 2 → append two 3s.
    while len(sequence) < n:
        sequence.extend([i] * sequence[i - 1])
        i += 1

    # Return only the first n terms in case we generated more.
    return sequence[:n]