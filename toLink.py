# coding:utf-8
import base64
import os
import json
import time

global iNo
iNo = 0
os.system("git pull")

os.system("curl -O https://v2ray.neocities.org/v2ray.txt")
os.system("curl -O https://cdn.jsdelivr.net/gh/freefq/free@master/v2")
# vmess://eyd2JzogJzInLCAncHMnOiAn5L2/55So5YmN6K6w5b6X5pu05paw6K6i6ZiFJywgJ2FkZCc6ICfkvb/nlKjliY3orrDlvpfmm7TmlrDorqLpmIUnLCAncG9ydCc6ICcwJywgJ2lkJzogJzI4YWQwOTIyLTViMWItNDVhNi05ZjBiLTBlZmE5NmNiOGY1NScsICdhaWQnOiAnMCcsICduZXQnOiAndGNwJywgJ3R5cGUnOiAnbm9uZScsICdob3N0JzogJycsICdwYXRoJzogJycsICd0bHMnOiAnJ30=
# os.system("echo vmess://eyd2JzogJzInLCAncHMnOiAnMTIzJywgJ2FkZCc6ICfkvb/nlKjliY3orrDlvpfmm7TmlrDorqLpmIUnLCAncG9ydCc6ICcwJywgJ2lkJzogJzI4YWQwOTIyLTViMWItNDVhNi05ZjBiLTBlZmE5NmNiOGY1NScsICdhaWQnOiAnMCcsICduZXQnOiAndGNwJywgJ3R5cGUnOiAnbm9uZScsICdob3N0JzogJycsICdwYXRoJzogJycsICd0bHMnOiAnJ30=> source.txt")
os.system("base64 -d v2 > source.txt")
os.system("base64 -d v2ray.txt >> source.txt")
# exit()
opt = open('source.txt', encoding="utf-8")

lst11 = opt.readlines()
opt.close()


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
    return "LordKidd"+strRes


strRes = ""
for str1 in lst11:
    iNo += 1
    strRes1 = ""
    if("vmess://" in str1):
        strRes1 = VmessClear(str1, iNo, lst11)
    else:
        strRes1 = OtherClear(str1, iNo, lst11)

    if(strRes1 != ""):
        strRes += strRes1 + "\n"
    else:
        pass


if(strRes != ""):
    ipt = open("node.txt", "w", encoding="utf-8")
    ipt.write(strRes)
    ipt.close()
    cmd = "base64 -w 0 node.txt > v2.txt"
    os.system(cmd)
    strTime = time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime())
    strTime2 = "<h1>%s<h1>" % strTime
    ipt = open("index.html", "w", encoding="utf-8")
    ipt.write(strTime2)
    ipt.close()
#    print("echo '%s' > index.html" % strTime2)
#    os.system("echo '%s' > index.html" % strTime2)
    os.system("git add .")
    os.system("git commit -m '%s'" %(strTime) )
    os.system("git push")

else:
    pass
