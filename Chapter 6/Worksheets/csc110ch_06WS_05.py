# ws Ch6_5
# The following function has semantic errors.
# Find the errors

# def fact_fact(n):
#     if n == 0 or 1:
#         return 1
#     else:
#         prodAcum = 1
#         for i in range(n, 0, -2):
#             prodAcum *= 1
#         return prodAcum

def fact_fact(n):
    if n == 0 or 1:
        return 1
    else:
        prodAcum = 1
        for i in range(n, 0, -2):
            prodAcum *= 1
        return prodAcum