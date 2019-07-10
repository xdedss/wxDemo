# -*- coding: utf-8 -*-
# filename: handle.py

import auto_response as ar
import receive
import reply
import hashlib
import web
from breakpoint import breakpoint

class Handle(object):
    def GET(self):
        try:
            data = web.input()
            if len(data) == 0:
                return "hello, this is handle view"
            signature = data.signature
            timestamp = data.timestamp
            nonce = data.nonce
            echostr = data.echostr
            token = "233333"

            list = [token, timestamp, nonce]
            list.sort()
            sha1 = hashlib.sha1()
            map(sha1.update, list)
            hashcode = sha1.hexdigest()
            print("handle/GET func: hashcode, signature: ", hashcode, signature)
            if hashcode == signature:
                return echostr
            else:
                return ""
        except Exception as Arg:
            return Arg
    
    def POST(self):
        try:
            webData = web.data()
            #print("Handle Post webdata is ", webData)
            recMsg = receive.parse_xml(webData)
            if isinstance(recMsg, receive.Msg):
                return ar.response(recMsg)
            else:
                print("暂且不处理")
                return "success"
        except Exception as Arg:
            print(' ' + str(Arg) + ' ')
            return Arg