# -*- coding: utf-8 -*-
"""
# @Time         : 2021/11/8 22:22
# @Author       : ChenLvLei
# @Email        : 2516455367@qq.com
# @FileName     : spider_test
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
import os
from os.path import split

from fastapi import APIRouter

from config import CrawlerScriptAddress

spider_test = APIRouter()


@spider_test.get("/{spiders_path}/{parameters}")
def spiders_files_search(spiders_path: str, parameters: str):  # 函数的顺序就是路由的顺序
    spiders = [os.path.join(spider_path, file_name)
               for spider_path in CrawlerScriptAddress
               for file_name in os.listdir(spider_path)
               if file_name != '__init__.py']
    for spider in spiders:
        if spiders_path in spider and parameters in spider:
            print('已经查找到：', spider, spiders_path, split(spider)[1])

    return {"message": "This is a {}".format('a')}
