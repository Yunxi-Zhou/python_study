


import admin.my_admin as a   #  包名.模块

a.info()


print('-'*80)
from admin import my_admin as b # from 包名 import 模块 as nickname


b.info()

from admin.my_admin import info  # from 包名.模块名 import 函数/变量等
info()


from admin.my_admin import * 
print(name)








