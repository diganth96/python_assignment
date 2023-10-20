def calculate_sum_of_digits(number):
    sum_of_digits = 0
    while number > 0:
        digit = number % 10
        sum_of_digits += digit
        number //= 10
    return sum_of_digits
num = int(input("Enter a number: "))
while num >= 10:
    num = calculate_sum_of_digits(num)
print("Final Output:", num)
