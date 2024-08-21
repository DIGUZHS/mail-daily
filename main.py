import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formataddr
import string
import requests
import base64
from datetime import datetime
import os

# os.environ['sender_email'] = 'dusk@mail.lovelxl.top'
# os.environ['sender_pad'] = 'Pq3ctu7Uj8QTWU1vwnrR'
# os.environ['receiver_emails'] = '2919408342@qq.com,3406485437@qq.com,3211983338@qq.com'
# os.environ['city'] = 'jinan'
# os.environ['start_day'] = '2024-06-13'


sender_email = os.environ.get('SENDER_EMAIL')
sender_pad = os.environ.get('SENDER_PAD')
city = os.environ.get('CITY')
start_day = os.environ.get('START_DAY')
receiver_emails = os.environ.get('RECEIVER_EMAILS')
receiver_email_list = receiver_emails.split(',')


def inday(start_day):
    # 定义过去的某一天
    #start_day = '2024-06-13'  # 使用 YYYY-MM-DD 格式
    past_date = datetime.strptime(start_day, '%Y-%m-%d')
    # 获取今天的日期
    today = datetime.today()
    weekday = today.weekday()
    weekdays = ["周一", "周二", "周三", "周四", "周五", "周六", "周天"]
    # 计算两个日期之间的天数
    delta = today - past_date
    days = int(delta.days) + 1
    return days, weekdays[weekday]

def gat_weather_info(city):
    now = 'https://api.seniverse.com/v3/weather/now.json?key=SzNe6EfEYEPXIC9qd&location='+ city +'&language=zh-Hans&unit=c'
    daily = 'https://api.seniverse.com/v3/weather/daily.json?key=SzNe6EfEYEPXIC9qd&location='+ city +'&language=zh-Hans&unit=c&start=0&days=1'
    suggestion = 'https://api.seniverse.com/v3/life/suggestion.json?key=SzNe6EfEYEPXIC9qd&location='+ city +'&language=zh-Hans&days=1'
    qinghau = 'https://api.uomg.com/api/rand.qinghua'
    now_response = requests.get(now).json()
    daily_response = requests.get(daily).json()
    suggestion_response = requests.get(suggestion).json()
    qinghua_response = requests.get(qinghau).json()
    # now
    weather = now_response['results'][0]['now']['text']
    weather_code = now_response['results'][0]['now']['code']
    temperature = now_response['results'][0]['now']['temperature']
    # daily
    text_day = daily_response['results'][0]['daily'][0]['text_day']
    text_night = daily_response['results'][0]['daily'][0]['text_night']
    code_day = daily_response['results'][0]['daily'][0]['code_day']
    code_night = daily_response['results'][0]['daily'][0]['code_night']
    high = daily_response['results'][0]['daily'][0]['high']
    low = daily_response['results'][0]['daily'][0]['low']
    # suggestion
    comfort = suggestion_response['results'][0]['suggestion'][0]['comfort']['details']
    uv = suggestion_response['results'][0]['suggestion'][0]['uv']['details']
    umbrella = suggestion_response['results'][0]['suggestion'][0]['umbrella']['details']
    # qinghua
    qinghua = qinghua_response['content']
    #return weather, weather_code, temperature, text_day, text_night, code_day, code_night, high, low, comfort, uv, umbrella, qinghau
    return {
        'weather': weather,
        'weather_code': weather_code,
        'temperature': temperature,
        'text_day': text_day,
        'text_night': text_night,
        'code_day': code_day,
        'code_night': code_night,
        'high': high,
        'low': low,
        'comfort': comfort,
        'uv': uv,
        'umbrella': umbrella,
        'qinghua': qinghua
    }

def image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
        return encoded_string.decode('utf-8')

def send_email(sender_email, sender_password, receiver_email_list, subject, html):
    # 设置SMTP服务器地址和端口
    smtp_server = 'smtpdm.aliyun.com'
    smtp_port = 25

    # 创建一个MIMEMultipart对象
    # message = MIMEMultipart()
    message = MIMEMultipart("alternative")
    message['From'] = formataddr(('爱你的宝', sender_email))
    message['To'] = ", ".join(receiver_email_list)
    message['Subject'] = subject

    # 添加邮件内容
    message.attach(MIMEText(html, "html"))
    try:
        # 连接到SMTP服务器
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # 启用TLS加密
        server.login(sender_email, sender_password)  # 登录SMTP服务器

        # 发送邮件
        server.sendmail(sender_email, receiver_email_list, message.as_string())
        print("邮件发送成功！")
    except Exception as e:
        print(f"邮件发送失败: {e}")
    finally:
        server.quit()  # 关闭与SMTP服务器的连接


try:
    weather_data = gat_weather_info(city)
    #weather, weather_code, temperature, text_day, text_night, code_day, code_night, high, low, comfort, uv, umbrella, qinghua = gat_weather_info(city)
    with open('weather.html', 'r', encoding='utf-8') as f:
        con = f.read()
    variables = {
        'card_color': '#E0F7FA',
        'header_color': '#87CEEB',
        'week': inday(start_day)[1],
        'weather': weather_data['weather'],
        'now_temperature': weather_data['temperature'],
        'max_temperature': weather_data['high'],
        'min_temperature': weather_data['low'],
        'text_day': weather_data['text_day'],
        'text_night': weather_data['text_night'],
        'comfort': weather_data['comfort'],
        'uv': weather_data['uv'],
        'inday': inday(start_day)[0],
        'qinghua': weather_data['qinghua'],
        'weather_icon': image_to_base64('white/' + weather_data['weather_code'] + '.png'),
        'day_icon': image_to_base64('white/' + weather_data['code_day'] + '.png'),
        'night_icon': image_to_base64('white/' + weather_data['code_night'] + '.png'),
    }
    template = string.Template(con)
    formatted_content = template.safe_substitute(variables)
    with open('backups/' + str(datetime.today().strftime("%Y-%m-%d"))+'.html', 'w', encoding='utf-8') as file:
        file.write(formatted_content)
except Exception as e:
    print(e)



# 使用示例
# sender_email = 'dusk@mail.lovelxl.top'
# sender_password = 'Pq3ctu7Uj8QTWU1vwnrR'
# recipient_email = '2919408342@qq.com'
subject = str(datetime.today().strftime("%Y-%m-%d"))+'今天也是爱宝宝的一天'


with open('weather.html', 'r', encoding='utf-8') as html_file:
    html_content = html_file.read()

send_email(sender_email, sender_pad, receiver_email_list, subject, formatted_content)
