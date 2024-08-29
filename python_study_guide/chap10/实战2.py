# 推算几天后的日期 编写一个程序，输入开始日期和间隔天数，可以推算出结束日期，使用内置datetime模块
import datetime

# 输入 日期的函数

def input_date():
    input_date = input("give date:")
    date_str=input_date[0:4]+'-'+input_date[4:6]+'-'+input_date[6:]  # 切片出年月日
    # 类型转换
    dt = datetime.datetime.strptime(date_str,'%Y-%m-%d')
    return dt


# 主程序运行

if __name__ == '__main__':
    date = input_date()
    # 输入间隔天数

    in_num=eval(input('give days:'))
    date=date+datetime.timedelta(days=in_num)
    print('the days you guess:',date)
