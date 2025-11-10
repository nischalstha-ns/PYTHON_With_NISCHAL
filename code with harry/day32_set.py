# s1={2,3,6,8,9}
# s2={2,5,7,9,9}
# print(s1.union(s2))
# s1.update(s2)
# print(s1,s2)
cities={"tokha","basundhara","ranibari","samakhushi"}
cities2={"tokha","basundhara"}
print(cities.union(cities2))
print(cities.intersection(cities2))
# # cities.intersection_update(cities2)
# # print(cities)
# # cities3=cities.symmetric_difference(cities2)#it is the inverse of union
# # cities3=cities.difference(cities2)
# # print(cities3)
# print(cities.isdisjoint(cities2))
# print(cities.issuperset(cities2))