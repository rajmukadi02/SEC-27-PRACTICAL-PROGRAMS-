def sum_list(numbers):
    total = 0
    for num in numbers:
        total = total + num
    return total

my_list = [10, 20, 30, 40, 50]
result = sum_list(my_list)

print("List:", my_list)
print("Sum of all numbers:", result)
