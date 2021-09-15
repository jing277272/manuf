import pandas as pd
import pymysql as pm
import os
import time
#获取最新的excel表


import os

dir = '\\\\smbserver\\共享文件夹\\生产管理部\\生产管理部\\公司生产统计台帐\\低值易耗品库\\二厂\\'
specify_str = '冲头凹模'

# 搜索指定目录
files = []
folders = [dir]

for folder in folders :
    # 把目录下所有文件夹存入待遍历的folders
    folders += [os.path.join(folder, x) for x in os.listdir(folder) \
                if os.path.isdir(os.path.join(folder, x))]

    # 把所有满足条件的文件的相对地址存入结果results
    files += [os.path.relpath(os.path.join(folder, x), start = dir) \
                for x in os.listdir(folder) \
                if os.path.isfile(os.path.join(folder, x)) and specify_str in x]
print('files')
print(files)


results=files.sort(key=lambda fn:os.path.getmtime(dir + "\\" + fn) )  # 按时间排序
print(results)



print('[#]')
# 输出结果
'''for result in results:
    print(result)
print('找到 %s 个结果！' % len(results))'''

file_new =files[-1] # 获取最新的文件保存到file_new
print('最新文件'+file_new)


path_excel = str(dir+file_new)
#path_excel  = path_excel .replace('\\','\\\\')
os.path.isfile(path_excel)
#连接数据库
db = pm.connect(
    host="127.0.0.1",
    port=3307,
    user="root",
    passwd="usbw",
    db="manuf")
print("数据库连接成功")
#创建游标
cursor = db.cursor()
print('---update---')
#读取excel
print("读取excel:\n"+path_excel)
df = pd.read_excel(path_excel,usecols=['存货编号','规格型号','期末'])
df.rename(columns={'存货编号':'local','规格型号':'model','期末':'quantity'},inplace=True)
#转换数字型
df[['local','quantity']] = df[['local','quantity']].apply(pd.to_numeric, errors='ignore')
#删除空行
df.dropna(axis=0, how='all', inplace=True)  
print(df.head(3))
#到出csv文件
df = df.to_csv('out.csv',index=False)
print("成功导出到out.csv!")



#更新数据
data_list = df.values.tolist()
sql_replace=f"""replace into m_specialparts (local,model,quantity) values (%s,%s,%s)  index=False """
cursor.executemany(sql_replace,data_list)
#提交
db.commit()
#关闭游标
cursor.close()
#关闭连接
db.close()
