# -*- coding: utf-8 -*-

import web
import time
from datetime import datetime
from datetime import timedelta
import threading
import requests
import json
from breakpoint import breakpoint

tokenstr = ''
validtime = 0

class Handle(object):
    def GET(self):
        #breakpoint('1', [validtime])
        if time.time() > validtime:
            updateToken()
        return tokenstr

def updateToken():
    global tokenstr
    global validtime
    r = requests.get('https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=xxxxxxxxxxxxxxxxxxxxxxxxxx&secret=xxxxxxxxxxxxxxxxxxxxx')#自己改
    j = json.loads(r.text)
    if 'access_token' in j.keys():
        tokenstr = j['access_token']
        slptime = int(j['expires_in']) - 300
        #slptime = 10
        validtime = time.time() + slptime
        print(datetime.now().strftime("%Y-%m-%d %X") + '  ' + tokenstr + '  sleep until ' + str(validtime))
    else:
        print(datetime.now().strftime("%Y-%m-%d %X") + ' failed to get access_token')
        

urls = (
    '/token', 'Handle',
)

if __name__ == '__main__':
    t = threading.Thread(target=updateToken)
    t.setDaemon(True)
    t.start()
    
    app = web.application(urls, globals())
    app.run()
    
    #t.join()
    