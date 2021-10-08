import xlrd
wb = xlrd.open_workbook(filename=r"D:\gitbash\course\MySQL数据库\day09(xlrd)\任务\2020年每个月的销售情况.xlsx",encoding_override=True)
# st = wb.sheet_by_name("12月份各种服饰销售情况")
# rows = st.nrows #  多少行
# cols = st.ncols # 多少列
#print("有",rows,"行，有",cols,"列")


#方法一(自己的方法):
# 全年销售总额
sum0 = 0
for a in range(0,12):
    st= wb.sheet_by_index(a)
    rows=st.nrows
    cols=st.ncols
    for b in range(1,rows):
        sum0 = sum0 + st.row_values(b)[2]*st.row_values(b)[4]
print("全年销售总额",sum0)

# 每件衣服的销售件数占比
list=["羽绒服","牛仔裤","铅笔裤","皮草","衬衫","卫衣","T血","风衣","马甲","小西装","休闲裤","棉衣","皮衣"]
for c in range(len(list)):
    sum1=0
    data=0
    for d in range(0, 12):
        st= wb.sheet_by_index(d)
        rows=st.nrows
        cols=st.ncols
        for e in range(1,rows):
            sum1 = sum1 + st.row_values(e)[4]
            if st.row_values(e)[1] == list[c]:
                data=data+ st.row_values(e)[4]
    print(list[c],"的销售占比为：","{:.2%}".format(data/sum1))


# 方法二(老师方法):
print("                           ")
print("===========================")
store={}
nsheet=wb.nsheets
for i in range(nsheet):
    st=wb.sheet_by_index(i)
    nrow=st.nrows
    for j in range(1,nrow):
        cell=st.row_values(j)
        if cell[1] in store:
            store[cell[1]]={
                "sum_money":round(store[cell[1]]["sum_money"]+cell[2]*cell[4],2),
                "sum_count":int(store[cell[1]]["sum_count"]+cell[4])
            }
        else:
            store[cell[1]]={
                "sum_money":round(cell[2]*cell[4],2),
                "sum_count":int(cell[4])
            }
#全年的销售总额
all_sum=sum(store[item]["sum_money"] for item in store)
all_count=sum(store[item]["sum_count"] for item in store)
print("全年的销售总额为：",round(all_sum,2))
print("全年的销售总量为：",int(all_count))
for name in store:
    print("----------------------")
    print(name,"的年度销售额占比：",round(store[name]["sum_money"] / all_sum *100,2),"%")
    print(name,"的年度销售量占比：",round(store[name]["sum_count"] / all_count *100,2),"%")










