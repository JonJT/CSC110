# Write a function which is given an exam mark, and it returns a string — the grade for
# that mark — according to this scheme:
# Mark Grade
# >= 75 First
# [70-75) Upper Second
# [60-70) Second
# [50-60) Third
# [45-50) F1 Supp
# [40-45) F2
# < 40 F3
# The square and round brackets denote closed and open intervals. A closed interval includes the number, and open interval excludes it. So 39.99999 gets grade F3, but 40 gets
# grade F2. Assume
# xs = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50,
# 49.9, 45, 44.9, 40, 39.9, 2, 0]
# Test your function by printing the mark and the grade for all the elements in this list.

def grade(x):
    g = ["First", "Upper Second", "Second", "Third", "F1 Supp", "F2", "F3"]
    if 75 <= x:
        return g[0]
    elif 70 <= x and x < 75:
        return g[1]
    elif 60 <= x and x < 70:
        return g[2]
    elif 50 <= x and x < 60:
        return g[3]
    elif 45 <= x and x < 50:
        return g[4]
    elif 40 <= x and x < 45:
        return g[5]
    else:
        return g[6]
        

xs = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50, 49.9, 45, 44.9, 40, 39.9, 2, 0]

for x in xs:
    print(float(x), ' ', grade(x))