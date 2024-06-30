# import string
# import requests
# import base64
# from datetime import datetime
# def inday():
#     # 定义过去的某一天
#     start_day = '2024-06-13'  # 使用 YYYY-MM-DD 格式
#     past_date = datetime.strptime(start_day, '%Y-%m-%d')
#     # 获取今天的日期
#     today = datetime.today()
#     weekday = today.weekday()
#     weekdays = ["周一", "周二", "周三", "周四", "周五", "周六", "周天"]
#     # 计算两个日期之间的天数
#     delta = today - past_date
#     days = delta.days
#     return days, weekdays[weekday]
#
# def gat_weather_info():
#     now = 'https://api.seniverse.com/v3/weather/now.json?key=SzNe6EfEYEPXIC9qd&location=jinan&language=zh-Hans&unit=c'
#     daily = 'https://api.seniverse.com/v3/weather/daily.json?key=SzNe6EfEYEPXIC9qd&location=jinan&language=zh-Hans&unit=c&start=0&days=1'
#     suggestion = 'https://api.seniverse.com/v3/life/suggestion.json?key=SzNe6EfEYEPXIC9qd&location=jinan&language=zh-Hans&days=1'
#     qinghau = 'https://api.uomg.com/api/rand.qinghua'
#     now_response = requests.get(now).json()
#     daily_response = requests.get(daily).json()
#     suggestion_response = requests.get(suggestion).json()
#     qinghua_response = requests.get(qinghau).json()
#     # now
#     weather = now_response['results'][0]['now']['text']
#     weather_code = now_response['results'][0]['now']['code']
#     temperature = now_response['results'][0]['now']['temperature']
#     # daily
#     text_day = daily_response['results'][0]['daily'][0]['text_day']
#     text_night = daily_response['results'][0]['daily'][0]['text_night']
#     code_day = daily_response['results'][0]['daily'][0]['code_day']
#     code_night = daily_response['results'][0]['daily'][0]['code_night']
#     high = daily_response['results'][0]['daily'][0]['high']
#     low = daily_response['results'][0]['daily'][0]['low']
#     # suggestion
#     comfort = suggestion_response['results'][0]['suggestion'][0]['comfort']['details']
#     uv = suggestion_response['results'][0]['suggestion'][0]['uv']['details']
#     # qinghua
#     qinghau = qinghua_response['content']
#     return weather, weather_code, temperature, text_day, text_night, code_day, code_night, high, low, comfort, uv, qinghau
#
#
# weather, weather_code, temperature, text_day, text_night, code_day, code_night, high, low, comfort, uv, qinghua = gat_weather_info()
#
#
# def image_to_base64(image_path):
#     with open(image_path, "rb") as image_file:
#         encoded_string = base64.b64encode(image_file.read())
#         return encoded_string.decode('utf-8')
#
# print(gat_weather_info())
# with open('weather.html', 'r', encoding='utf-8') as f:
#     con = f.read()
# variables = {
#     'card_color': '#87CEEB',
#     'header_color': '#87CEEB',
#     'week': inday()[1],
#     'weather': weather,
#     'now_temperature': temperature,
#     'max_temperature': high,
#     'min_temperature': low,
#     'text_day': text_day,
#     'text_night': text_night,
#     'comfort': comfort,
#     'uv': uv,
#     'inday': inday()[0],
#     'qinghua': qinghua,
#     'weather_icon': image_to_base64('white/' + weather_code + '.png'),
#     'day_icon': image_to_base64('white/' + code_day + '.png'),
#     'night_icon': image_to_base64('white/' + code_night + '.png'),
# }
# template = string.Template(con)
# formatted_content = template.safe_substitute(variables)
# with open(str(datetime.today().strftime("%Y-%m-%d"))+'.html', 'w', encoding='utf-8') as file:
#     file.write(formatted_content)

# import base64
#
#
# # 读取图片并转换为Base64编码
# def image_to_base64(image_path):
#     with open(image_path, "rb") as image_file:
#         encoded_string = base64.b64encode(image_file.read())
#         return encoded_string.decode('utf-8')
#
#
# # 保存Base64编码到文件
# def save_base64_to_file(encoded_string, output_file):
#     with open(output_file, "w") as file:
#         file.write(encoded_string)
#
#
# # 示例：将图片转换为Base64编码并保存到文件
# image_path = "image/jiantou.png"  # 替换为实际图片路径
# output_file = "output.txt"  # 替换为输出文件路径
#
# # 将图片转换为Base64编码
# encoded_string = image_to_base64(image_path)
#
# # 保存Base64编码到文件
# save_base64_to_file(encoded_string, output_file)
#
# print("Base64 encoding saved to:", output_file)
import datetime
data = 1
# 获取当前日期
today = datetime.date.today()

# 输出当前日期
print("今天的日期：", today)