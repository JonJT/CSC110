# *************************************
# WS ch2_10
# You leave for vacation on Friday & return 123 days later.  Use // and % to compute the number of weeks gone and number of 
# days after Friday that you returned.  What day did you return?
# **************************************

days_gone = 123
days_per_wk = 7
wks_gone = 123 // 7
days_left_over = days_gone % days_per_wk

print("You were gone",wks_gone,"weeks and", days_left_over, "days.", "I returned on a Tuesday")