# def ns(a,b):
#     if a>b:
#         print("a is bigger")
#     else:
#         print("b is smaller")

# ns(2,8)

# write  a 
# def power(a,b):
#     n=a**b
#     print(n)
#     return n
# a=int(input("enter the value of base"))    
# b=int(input("power"))
# power(a,b)

# prime
def is_prime(n):
    # 0 and 1 are not prime numbers
    if n < 2:
        print(f"{n} is not prime")
        return

    # Check for divisors from 2 up to n-1
    for i in range(2, n):
        if n % i == 0:
            # Found a divisor, so it's not prime.
            # We can stop checking immediately.
            print(f"{n} is not prime")
            return  # Exit the function

    # If the loop finished without finding any divisors,
    # then the number must be prime.
    print(f"{n} is prime")

# Get input from the user
try:
    n = int(input("Enter a number: "))
    is_prime(n)
except ValueError:
    print("Please enter a valid whole number.")