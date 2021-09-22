names=[
      ["曹操",56,"男","106","IBM",500,"50"],
      ["大乔",19,"女","230","微软",501,"60"],
      ["小乔",19,"女","210","Oracle",600,"60"],
      ["许褚",45,"男","230","Tencent",700,"10"]
]

i=0
num=0
while i<len(names):
      num=num+names[i][5]
      i=i+1
print("平均薪资为：",num/len(names))

i=0
age=0
while i<len(names):
      age=age+names[i][1]
      i=i+1
print("平均年龄：",age/len(names))

names.append(["刘备",45,"男","220","alibaba",500,"30"])
print("将刘备添加到names中:",["刘备",45,"男","220","alibaba",500,"30"] in names)

i=0
pel=0
man=0
while i<len(names):
      if names[i][2]=="女":
            pel+=1
            i+=1
      elif names[i][2]=="男":
            man+=1
            i+=1
print("公司男生人数：",man)
print("公司女生人数：",pel)

i=0
class1=0
class2=0
class3=0
class4=0
while i<len(names):
      if names[i][6]=="50":
            class1+=1
            i+=1
      elif names[i][6]=="60":
            class2+=1
            i+=1
      elif names[i][6] == "10":
            class3 += 1
            i += 1
      elif names[i][6] == "30":
            class4 += 1
            i += 1
print("公司50部门人数：",class1)
print("公司60部门人数：",class2)
print("公司10部门人数：",class3)
print("公司30部门人数：",class4)

