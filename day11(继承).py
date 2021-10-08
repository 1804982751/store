#面向对象：
#继承：子类与父类
# class Person:
#     username=""
#     age=0
#     sex=""
#     address=None
#
# class Address:
#     country=""
#     province=""
#     street=""
#     door=""
#
# p=Person()
# p.username="魏朝辉"
# p.sex="男"
# p.age=20
#
# add=Address()
# add.country="china"
# add.province="北京"
# add.street="朝阳北大街"
# add.door=1102
#
# p.address=add




class cook:
    __name=""
    __age=0
    def setname(self,name):
        self.__name=name
    def getname(self):
        return self.__name
    def setage(self,age):
        if age < 0 or age > 120:
            print("年龄输入非法")
        else:
            self.__age=age
    def getage(self):
        return self.__age

    def zhengfan(self,zhengfan_name):
        print(self.__age,"岁的",self.__name,"正在蒸饭，蒸的",zhengfan_name)
# c=cook()
# c.setage(20)
# c.setname("张三")
# c.zhengfan("小米饭")

class good_cook(cook):
    def chaocai(self,chaocai):
        print("正在",chaocai)

class best_cook(good_cook):
    def zhengfan(self,zhengfan_name):
        super().zhengfan(zhengfan_name)

    def chaocai(self,chaocai):
        super().chaocai(chaocai)

b=best_cook()
b.setname("小二")
b.setage(18)
b.zhengfan("米饭")
b.chaocai("炒菜")



print("----------------")
class person:
    age=0
    sex=""
    name=""
    def work(self,work):
        return
class worker(person):
    type=""
    def WORK(self,WORK):
        super().work(WORK)
        print(self.name,self.type,"正在工作")
class student(worker):

    def study(self,study):
        super().WORK(study)
        print(self.name,self.type,"正在学习",study)
    def song(self,song):

        print(self.name,self.type,"正在唱歌",song)

s = student()
s.age=5
s.sex="男"
s.name="三哥"
s.type="学生"
s.study("英语")
s.song("大江大河")






