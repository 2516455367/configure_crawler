# -*- coding: utf-8 -*-
"""
# @Time         : 2021/11/8 22:05
# @Author       : ChenLvLei
# @Email        : 2516455367@qq.com
# @FileName     : run.py
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
import uvicorn
from fastapi import FastAPI
from spider_ptoject import spider_test
app = FastAPI(title="Common reptile API.",
              description="The universal crawler framework is under development.",
              version='0.0.1',
              docs_url='/docs',  # 可以改地址
              redoc_url='/redocs')

app.include_router(spider_test, prefix='/spider_test', tags=['dedicated for development and testing'])

if __name__ == '__main__':
    uvicorn.run('run:app',
                host='127.0.0.1',
                port=8888,
                reload=True, debug=True)
