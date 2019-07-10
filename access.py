# -*- coding: utf-8 -*-

import requests

def getToken():
    r = requests.get('http://localhost:8080/token')
    return r.text
    
if __name__ == '__main__':
    print(getToken())