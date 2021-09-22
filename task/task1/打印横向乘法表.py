#左上角99乘法表
for row in range(1,10):#打印行
    for col in range(row,10):#打印列
        print("%dX%d=%d"%(row,col,row*col),end=" ")
        #{2:2d}是给{2}这个位置两倍的空间
        #设置end=""print就不会进行换行操作
    print(" ")