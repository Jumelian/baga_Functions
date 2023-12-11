print(" ")
print(" ")
print(" ")
print("problem: create a Python program that displays all prime numbers within a range.")
print(" ")
print(" ")
print("RULES TO CONSIDER:")
print("[1] if the number (start) is a negative number, the program will prompt a message [Enter a non-negative number].")
print("[2] if the number (end) is less than the number (start), the program will prompt a message [Enter a number greater than number (start)].")
print("[3] lastly, if the user enters the number [0], the program will terminate.")
print(" ")
print(" ")
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True
def smallest_factor(n):
    if n < 2:
        return None
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return i
    return n
def prime_numbers_in_range(start, end):
    return [number for number in range(start, end + 1) if is_prime(number)]
while True:
    print("\noptions:")
    print("1.find the smallest factor number.")
    print("2.find prime the numbers range.")
    print("3.Exit")
    print(" ")
    choice = input("enter your choice (1, 2, or 3): ")
    if choice == '1':
        n = int(input("enter a number to find its smallest factor: "))
        result = smallest_factor(n)
        print(f"the smallest factor of {n} is: {result}")
    elif choice == '2':
        start = int(input("enter the start of the range: "))
        end = int(input("enter the end of the range: "))
        prime_numbers = prime_numbers_in_range(start, end)
        print(f"prime numbers between {start} and {end} are: {', '.join(map(str, prime_numbers))}")
    elif choice == '3':
        print("program terminated.")
        break
    else:
        print("invalid choice. please enter 1, 2, or 3.")