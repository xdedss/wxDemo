# -*- coding: utf-8 -*-

import reply
import media
import config
from PIL import Image
#import os
from breakpoint import breakpoint

fixed = {
    '你好啊' : '好啊你',
    '' : '',
}

fixedImg = {
    'huaji' : 'Huaji.jpg',
    '' : '',
}

revdic = {
    '(' : ')',
    ')' : '(',
    '（' : '）',
    '）' : '（',
    'b' : 'd',
    'd' : 'b',
    'p' : 'q',
    'q' : 'p',
    'N' : 'И',
}

def response(recMsg):
    sp = special(recMsg)
    if sp != None:
        return sp
    
    if recMsg.MsgType == 'text':
        return responseText(recMsg)
    elif recMsg.MsgType == 'image':
        return responseImg(recMsg)
    elif recMsg.MsgType == 'voice':
        return responseVoice(recMsg)
    elif recMsg.MsgType == 'location':
        return responseLocation(recMsg)
    else:
        print('unknown type: ' + recMsg.MsgType)
        return reply.Msg().send()

def responseText(recMsg):
    toUser = recMsg.FromUserName
    fromUser = recMsg.ToUserName
    content = rev(recMsg.Content)
    replyMsg = reply.TextMsg(toUser, fromUser, content)
    
    print(fromUser + '  :  ' + recMsg.Content)
    print('Server  :  ' + content)
    
    return replyMsg.send()


def responseImg(recMsg):
    toUser = recMsg.FromUserName
    fromUser = recMsg.ToUserName
    
    mediaId = recMsg.MediaId
    media.saveImg(mediaId, config.temppath + mediaId + '.jpg')
    revImg(temppath + mediaId + '.jpg', config.temppath + mediaId + '_flip.jpg')
    mid = media.uploadImg(config.temppath + mediaId + '_flip.jpg')
    replyMsg = reply.ImageMsg(toUser, fromUser, mid)
    return replyMsg.send()
    

def responseVoice(recMsg):
    toUser = recMsg.FromUserName
    fromUser = recMsg.ToUserName
    
    content = '哈哈哈'
    replyMsg = reply.TextMsg(toUser, fromUser, content)
    
    print(fromUser + '  :  ' + '[voice' + recMsg.MediaId + ']')
    print('Server  :  ' + content)
    
    return replyMsg.send()
    
def responseLocation(recMsg):
    toUser = recMsg.FromUserName
    fromUser = recMsg.ToUserName
    
    content = '哈哈哈地图 ' + recMsg.Label
    replyMsg = reply.TextMsg(toUser, fromUser, content)
    
    print(fromUser + '  :  ' + '[map@' + recMsg.Location_X + ', ' + recMsg.Location_Y + '@' + recMsg.Scale + ']')
    print('Server  :  ' + content)
    
    return replyMsg.send()






def special(recMsg):
    toUser = recMsg.FromUserName
    fromUser = recMsg.ToUserName
    
    if recMsg.MsgType == 'text':
        if recMsg.Content in fixed.keys():
            content = fixed[recMsg.Content]
            replyMsg = reply.TextMsg(toUser, fromUser, content)
            return replyMsg.send()
            
        if recMsg.Content in fixedImg.keys():
            mid = media.uploadImg(config.imgpath + fixedImg[recMsg.Content])
            replyMsg = reply.ImageMsg(toUser, fromUser, mid)
            return replyMsg.send()
        
        if checkSpace(recMsg.Content):
            content = '你 打 字 带 空 格'
            replyMsg = reply.TextMsg(toUser, fromUser, content)
            return replyMsg.send()
        
    return None


def checkSpace(data):
    if len(data) > 5:
        s = data.split(' ')
        totallen = 0
        for c in s:
            totallen += len(c)
            if len(c) > 1:
                return False
        if totallen > 2:
            return True
    return False
    

def revImg(filePath, toFilePath):
    im = Image.open(filePath)
    out = im.transpose(Image.FLIP_LEFT_RIGHT)
    out.save(toFilePath)


def rev(strdata):
    s = u''
    for c in strdata:
        s = revchr(c) + s
    return s
    
def revchr(chardata):
    if(chardata in revdic.keys()):
        return revdic[chardata]
    else:
        return chardata