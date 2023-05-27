#该程序用来自动从分子数据库PubChem上根据分子的CID号直接下载三维的结构
#需要准备文件：名为"CID.txt"的文本文件，文件中只需要分子的CID号，第一行为CID
#由于浏览器IE经常会自动更新，因此常遇到无法下载的问题。主要是由于Webdriver版本和浏览器版本不一致带来的。
# 解决方法如下：在文件夹C:\Program Files (x86)\Microsoft\Edge\Application中查询目前浏览器的版本，
#在https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/上下载对应版本
#更换msedgewebdriver.exe文件即可
#author: ylwu
#Date: 2022/10/7



import re
from fake_useragent import UserAgent
from selenium import webdriver
import time

browser = webdriver.Edge('C:\Program Files (x86)\Microsoft\Edge\Application\msedgedriver.exe')
url='https://pubchem.ncbi.nlm.nih.gov/compound/cid'
CID=[]
ua=UserAgent()
CID_file=open("CID.txt",'r',encoding='utf-8')
cid_line=CID_file.readlines()

def ttt(url):
    browser.get (url)

#ttt()

#for i in range(len(cid_line)):
#    cid_url=re.sub(r'cid',cid_line[i],url)
   # 替换url中的cas，使其成为cas编码
 #   headers = {"User-Agent": ua.random}
    # 请求头设置随机,为了反爬虫
#    print(cid_url)
#    ttt(cid_url)
#    text=browser.page_source
    # browser.page_source是获取网页的全部html，下面是通过正则表达式来进行网页的文本内容检索，即获取检索后的网页上的CID编号

url1='https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/CID/cid/record/SDF/?record_type=3d&amp;response_type=save&amp;response_basename=Conformer3D_CID_cid'
for i in range(len(cid_line)):
    cid_url1=re.sub(r'cid',cid_line[i],url1)
   # 替换url中的cas，使其成为cas编码
    headers = {"User-Agent": ua.random}
    # 请求头设置随机,为了反爬虫
    print(cid_url1)
    ttt(cid_url1)
    text=browser.page_source

browser.close()