# print out odd ints from 13 to 21 on the same line, inclusive
# for x in range(13,23,2):
#     print(float(x), end = ' ')

# sum_acum = 0
# for x in range(3, 9 +2, 2):
#     sum_acum += x

# print(sum_acum)

# sum_acum = 0
# for x in range(1, 6):
#     sum_acum += x**2

# print(sum_acum)

# L = range(1,10)
# print(sum(L))

# import turtle

# wn = turtle.Screen()
# tess = turtle.Turtle()
# wn.bgcolor("black")
# tess.color("red")
# tess.pensize(4)

# # for i in range(2):
# #     tess.fd(50)
# #     tess.lt(90)
# #     tess.fd(100)
# #     tess.lt(90)

# def rect (t,W,H):
#     '''turtle t draws rectangle of width W and of hight H.'''
#     trn = 90
#     for i in range(2):
#         tess.fd(50)
#         tess.lt(trn)
#         tess.fd(100)
#         tess.lt(trn)

# # rect(tess, 100, 50)

# def pinwheelRect(t,W,H,n):
#     '''turtle t draws n rectangle of width W and of hight H, in a circle. Ue rect (t, W, H) as a helper function.'''
#     trnAngle = 360/n
#     for i in range(n):
#         rect(t, W, H)
#         t.lt(trnAngle)

# # pinwheelRect(tess, 100, 50, 6)

# def sqr():
#     '''tess draws a square of size 100.'''
#     for i in range (4):
#         tess.fd(100)
#         tess.lt(90)

# sqr()

# def Sqr(t, Sz):
#     '''turtle t draws a square of size Sz.'''
#     for i in range (4):
#         t.fd(Sz)
#         t.lt(90)

# Sqr(tess, 150)


# def addInts():
#     s = 0
#     for i in range(5, 29 + 3, 3):
#         s += i
#     print(s)

# addInts()

# def  addMult3(n):
#     s = 1
#     for i in range(3, n, 3):
#         s += i ** 3
#     print(s)
# addMult3(2)

# n1 = 1950.1**3
# n2 = 1975.2**3
# n3 = 2000.3**3

# n4 = n1 + n2 + n3

# print(n4)

# oz2cup = 8
# oz2pt = oz2cup * 2
# oz2qt = oz2pt * 2
# oz2gal = oz2qt * 4

# print(oz2cup)
# print(oz2pt)
# print(oz2qt)
# print(oz2gal)

# oz2cup = 8
# oz2pt = oz2cup * 2
# oz2qt = oz2pt * 2
# oz2gal = oz2qt * 4

# begin = 7953
# total_oz = begin

# total_gals = total_oz // oz2gal
# total_oz %= oz2gal

# total_qts = total_oz // oz2qt
# total_oz %= oz2qt

# total_pts = total_oz // oz2pt
# total_oz %= oz2pt

# total_cups = total_oz // oz2cup
# total_oz %= oz2cup

# total_oz_remain = total_oz

# print("7953 oz is", total_gals, "gallons", total_qts, "quarts", total_pts, "pints", total_cups, "cups", total_oz_remain, "oz.")

# usrNm=[]
# s = 0

# for i in range(3):
#     usrNm.append(float(input("Enter number: ")))
    
# for x in (usrNm):
#     s += x ** 3

# print(s)

usrNm=[]
 
for i in range(3):
    usrNm.append(float(input("Enter number: ")))
    s = 0
    for x in (usrNm):
        s += x ** 3
 
print(s)
