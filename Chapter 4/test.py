# import turtle

# wn = turtle.Screen()
# t = turtle.Turtle()
# wn.bgcolor("black")
# t.color("white")
# t.pensize(3)

# def draw_mltclr_sq (tt, sz):
#     """Make turtle t draw a multi-color square of sz."""
#     for i in ["red", "purple", "hotpink", "blue"]:
#         t.color(i)
#         t.forward(sz)
#         t.left(90)

# size = 20
# for i in range (15):
#     draw_mltclr_sq(t, size)
#     size = size + 10
#     t.fd(10)
#     t.rt(18)

# wn.mainloop()

##################################

# def return_sqr(x):
#     return x**2

# # print(return_sqr(4) + 1)

# answer = return_sqr(4)
# finalAnswer = answer + 1
# print(finalAnswer)

# F = [range(0,60)]

# print(F)

def SumOfSqrOfInts_A(x, y):

    
    
    for n in range(x, y):
        total = 0
        
        d7 = (n % 7 == 0)           # div by 7
        d3 = (n % 3 == 0)           # div by 3
        d2 = (n % 2 == 0)           # div by 2
        b = ((d7 or d3) and d2)
        if (b):

            sqrn = n**2
            
            total = total + sqrn
            
            print(n, end = ' ')

        print(total)
            
print(SumOfSqrOfInts_A(20, 41))

