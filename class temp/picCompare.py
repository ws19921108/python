#coding:utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import urllib2
import json
import requests
url = 'https://api-cn.faceplusplus.com/facepp/v3/compare'
files = {'image_file1': open('data\\1.jpg', 'rb'),'image_file2': open('data\\2.jpg', 'rb')}
payload = {
    'api_key':'slVt2rQyoO4ocSRGWx1uwsgg-10fnFvB',
    'api_secret':'gtqgWcTc-uHMaaxc_DkZ84Q-Phi34LFV',
}

# url = 'https://api-cn.faceplusplus.com/facepp/v3/faceset/create'
# payload = {
#     'api_key':'slVt2rQyoO4ocSRGWx1uwsgg-10fnFvB',
#     'api_secret':'gtqgWcTc-uHMaaxc_DkZ84Q-Phi34LFV',
#     'face_tokens':'9e61c49c3da3dbb24604400c0c2e441f,05f8ede8d9a1d4a9524f98f1c0e314e9,e9818fb76965d258cced3c4149b4a2f7',
# }

# url = 'https://api-cn.faceplusplus.com/facepp/v3/detect'
# files = {'image_file': open('data\\3.jpg', 'rb')}
# payload = {
#         'api_key': 'slVt2rQyoO4ocSRGWx1uwsgg-10fnFvB',
#         'api_secret':'gtqgWcTc-uHMaaxc_DkZ84Q-Phi34LFV',
# }

req = requests.post(url=url,files=files,data=payload)

print req.text

'''
url = 'http://example.com/'  
headers = { 'Host':'example.com',  
                    'Connection':'keep-alive',  
                    'Cache-Control':'max-age=0',  
                    'Accept': 'text/html, */*; q=0.01',  
                    'X-Requested-With': 'XMLHttpRequest',  
                    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36',  
                    'DNT':'1',  
                    'Referer': 'http://example.com/',  
                    'Accept-Encoding': 'gzip, deflate, sdch',  
                    'Accept-Language': 'zh-CN,zh;q=0.8,ja;q=0.6'  
}  
data = None  
req = urllib2.Request(url, data, headers)  
response = urllib2.urlopen(req)  
html = response.read()  
'''



'''
{"confidence": 82.76, "request_id": "1505985690,6d06f638-b7a6-4bef-b8a1-e00521e7c0ee", "time_used": 406, "thresholds": {"1e-3": 62.327, "1e-5": 73.975, "1e-4": 69.101}}
'''