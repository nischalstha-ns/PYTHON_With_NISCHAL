a=int(input("ehter the number"))
b=int(input("ehter the number"))
c=input("enter the character like + - *")

match c:
    case "+":
        print(a+b)
    case "-":
        print(a-b)
    case "*":
        print(a*b)
match a:#like switch in c
    case 0:
        print("you enter 0")
    case 1:
        print("you enter the 1")
    case _:#like defult
        print("dkshajkf")

