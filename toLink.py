# coding:utf-8
import base64,os,json,time
from codecs import iterdecode
from io import IncrementalNewlineDecoder
global iNo
iNo = 0
str1 = "vmess://ew0KICAidiI6ICIyIiwNCiAgInBzIjogIuW8oOa1qeiKgueCuUBtZmZ4el85MSIsDQogICJhZGQiOiAiMTMzLndnb25nLnh5eiIsDQogICJwb3J0IjogIjUyMzMzIiwNCiAgImlkIjogImIyMGUyYWU5LWI4MjItMzViZS05NjU3LWE4MWJiZWY1YWViNiIsDQogICJhaWQiOiAiMiIsDQogICJzY3kiOiAiYXV0byIsDQogICJuZXQiOiAidGNwIiwNCiAgInR5cGUiOiAibm9uZSIsDQogICJob3N0IjogInQubWUvdnBuaGF0IiwNCiAgInBhdGgiOiAidC5tZS92cG5wb29sIiwNCiAgInRscyI6ICIiLA0KICAic25pIjogIiINCn0="


opt = open('source.txt', encoding="utf-8")

lst11 = opt.readlines()
opt.close()
# lst11 = ['trojan://0d0a53dd-6a0f-47ac-8d0c-6eca674926b2@t1.ssrsub.com:11033#%e6%8c%89%e5%ae%9e%e9%99%85%e7%9c%8b%e9%a3%8e%e6%99%af%e8%af%b4%e7%bf%bb%e5%b0%b1%e7%bf%bb%e5%b0%b1%e6%98%af%e5%af%b9%e6%96%b9']


def VmessClear(strUrl, iNum, lst111):
    str1 = strUrl.replace("vmess://", "")
    user_info = base64.b64decode(str1).decode("utf-8")
    user_dict = json.loads(user_info)
    user_dict['ps'] = Get0(iNum, lst111)
    bytes_url = str(user_dict).encode("utf-8")
    str_url = base64.b64encode(bytes_url)
    str1 = "vmess://" + str(str_url)[2:-1]
    return str1


def OtherClear(strUrl, iNum, lst111):
    iIndex = strUrl.find("#")
    return strUrl[:iIndex]+"#"+Get0(iNum, lst111)


def Get0(iNum, lst111):
    strRes = ''
    iwei = len(str(len(lst111)))
    iNow = len(str(iNum))
    if(iNow < iwei):
        iCount = iwei - iNow
        for i in range(iCount):
            strRes += "0"

    strRes = strRes + str(iNum)
    return strRes


strRes = ""
for str1 in lst11:
    iNo += 1
    strRes1 = ""
    if("vmess://" in str1):
        strRes1 = VmessClear(str1, iNo, lst11)
    else:
        strRes1 = OtherClear(str1, iNo, lst11)

    if(strRes1 != ""):
        strRes += strRes1 +"\n"
    else:
        pass
if(strRes != ""):
    ipt = open("node.txt","w",encoding="utf-8")
    ipt.write(strRes)
    ipt.close()
    cmd = "base64 node.txt > v2.txt"
    print()

    # print(strRes)
    os.system(cmd)
    os.system("git add .")
    os.system("git commit -m '%s'" % (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) ))
    os.system("git push")

    

    # pass
else:
    pass
