# coding=utf8
# author:kang
# url编码转化

import os,sys,urllib

curPath = os.path.abspath(os.path.dirname(__file__))  
rootPath = os.path.split(curPath)[0]  
sys.path.append(rootPath)

class encode_url():
#--generate random data--------------------------------
    def encodeurl(self,url_str):
        return urllib.request.unquote(url_str)
