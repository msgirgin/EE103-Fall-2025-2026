name = input("Enter a name: ")
number_string = input("Enter a number: ")

sum_of_even_digits = 0

for char in number_string:
    digit_int = int(char)
    if digit_int % 2 == 0:
        sum_of_even_digits = sum_of_even_digits + digit_int

last_digit = sum_of_even_digits % 10

print(f"Sum of even digits: {sum_of_even_digits}")
print(f"Last digit of the sum is: {last_digit}")

for i in range(last_digit):
    print(name)