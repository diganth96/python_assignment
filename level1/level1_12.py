num = int(input("Enter a number: "))
revnum = 0
temp = num
while temp > 0:
    last_digit = temp % 10
    revnum = revnum * 10 + last_digit
    temp = temp // 10
print("Reversed number:", revnum)