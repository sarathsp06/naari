#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import requests
from settings import sid,token,exophone,flow_id
class Exotel:
    def __init__(self,sid,token):
        self.sid =  sid
        self.token = token
        self.baseurl = 'https://twilix.exotel.in/v1/Accounts/{sid}'.format(sid=sid)

    def sms(self, from_number, to, txt):
        return requests.post(self.baseurl + '/Sms/send.json',
            auth = (self.sid, self.token),
            data = {
                'From': from_number,
                'To': to,
                'Body': txt
             })

    def call(self,from_number,caller_id,flow_id,timelimit):
       return requests.post(self.baseurl + '/Calls/connect.json',
        auth=(self.sid, self.token),
        data={
            'From': from_number,
            'CallerId': caller_id,
            'Url': "http://my.exotel.in/exoml/start/{flow_id}".format(flow_id=flow_id),
            'TimeLimit': timelimit,
            'CallType': "trans",
        })



exotel = Exotel(sid,token)
def sendOtp(number,otp):
    r = exotel.sms(exophone,number,"The SMS is OTP for Naree varification the otp here : {OTP}".format(OTP = otp))
    if r.ok:
        return r.json()['SMSMessage']['Sid']
    else:
        return False

def smsPolice(numbers,lat,long):
    #numbers are send in the assending order of distance from occured place
    for number in numbers:
        r = exotel.sms(exophone,number,"A crime occured at {} location : {},{}".format(str(datetime.datetime.now()),lat,long))
        if r.ok:
            return r.json()['SMSMessage']['Sid']
        else:
            return False


def callPolice(number):
    r = exotel.call(number,exophone,flow_id,180)
    if r.ok:
        return r.json()['Call']['Sid']
    else:
        return False

#sendOtp("9742033616",5423)
#callPolice("9742033616")
#smsPolice(['9742033616','8907965331'],100,212)
