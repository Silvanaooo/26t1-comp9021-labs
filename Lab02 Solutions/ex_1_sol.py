"""
Continuously prompts the user for a floating-point number between -1 and 1 (excluded).
- Must be something that float() accepts but int() would not (so it should contain a '.').
- Keeps asking until the input is valid.
- Finally prints the number rounded to 2 decimal places (with tolerance ±0.005).
"""
#Loop until valid input is received
while True:
    try:
        # Prompt user for input
        x = input('Enter a number strictly between -1 and 1 '
                      '(max 2 decimal places): ')
        # check e
        if 'e' in x.lower():
            raise ValueError
        # Check: must contain a decimal point
        if '.' in x:
            parts = x.split('.')
            if len(parts) != 2 or len(parts[1]) > 2:
                raise ValueError

        # Convert to float
        x = float(x)

        # Check: must be strictly between -1 and 1
        if not (-1 < x < 1):
            raise ValueError

        # Valid input, stop loop
        break
    except ValueError:
        # If any check fails, ask again
        print('You got that wrong, try again!\n')

# Format the result to 2 decimal places
print(f'\nYou entered {x:.2f} (rounded to two decimal places)')
