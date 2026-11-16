my_tuple = (10, 20, 30, 40, 50)

element = int(input("Enter an element to search: "))

if element in my_tuple:
    print(element, "exists in the tuple")
else:
    print(element, "does not exist in the tuple")
