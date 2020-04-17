# csc 110 spr 20 quiz 1 practice

# Convert to whole number of yards, feet, inches:

total_inches = 555  
print('total inches =',total_inches)
begin = total_inches

yards = total_inches // 36   ## compute number of yards
total_inches  %= 36          ## update inches, left over inches

feet = total_inches // 12    ## compute number of feet
inches = total_inches % 12   ## left over inches


print(begin,'inches =',yards,'yards,',feet,'feet,',inches,'inches.')

print('Check:', yards*36 + feet*12 + inches,'inches.')

##total inches = 555
##555 inches = 15 yards, 1 feet, 3 inches.
##Check: 555 inches.
##>>> 
