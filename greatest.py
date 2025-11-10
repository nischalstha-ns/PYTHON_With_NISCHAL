def ns(a,b,c):
    if a>b and a>c:
        print("a is greatest")
    if b>a and b>c:
        print("b is greatest")
    elif c>a and c>b:
        print("c is greatest")



a=int(input("enter the value of a"))
b=int(input("enter the value of b"))
c=int(input("enter the value of "))

ns(a,b,c)