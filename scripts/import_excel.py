import pandas as pd
import pymysql as pm
import os
import time
#获取最新的excel表
src = '\\\\smbserver\\共享文件夹\\生产管理部\\生产管理部\\公司生产统计台帐\\低值易耗品库\\二厂\\'#目录地址


def path_new(test_path):
    lists = os.listdir(test_path) #列出目录的下所有文件和文件夹保存到lists
    print(lists)
    lists.sort(key=lambda fn:os.path.getmtime(test_path + "\\" + fn))  # 按时间排序
    file_new = os.path.join(test_path,lists[-1]) # 获取最新的文件保存到file_new
    return file_new
test_path=src

i=1
while i<3:
    test_path =path_new(test_path)
    i=i+1
print(test_path)





'''
path_excel = 1

#连接数据库
db = pm.connect(host="127.0.0.1",port=3307,user="root",passwd="usbw",db="manuf")
print("数据库连接成功")
#创建游标
cursor = db.cursor()
print('---update---')
#读取excel
df = pd.read_excel('path_excel',usecols=['存货编号','规格型号','期末'])
df.head(3)
#更新数据
data_list = df.values.tolist()
sql_replace="""replace into m_specialparts (field1,field2,field3) values (%s,%s,%s) """
cursor.executemany(sql_replace,data_list)
#提交
db.commit()
#关闭游标
cursor.close()
#关闭连接
db.close()
'''