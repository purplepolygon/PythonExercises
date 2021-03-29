# Take all even valued terms under 1,000,000 in a Fibonacci sequence, and sum them.
first_number = 1
second_number = 2
third_number = 0
count = 0
while third_number < 1000000:
    if second_number % 2 == 0:
        count = count + second_number
    third_number = first_number + second_number
    first_number = second_number
    second_number = third_number

print(count)
