# -*- coding: utf-8 -*-
# https://api.weixin.qq.com/cgi-bin/media/get?access_token=ACCESS_TOKEN&media_id=MEDIA_ID

import requests
import access
import json

def saveImg(picId, filepath):
    r = requests.get('https://api.weixin.qq.com/cgi-bin/media/get?access_token=%s&media_id=%s' % (access.getToken(), picId))
    with open(filepath, 'wb') as file:
        file.write(r.content)

def uploadImg(filePath):
    mediaType = 'image'
    openFile = open(filePath, "rb")
    files = {'file': ('whatever.jpg', openFile, 'image/jpg', {})}
    postUrl = "https://api.weixin.qq.com/cgi-bin/media/upload?access_token=%s&type=%s" % (access.getToken(), mediaType)
    r = requests.post(postUrl, files=files)
    j = json.loads(r.text)
    print('uploaded  ' + r.text)
    return j['media_id']