
def send(email_content,email_address):
	from email.mime.multipart import MIMEMultipart
	from email.mime.text import MIMEText

	content = MIMEMultipart()  #建立MIMEMultipart物件

	content["subject"] = "富邦保險結果"  #郵件標題
	content["from"] = "410721315@gms.ndhu.edu.tw"  #寄件者
	content["to"] = email_address #收件者
	content.attach(MIMEText(email_content))  #郵件內

	import smtplib
	with smtplib.SMTP(host="smtp.gmail.com", port="587") as smtp:  # 設定SMTP伺服器
	    try:
	        smtp.ehlo()  # 驗證SMTP伺服器
	        smtp.starttls()  # 建立加密傳輸
	        smtp.login("410721315@gms.ndhu.edu.tw", "zannhautelxljmzj")  # 登入寄件者gmail
	        smtp.send_message(content)  # 寄送郵件
	        print("Complete!")
	    except Exception as e:
	        print("Error message: ", e)