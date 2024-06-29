import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import requests
import os

id = os.environ.get("a")
def send_email(sender_email, sender_password, recipient_email, subject, html):
    # 设置SMTP服务器地址和端口
    smtp_server = 'smtpdm.aliyun.com'
    smtp_port = 25

    # 创建一个MIMEMultipart对象
    # message = MIMEMultipart()
    message = MIMEMultipart("alternative")
    message['From'] = sender_email
    message['To'] = recipient_email
    message['Subject'] = subject

    # 添加邮件内容
    message.attach(MIMEText(html, "html"))
    try:
        # 连接到SMTP服务器
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # 启用TLS加密
        server.login(sender_email, sender_password)  # 登录SMTP服务器

        # 发送邮件
        server.sendmail(sender_email, recipient_email, message.as_string())
        print("邮件发送成功！")
    except Exception as e:
        print(f"邮件发送失败: {e}")
    finally:
        server.quit()  # 关闭与SMTP服务器的连接


# 使用示例
sender_email = 'dusk@mail.lovelxl.top'
sender_password = 'Pq3ctu7Uj8QTWU1vwnrR'
recipient_email = '2919408342@qq.com'
subject = '测试邮件'
html = """
<html>
  <body>
    <h1>HTML Email Test</h1>
    <p>Hello, this is a test email with <b>HTML content</b>.</p>
    <p>Here is a link to <a href="https://example.com">example.com</a>.</p>
  </body>
</html>
"""

send_email(sender_email, sender_password, recipient_email, subject, html)
