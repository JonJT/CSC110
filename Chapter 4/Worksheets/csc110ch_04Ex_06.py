# ******************************************
# WS ch4_6
# Choose p,r,n = 1000,0.05,1.  Use final_amt(p, r, n, t) with a for loop to print out a table showing  the final amount 
# for the 1st 20 years.  Look up and use the round  function to print out 2 decImal places.
# ******************************************

def final_amount(p, r, n, t):
    '''return a - p*(1 + r / n) ** (n*t))'''
    a = p*(1 + r / n) ** (n*t)
    return a

# table

p, r, n = 1000,0.05,1

print('year         $ amount')
print('----------------------')

for t in range(1,21):
    amt = round(final_amount(p, r, n, t), 2)
    print(t, '          ', amt)