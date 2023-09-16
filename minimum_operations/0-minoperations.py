def minOperations(n):
    if n <= 1:
        return 0  # If n is less than or equal to 1, no operations are needed, so return 0

    operations = 0  # Initialize the number of operations to 0
    factor = 2  # Start with the smallest prime factor

    while factor <= n:
        if n % factor == 0:  # Check if the current factor divides n evenly
            operations += factor  # Add the factor to the number of operations
            n //= factor  # Divide n by the factor to reduce it
        else:
            factor += 1  # If the current factor does not divide n, move to the next factor

    return operations  # Return the total number of operations needed
