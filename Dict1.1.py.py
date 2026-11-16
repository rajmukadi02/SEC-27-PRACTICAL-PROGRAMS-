def sort_dictionary(my_dict):
    sorted_dict = dict(sorted(my_dict.items()))
    return sorted_dict

my_dict = {3: "Apple", 1: "Mango", 4: "Banana", 2: "Orange"}

result = sort_dictionary(my_dict)

print("Original Dictionary:", my_dict)
print("Sorted Dictionary:", result)
