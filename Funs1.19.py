def largest_number(numbers):
    largest = numbers[0]

    for num in numbers:
        if num > largest:
            largest = num

    return largest

my_list = [10, 25, 45, 15, 30]

result = largest_number(my_list)

print("List:", my_list)
print("Largest number:", result)
