# CSC 110 Spring 2020  Quiz 7 Take-home                       NAME: Jonathan Tally
# YouTube: https://youtu.be/0c-HXV-FBUE
# Write clear, legible code, the simpler the better. Make sure your code works.
# Due next Monday by the start of class.  Use the editor to write your code. Submit a file,
# Quiz_7_YourFullName.py in an email that has as subject  csc 110 quiz 7_YourFullName.
# Points will be deducted if submission is late.   



# 1. [40 pts]  Soup temperature starts at 120 Fahrenheit cools at 1 degree a minute.Write code using
# a while loop which prints out the soup temperature and the time taken in minutes to get to that temperature,
# stopping when 112 degrees Fahrenheit is reached. The output looks like this:

def soupTemp():
    temp = 120
    time = 0
    print('Temp (F)', '         ', 'Time(min)')
    print('-----------', '      ', '-----------')
    while True:
        print(temp,'               ', time)
        temp -= 1
        time += 1
        if (temp <= 112):
            break
    print(temp,'               ', time)


soupTemp()


# [XC 5 pts] Generalize the previous question and write a function
# coolDown(T0,T1,coolRate,del_T), where T0 is the starting temperature in F,
# T1 is the final temperature reached, the cooling rate in F/minutes is
# coolRate and the temperature is printed out every del_T.   Uses a while loop.
# This assumes the cooling rate is linear. (Actual cooling rate is exponential, but we
# will ignore that.]  For example, for glass coming out of a high temperature glass oven, suppose that
# T0,T1,coolRate,del_T = 1000,100,.5,50
# Then, the printout gives a table like this:

# coolDown(1000,100,.5,50)

def coolDown(T0,T1,coolRate,del_T):
    print('Temp (F)', '    ', 'hrs', '    ', 'mins')
    print('--------', '   ', '-----', '  ', '------')
    totalMin = 0
    numHrs = 0
    remainMins = 0
    while True:
        print(T0, '        ', numHrs, '    ', remainMins)
        T0 -= del_T
        totalMin += del_T / coolRate
        numHrs = totalMin // 60
        remainMins = totalMin % 60
        if(T0 <= T1):
            break
    print(T0, '        ', numHrs, '     ', remainMins)


# coolDown(1000, 100, .5, 50)

# To Submit:
# Your quiz .py file, csc110_Quiz_7_YourFullName.py in an email that has as subject csc110_Quiz_7_YourFullName.
# 2.  In your file, put a youtube link of a video showing and discussing Q1. Use https://screencast-o-matic.com/
# to download a video creation application.   I need to see Python code on the screen and to hear your voice as you explain.
# Be sure to announce yourself at the beginning of the video.  
