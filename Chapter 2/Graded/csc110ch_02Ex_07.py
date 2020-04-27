## grade = 0.9, should be 17 or 5 pm.  Do you see what's wrong?

# You look at the clock and it is exactly 2pm. You set an alarm to go off in 51 hours. at what time does the alarm go off?
# (HintL you could count on your fingers, but this is not what we're after. If you are tempted to count on your fingers, change the 51 to 5100)

t = 1400 # starting time of day 't'
a = 5100 # alarm will go off after 'a' hours

taa = (t + a) % 24

print("arlarm will go off at", taa, ":00 hours")

# I tried a few different things to remove the space between taa and :00 hours, but was unable to come up with a solution

##arlarm will go off at 20 :00 hours
##>>>