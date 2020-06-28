import requests
from bs4 import BeautifulSoup as bs  # bs4 库 BeautifulSoup为包
import pandas as pd

# 前 10 个电影名称、电影类型和上映时间，并以 UTF-8 字符集保存到 csv 格式的文件中。
url = 'https://maoyan.com/films?showType=3'
user_agent = "Mozilla/5.0 (Macintosh;Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER"
cookie = '_csrf=acb2444a72b9aae0d86749dec17bb51c4dcdbdc6b47df29bd04a347d68d3f10f; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593328444; uuid_n_v=v1; mojo-uuid=e8c8db3abafe6ce130e35932c7f6d46d; uuid=A2917F70B90911EA9B3075693A212BAF0F19EEB90A054A84A26E386FFD5A7D54; _lxsdk_cuid=172f9a3d746c8-028d9174841d3d-71415a3a-115bc0-172f9a3d747c8; __mta=121592247.1593326163831.1593326163831.1593328444247.2; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593326163,1593328444; mojo-session-id={"id":"9cb0f9a2efa016007b6c404770abb376","time":1593328444167}; mojo-trace-id=1; _lxsdk=A2917F70B90911EA9B3075693A212BAF0F19EEB90A054A84A26E386FFD5A7D54; _lxsdk_s=172f9c6a32d-96c-dec-bdb%7C%7C2'
header = {'user-agent': user_agent, 'Cookie': cookie}

# 无header的话就会被拦截，无法正常获取网页
response = requests.get(url, headers=header)
# print(response.text)
print(f'返回码是：{response.status_code}')
bs_info = bs(response.text, 'html.parser')

data = pd.DataFrame()
for tag in bs_info.find_all('div', attrs={'class': 'movie-hover-info'}):
    if len(data) > 9:
        break
    # print(tag.find('span', attrs={'class': 'name'}).text)  # 获取电影名称
    name = tag.find('span', attrs={'class': 'name'}).text
    type = ""
    date = ""

    for info in tag.find_all('div', attrs={'class': 'movie-hover-title'}):
        # print(info.text.strip()[0:2])
        if info.text.strip()[0:2] == '类型':
            #    print(info.text.strip())  # 获取电影类型
            type = info.text.strip()
        if info.text.strip()[0:2] == "上映":
            #    print(info.text.strip())  # 获取电影上映时间
            date = info.text.strip()

    mylist={'name':name,'type':type,'date':date}
  #  print(mylist)
    data=data.append(mylist,ignore_index=True)

data.to_csv("maoyan.csv",encoding="utf_8_sig")

