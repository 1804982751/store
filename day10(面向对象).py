#笔记本电脑
class computer:
    __size=""
    __money=""
    __cpu=""
    __RAM=""
    __work_time=""
    def setSize(self,size):
        self.__size=size
    def getSize(self):
        return self.__size

    def setMoney(self,money):
        self.__money=money
    def gitMoney(self):
        return self.__money

    def setCpu(self,cpu):
        self.__cpu=cpu
    def gitCpu(self):
        return self.__cpu

    def setRam(self,RAM):
        self.__RAM=RAM
    def getRAM(self):
        return self.__RAM

    def setwork_time(self,work_time):
        self.__work_time=work_time
    def gitwork_time(self):
        return self.__work_time


    def dazi(self):
        print("打的字显示在",self.__size,"的屏幕上了，并占用了",self.__RAM)
    def dayouxi(self):
        print("正在打游戏，待机时长",self.__work_time)
    def kanshiping(self):
        print("正在用CPU为",self.__cpu,"的电脑看视频")



c=computer()
c.setwork_time("3小时")
c.setRam("2GB")
c.setCpu("CPU2号")
c.setMoney("7000元")
c.setSize("4.8英寸")

c.dazi()
c.dayouxi()
c.kanshiping()






