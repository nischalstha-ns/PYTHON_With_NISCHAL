# def nischal(a=7,b=20):
#     print("the average of number is",(a+b)/2)
# nischal()
# def name(fname="nischal",lname="shrestha"):
#     print("the name is ",fname,lname)
# name(lname="gurung",fname="HERO")
def avrage(*number):
    # print(type(number))
    sum=0
    for i in number:
        sum=sum+i
    # print("the average is",sum/len(number))
    return sum/len(number)
c=avrage(4)  
print(c) 

# def nam(**nam):
#     print(type(nam))
#     print("hello",nam["fname"],nam["lname"],nam["midname"])

# nam(fname="nsiljdk",midname="kkk" ,lname="stha")