# ws ch 7_10
# If you make a guess x0 for the square root of a number, n, a better guess for the sqr root is
# (x0 + n/x0)/2
# Write code to find abs(guess**2 - n)/n  <= 0.01%.

def sqrt(n):
    approx = n/2.0 # Start with some or other guess at the answer
    while True:
        better = (approx + n/approx)/2.0
        if abs(approx - better) < 0.001:
            return better
        approx = better


print(sqrt(25.0))
print(sqrt(49.0))
print(sqrt(81.0))