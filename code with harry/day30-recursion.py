# factorial find
# formula 
# factorial(n)=n*factorial(n)
# def factorial(n):
#     if(n==1 or n==0):
#         return 1
#     else:
#         return n+factorial(n-1)
# print(factorial(30))
# print(factorial(0))
# febonic series
# 0 1 1 2 3 5 8 13
def nischal():
    temp=00
    a=0
    b=1
    while temp<9:
        temp=a+b
        a=b
        b=temp
    print(a)
nischal()
