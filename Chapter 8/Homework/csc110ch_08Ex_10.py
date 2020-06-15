# Write a function that recognizes palindromes. (Hint: use your reverse function to
# make this easy!):
# test(is_palindrome("abba"))
# test(not is_palindrome("abab"))
# test(is_palindrome("tenet"))
# test(not is_palindrome("banana"))
# test(is_palindrome("straw warts"))
# test(is_palindrome("a"))
# test(is_palindrome("")) # Is an empty string a palindrome?

def reverse(String):
    return String[::-1]

def is_palindrome(String):
    reverseString = reverse(String)
    if reverseString == String:
        return True
    else:
        return False

print(is_palindrome("abba"))
print(not is_palindrome("abab"))
print(is_palindrome("tenet"))
print(not is_palindrome("banana"))
print(is_palindrome("straw warts"))
print(is_palindrome("a"))
print(is_palindrome("")) # Is an empty string a palindrome? Yes