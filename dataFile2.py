import pandas as pd
import random
xl = pd.ExcelFile("groupInfo.xlsx")

df = xl.parse("Sheet1")


for i in df.index:
    data1 = str(df['fname'][i])
    data2 = str(df['lname'][i])
    data3 = str(df['email'][i])
    data4 = str(df['cellPhone'][i])

    print("first Name: ",data1 +"\n Last Name: "+data2+"\n Email: "+data3 +"\n Cell Phone: "+data4 +"\n")
    #Solution2
df = pd.read_excel('groupInfo.xlsx')

# df display
print(df)
#for i in df.index:
# m= list(df.iloc[i])
# print(m)

n = list(df['email'])
group = 1
a=int(input("\nPlease enter group size: "))
membersInGroup = a
for x in n[:]:
          if membersInGroup == a:
              print("\nGroup {} consists of;".format(group))
              membersInGroup = 0
              group =group + 1
          employee = random.choice(n)
          print(employee)
          membersInGroup=membersInGroup+1
          n.remove(str(employee))











