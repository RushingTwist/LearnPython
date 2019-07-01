from urllib.request import urlopen
import requests
import ssl
from bs4 import BeautifulSoup
import re
import base64
from spider import mail



def getSSR():

    url = 'https://doub.io/sszhfx/'

    # 全局取消证书验证
    ssl._create_default_https_context = ssl._create_unverified_context

    html = urlopen(url)
    # html = requests.get(url)

    bsObj = BeautifulSoup(html, 'html.parser')

    ssrList = bsObj.find_all('a', {'class':'dl1', 'href':re.compile('text=ssr')})

    ssrLinks = []
    for link in ssrList:
        print(link)
        print('\n')

        res = link['href'].split('text=')
        ssrLink = res[-1]
        ssrLinks.append(ssrLink)

    # subContent = 'aaa'
    # # subContent = base64.b64encode(b'{}', ssrList[0])
    # data = subContent.encode(encoding='utf-8', errors = 'strict')
    # print(data)
    #
    # files = {
    #     # 'filePath': '/opt/IBM/upload',
    #     'upload': open('/Users/lynn/Desktop/ssr.txt')
    # }
    # param = {
    #     'fileName':'ssr.txt',
    #     'filePath': '/opt/IBM/upload',
    #     'filePathApp': '/opt/IBM/WebSphere/AppServer/profiles/AppSrv01/installedApps/oadevCell01/mstep_war.ear/mstep.war'
    # }
    # rsp = requests.post('http://218.13.4.194:2003/appDown/UploadServlet',data=param, files=files)
    # print(rsp)

    # send mail
    mail.sendMail(ssrLinks)

if __name__ == '__main__':
    getSSR()