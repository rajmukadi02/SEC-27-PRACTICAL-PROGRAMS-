def is_palindrome(string):
    if string == string[::-1]:
        return True
    else:
        return False

text = input("Enter a string: ")

if is_palindrome(text):
    print(text, "is a Palindrome")
else:
    print(text, "is not a Palindrome")
