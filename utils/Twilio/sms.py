import time,random
from django.conf import settings
from twilio.rest import Client # 需要装twilio库
# 获取当前时间并格式化显示方式：
send_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
def send_message(phone_num,tpl,code,nickname):
	account_sid = settings.SMS_APP_ID
	auth_token = settings.SMS_APP_KEY
	phone_num = '+86'+phone_num
	user_name = nickname
	if tpl == 'register':
		client = Client(account_sid, auth_token) # 账户认证
		message = client.messages.create(to="+8618872581558", # 接受短信的手机号 注意写中国区号 +86
		from_="+17326064111", # api参数 Number(领取的虚拟号码+17326064111
		body="\n用户"+str(user_name)+"您好！\n您通过"+str(phone_num)+"注册的短信验证码："+str(code)+"\n请勿透露他人") #自定义短信内容
		print('接收短信号码：'+message.to)# 打印发送时间和发送状态：
		print('发送时间：%s \n状态：发送成功！' )
		print('短信内容：\n'+message.body) # 打印短信内容
		print('短信SID：' + message.sid) # 打印SID
'''		try:
			message.sid == 0
			print("发送失败")
		except HTTPError as e:
			response = {'result': 1000, 'errmsg': "网络异常发送失败"}
		return response'''
'''	elif tpl == 'login':
		client = Client(account_sid, auth_token) # 账户认证
		message = client.messages.create(to=phone_num, # 接受短信的手机号 注意写中国区号 +86
		from_="+17326064111", # api参数 Number(领取的虚拟号码
		body="\n您的登录短信验证码："+str(code)+"\n——请勿向他人透露") #自定义短信内容
		print('接收短信号码：'+message.to)# 打印发送时间和发送状态：
		print('发送时间：%s \n状态：发送成功！')
		print('短信内容：\n'+message.body) # 打印短信内容
		print('短信SID：' + message.sid) # 打印SID
		try:
			message.sid == 0
			print("发送失败")
		except HTTPError as e:
			response = {'result': 1000, 'errmsg': "网络异常发送失败"}
		return response
	else :
		response = {'result': 1000, 'errmsg': "网络异常发送失败"}
		return response'''
	