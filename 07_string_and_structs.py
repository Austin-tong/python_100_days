# 跑馬燈文字
import os, time, random
def horse_light():
    content = 'welcome to beijing'
    while True:
        os.system('cls')
        print(content)
        time.sleep(2)
        content = content[1:]+content[0]
# horse_light()

# 驗證碼
def generate_code():
    code = ''
    for i in range(6):
        code += str(random.randint(0,9))
    print(code)
# generate_code()

# 返回列表最大值和
def max2(L):
    max_num = max(L)
    L.remove(max_num)
    print(max_num + max(L))
# L = [1,2,3,4,5,6,7,8,9,10,11]
# max2(L)

# 计算指定的年月日是这一年的第几天
def is_leap_year(year):
    return True if year%4 == 0 else False

def which_day(year, month, day):
    days_of_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    result = 0
    if month == 1:
        return day
    else:
        for i in range(month-1):
            result += days_of_month[i]
        result += day
        if is_leap_year(year):
            result += 1
        return result
# print(which_day(2021,2,28))

# 打印杨辉三角
def yanghui(level):
    for i in range(1,level+1):
        str = ''
        for j in range(i):
            str += '*'
        print(str)
yanghui(5)

