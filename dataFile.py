import random

try:
  file = open("group.txt","r")

  for line in file:
      data = line.split(",")
      data1 =data[0]
      data2 = data[1]
      data3 =data[2]
      data4 = data[3]
      print("first Name: ",data1 +"\n Last Name: "+data2+"\n Email: "+data3 +"\n Cell Phone: "+data4)
except FileNotFoundError:
 print("No data exist")

file = open("group.txt", "r")
content = file.read()
Info = content.split("\n")
print(Info)
group = 1
a=int(input("\nPlease enter group size: "))
membersInGroup = a
for x in Info[:]:
          if membersInGroup == a:
              print("\nGroup {} consists of;".format(group))
              membersInGroup = 0
              group += 1
          employee = random.choice(Info)
          print(employee)
          membersInGroup=membersInGroup+1
          Info.remove(str(employee))

file.close()



