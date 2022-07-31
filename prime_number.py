def isPrime(num):
    """
    This function takes in a number and tests to see if it's a prime number, returning true or false.
    
    Example: 
    Call the function with an integer like isPrime(31)
    
    """
    x = 2
    if num <= 0:
        num = (num * -1)

    while x <= (num - 1):
        if num % x != 0:
            x += 1
        else:
            return False

    if x == num:
        return True

# num = int(input("Is it a prime number? "))
# print(isPrime(num))