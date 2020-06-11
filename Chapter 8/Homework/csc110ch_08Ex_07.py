# Write a function that reverses its string argument, and satisfies these tests:
# 1 test(reverse("happy") == "yppah")
# 2 test(reverse("Python") == "nohtyP")
# 3 test(reverse("") == "")
# 4 test(reverse("a") == "a")

def reverse(word):
    return word[::-1]

print(reverse("happy") == "yppah")
print(reverse("Python") == "nohtyP")
print(reverse("") == "")
print(reverse("a") == "a")