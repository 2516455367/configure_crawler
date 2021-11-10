# -*- coding: utf-8 -*-
"""
# @Time         : 2021/11/8 22:37
# @Author       : ChenLvLei
# @Email        : 2516455367@qq.com
# @FileName     : baidu_est
# @Description  :
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""
import requests

url = "https://www.baidu.com/"

payload={}
headers = {
  'Cookie': 'BAIDUID=8BC1B10D22717D108E2D8C7DDC341820:FG=1; BIDUPSID=8BC1B10D22717D10B1427768F7C62B55; PSTM=1630549132; BD_NOT_HTTPS=1'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
