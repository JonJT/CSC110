# Write a function that mirrors its argument:
# test(mirror("good") == "gooddoog")
# test(mirror("Python") == "PythonnohtyP")
# test(mirror("") == "")
# test(mirror("a") == "aa")

def mirror(String):
    reverse = String[::-1]
    return String + reverse

print(mirror("good") == "gooddoog")
print(mirror("Python") == "PythonnohtyP")
print(mirror("") == "")
print(mirror("a") == "aa")