# f= open('myfile.txt','r')
# text=f.read()
# print(text)
# f.close()


# # writing to the file
# f= open('myfile.txt','a')
# f.write("hello my name is nischal shrestha")
# f.close()
# # reading
# f= open('myfile.txt','r')
# text=f.read()
# print(text)
# f.close()

f=open("myfile.txt","a")
num=int(input("enter the numer:"))
for i in range(0,num):
    stdN=str(input("enter the student name:"))
    stdR=int(input("enter the student roll:"))
    stdC=int(input("enter the student class: "))
    f.write(f"student name:{stdN}\n, studnt roll: {stdR}\n, student class:{stdC}\n")

f.close()


