# Ws ch7-9
# A fruit vendor has :
# 250 apples   sold at    $1.25/apple
# 100 peaches sold at    $0.95/peach
# 75 bananas  sold at      $0.20/ banana
# 125 oranges sold at     $0.50/orange

# Organize this data into an appropriate data structure & write code to:
# Find the total number of pieces of fruit
# Find the total $ value for the fruit.
# Find the average cost of a piece of fruit.
# Find the number of pieces of fruit that have a greater than average cost.

fruit_vendor = [("apples", 250, 1.25),
    ("peaches", 100, 0.95),
    ("bananas", 75, 0.20),
    ("oranges", 125, 0.50)]

# total = 0
# for (frt, qty, prc) in fruit_vendor:
#     total += qty
# print("total number fruit is", total)

# value = 0
# for (frt, qty, prc) in fruit_vendor:
#     value = value + prc * qty
# print("The total fruit value is $", value)

# avg_cost = value / total

# print("Average cost of a piece of fruit is $", round(avg_cost, 2))

# sum_acum = 0
# for (frt, qty, prc) in fruit_vendor:
#     if (prc > avg_cost):
#         sum_acum += qty

# print('pieces of fruit with > average cost is', sum_acum)

total, value, sum_acum = 0, 0, 0
for (frt, qty, prc) in fruit_vendor:
    total += qty
    value = value + prc * qty

avg_cost = value / total

sum_acum = 0
for (frt, qty, prc) in fruit_vendor:
    if (prc > avg_cost):
        sum_acum += qty

print("total number fruit is", total)
print("The total fruit value is $", value)
print("Average cost of a piece of fruit is $", round(avg_cost, 2))
print('pieces of fruit with > average cost is', sum_acum)