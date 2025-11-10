import time
t=time.strftime('%H:%M:%S')
print(t)
hour=int(time.strftime('%H'))
if(hour<12 and hour>0):
    print("good morning")
elif(hour>=12 and hour<17):
    print("good after noon")
elif(hour>17 and hour<24):
    print("good night") 
# else:
#     print("invalid")
# print(hour)
# hour=int(input("ehter the hour"))
# print(hour)