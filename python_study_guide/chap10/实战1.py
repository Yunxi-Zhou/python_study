import prettytable as pt

# 显示坐席

def show_ticket(row_num):
    tb=pt.PrettyTable() # 创建一张表格
    # 设置标题(表格的排头部分)
    tb.field_names = ['行号','table1','table2','table3','table4','table5']

    # 遍历有票

    for i in range(1,row_num+1):
        lst=[f'第{i}行','available','available','available','available','available']
        tb.add_row(lst)
    
    print(tb)

# 订票
    
def order_ticket(row_num, row, column):
    tb=pt.PrettyTable() # 创建一张表格
    # 设置标题(表格的排头部分)
    tb.field_names = ['行号','table1','table2','table3','table4','table5']
    for i in range(1,row_num+1):
        if int(row) == i:
            lst=[f'第{i}行','available','available','available','available','available']
            lst[int(column)]='sold'
            tb.add_row(lst)
        else:
            lst=[f'第{i}行','available','available','available','available','available']
            tb.add_row(lst)

    print(tb)





if __name__ == '__main__':
    row_num = 6
    show_ticket(row_num)

    choose_num=input('please give your table: 4,3 = row 4 column 3:')
    row,column = choose_num.split(',')   # 系列解包赋值
    order_ticket(row_num,row,column)

