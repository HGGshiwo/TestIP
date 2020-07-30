from selenium import webdriver
import requests
from lxml import etree
import time

def Ip_Is_useable_abroad(url):   
    ret = 0
    proxies = {'http' : url}
    headers={'Connection':'close'}
    try:
        request=requests.get("http://www.youtube.com",headers=headers,proxies=proxies)
        if request.status_code == 200 :ret=1
    finally:
        return ret

def Ip_Is_useable_in_home(url):
    ret = 0   
    proxies = {'http' : url}
    headers={'Connection':'close'}
    try:
        request=requests.get("http://www.baidu.com",headers=headers,proxies=proxies)
        if request.status_code==200 :ret = 1
    finally:
        return ret        

def Get_Ip_Form_66():
    global iplist
    iplist = []
    _headers = {
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate, sdch',
        'Accept-Language':'zh-CN,zh;q=0.8',
        'Cache-Control':'max-age=0',
        'Connection':'close',
        'Host':'www.66ip.cn',
        'If-None-Match':'W/"b077743016dc54409ebe6b86ba7a869b"',
        'Upgrade-Insecure-Requests':'1',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36',
    }
    _cookies = None
    
    for i in range(1,20):
        html1 = requests.get('http://www.66ip.cn/'+str(i)+'.html',headers=_headers) #爬取前20页
        etree_html = etree.HTML(html1.text)
        try:
            for j in range(2,12):
                ip = etree_html.xpath('//*[@id="main"]//tr[' + str(j) + ']/td[1]/text()')
                port = etree_html.xpath('//*[@id="main"]//tr[' + str(j) + ']/td[2]/text()')
                url="http://"+str(ip[0])+":"+str(port[0])
                if not "市" in etree_html.xpath('//*[@id="main"]//tr['+ str(j) + ']/td[3]/text()'):
                    print(url+' in home:'+str(Ip_Is_useable_in_home(url))+' abroad:'+str(Ip_Is_useable_abroad(url)))
                    #iplist.append(url)
        except:
            pass

if __name__ =="__main__":
    Get_Ip_Form_66()