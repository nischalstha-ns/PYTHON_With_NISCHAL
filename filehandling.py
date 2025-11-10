# f= open('myfile.txt','r')
# text=f.read()
# print(text)
# f.close()


# writing to the file
f= open('myfile.txt','w')
f.write("hello my name is nischal shrestha")
f.close()

f= open('myfile.txt','r')
text=f.read()
print(text)
f.close()

