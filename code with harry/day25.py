truple=(0,1,2,3,4,5,6,7,8,9)
# res=truple.count(3)
res=truple.index(3)

ns=list(truple)
# print(ns)
ns[1]=38
truple=tuple(ns)
print(type(truple))
print(ns)
# print(type(ns))