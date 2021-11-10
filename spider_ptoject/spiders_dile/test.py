# -*- coding: utf-8 -*-
"""
# @Time         : 2021/11/8 23:04
# @Author       : ChenLvLei
# @Email        : 2516455367@qq.com
# @FileName     : test.py
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


def main():
    import requests

    url = "https://fastapi.tiangolo.com/tutorial/first-steps/"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text)
    return response.text

if __name__ == '__main__':
    main()