
import datetime
import time

from flask import Flask,request
'''创建一个接受接口的服务器，用于postman做MOCK档板测试'''
#用flask 创建一个简单的接口
app = Flask(__name__)
#构造一个post请求
@app.route('/query_bank_check_amount',methods=['get'])    #对应请求API 和请求方法
def test_post():
    data={
    "returnCode":0,
    "errorCode":"0",
    "returnMsg":"操作成功",
    "result":{"pnpBal": "100.16", "pnpInt": "100", "totFee": "200"}}

    # 设置延迟几秒再响应，如等5秒再响应，也可用于验证前端请求后还未返回前是否能重复再次点击
    time.sleep(1)

    return data

@app.route('/query_bank_check_amount1',methods=['get'])    #对应请求API 和请求方法
def test_post1():
    data={
    "returnCode":0,
    "errorCode":"0",
    "returnMsg":"操作成功",
    "result":{"pnpBal": "100.16", "pnpInt": "100", "totFee": "200"}}

    time.sleep(5)

    return data

#本地运行
if __name__ == '__main__':
    app.run('192.168.88.30','9999')