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

n1 = 1950.1**3
n2 = 1975.2**3
n3 = 2000.3**3

n4 = n1 + n2 + n3

print(n4)