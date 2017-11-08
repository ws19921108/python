#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import json
from aip import AipSpeech
""" 你的 APPID AK SK """
APP_ID = '10327660'
API_KEY = 'OViqwGxnG9Q4Ogo2tkzeIvlA'
SECRET_KEY = '4c24672b7efcc563af486010e740b030'
aipSpeech = AipSpeech(APP_ID, API_KEY, SECRET_KEY)


# 读取文件
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()
# 识别本地文件
res = aipSpeech.asr(get_file_content('16k.pcm'), 'pcm', 16000, {
    'lan': 'zh',
})
#
#
# # 从URL获取文件识别
# aipSpeech.asr('', 'pcm', 16000, {
#     'url': 'http://121.40.195.233/res/16k_test.pcm',
#     'callback': 'http://xxx.com/receive',
# })

result = res['result']

print result[0]


result  = aipSpeech.synthesis(result[0], 'zh', 1, {
    'vol': 5,
})

# 识别正确返回语音二进制 错误则返回dict 参照下面错误码
if not isinstance(result, dict):
    with open('auido.mp3', 'wb') as f:
        f.write(result)