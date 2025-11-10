# # n*fact(n-1)
# n=4
# fact=1
# for i in range(1, n + 1):
#     fact = fact * i
# print(fact)

def trirecursive(k):
    if k>0:
        result=k*trirecursive(k-1)
        print(result)

    else:
        result=0
k=int(input("enter the valur"))
trirecursive(k)
