from flask import g
from flask_cors import cross_origin
from app.public import decorate_body_params,decorate_resource
from flask_restful import Resource
from app.model import ModelUser
import requests
from datetime import datetime
from bs4 import BeautifulSoup

class ResourceLianLian(Resource):

    @cross_origin()
    @decorate_resource()
    def get(self):
        timenow = datetime.now()
        year = str(timenow.year)
        month = str(timenow.month)
        day = str(timenow.day)
        hour = str(timenow.hour)
        minute = str(timenow.minute)
        second = str(timenow.second)
        if timenow.month < 10:
            month = "0" + month
        elif timenow.day < 10:
            day = "0" + day
        elif timenow.hour < 10:
            hour = "0" + hour
        elif timenow.minute < 10:
            minute = "0" + minute
        elif timenow.second < 10:
            second = "0" + second

        timestamp = year + month + day + hour + minute + second
        payload = {"version": "1.0", "oid_partner": "201304121000001004", "user_id": 84, "timestamp": timestamp,
                   "sign_type": "RSA",
                   "sign": "", "busi_partner": "", "no_order": "", "dt_order": "", "name_goods": "支付",
                   "money_order": 10,
                   "notify_url": "", "risk_item": ""}
        r = requests.post('https://cashier.lianlianpay.com/payment/bankgateway.htm', data=payload)
        print(r.text)
        soup = BeautifulSoup(r.text, 'html.parser')
        return soup.prettify()

