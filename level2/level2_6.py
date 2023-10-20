def is_power_of_two(n):
    if n == 1:
        return True
    elif n % 2 == 0 and n > 0:
        return is_power_of_two(n // 2)
    else:
        return False
num = int(input("Enter a number: "))

if is_power_of_two(num):
    print(num, "is a power of two.")
else:
    print(num, "is not a power of two.")
