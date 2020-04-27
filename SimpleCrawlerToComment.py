# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 15:40:51 2020

@author: xulim
"""

import requests
import json

def bv2av(bvid):
    site = "https://api.bilibili.com/x/web-interface/view?bvid=" + bvid
    r = requests.get(site)
    print(r.status_code)
    resp = json.loads(r.text)
    if(resp['code']==0):
        return resp['data']['aid']
    else:
        print(resp['message'])
        return -1

def getComment(av, page):
    url = "https://api.bilibili.com/x/v2/reply"
    params = {
        'jsonp':'jsonp',
        'pn':page,
        'type':1,
        'oid':av,
        'sort':2
    }
    r = requests.get(url, params)
    resp = json.loads(r.text)
    replies = resp['data']['replies']
    if replies is None:
        return -1
    else:
        return replies

#--------------------------------main----------------------------------

bv = '1Ht411h72G'
av = bv2av(bv)

page = 0
while(True):
    page = page+1
    replies = getComment(av, page);
    if(replies!=-1): 
        for reply in replies:
            print("uid:{0:<10}name:{1:<15}lv{2}{3}".format(
                    str(reply['member']['mid']),
                    reply['member']['uname'],
                    str(reply['member']['level_info']['current_level']),
                    str(reply['member']['official_verify']['type']))
            )
    else:
        break
    

    