import smtplib
from email.mime.text import MIMEText
from email.header import Header


def sendMail(ssr=None):

    if ssr == None:
        return

    content = None
    if type(ssr) == list:
        content = '\n\n'.join(ssr)
    else:
        content = ssr

    mail_host = "smtp.126.com"  # SMTP服务器
    mail_user = "devlynn@126.com"  # 用户名
    mail_pass = "xxx"
    sender = mail_user
    receivers = [
        'flynn.cocoa@gmail.com',
                 #'dengtaojava@163.com'
    ]

    # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
    message = MIMEText(content, 'plain', 'utf-8')
    # message['From'] = Header(sender, 'utf-8')  # 发送者
    # message['To'] = Header(';'.join(receivers), 'utf-8')  # 接收者
    message['From'] = sender
    message['To'] = ';'.join(receivers)

    subject = 'ssr链接'
    message['Subject'] = Header(subject, 'utf-8')

    try:
        smtpObj = smtplib.SMTP()
        smtpObj.set_debuglevel(1)
        smtpObj.connect(mail_host, 25)
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("邮件发送成功")
        smtpObj.quit()
    except smtplib.SMTPException:
        print("邮件发送失败")

if __name__ == '__main__':
    sendMail('abc')
