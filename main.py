import re
import base64
import json
import html
import requests
from urllib.parse import quote
import time
import urllib.request as urllib2
from collections import Counter
https://github.com/OceanSec/cnvdtools/tree/main
requests.packages.urllib3.disable_warnings()

headers = {
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.9 Safari/537.36',
}

class Account:
    """
    Init all of accounts
    """

    def __init__(self):
        pass
    def Fofakey(self):
        email = "*****************"
        fofa_token = "*****************"
        return email, fofa_token



def getHtml(urls):
    print('---》》使用本地IP《《---')
    try:
        html = requests.get(urls, headers=headers, verify=False)
        return html
    except Exception as u:
        print('lo_err:', u)
        return None
    # 延时，防止请求过快，如果还是太快出现请求错误，可以再调高一些
    time.sleep(1)





def fofa_search(kjgs, gs):

    fofa_size = 10000
    email, token = Account().Fofakey()
    # get top of 10000 results
    search = '"' + kjgs + '"'
    search_data_bs = str(base64.b64encode(search.encode("utf-8")), "utf-8")

    api_request = "https://fofa.info/api/v1/search/all?email=%s&size=%d&key=%s&qbase64=%s&fields=host,title,ip,domain,port,server,protocol,city" % (
        email, fofa_size, token, search_data_bs)
    # print(api_request)

    try:
        json_result = urllib2.urlopen(api_request)
        result = json_result.read()
    except Exception as e:
        print("No result of fscan")
    try:
        # json format read
        fofa_result = json.loads(result)
        # print(fofa_result)
        if fofa_result["error"] == "true":
            print(fofa_result["errmsg"])
        else:
            total = fofa_result["size"]
            total = int(total)
            # judge wether size of result of the fofa scan is more than 200
            if fofa_result["results"] == []:
                print("There no result!")
            else:
                titleresult = []
                # 输出 JSON 数据
                for i in fofa_result["results"]:
                    titleresult.append(i[1])

                frequency = Counter(titleresult)
                sorted_frequency = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
        

                # print(kjgs + "--->结果总数:" + total + "网站标题" + fofa_result['results'])
                print("++++++++++++++++++++++++++++++"+ kjgs + "++++++++++++++++++++++++++++++")
                print("fofa结果数--->",total)
                print("首个网站标题--->",fofa_result['results'][0][1])
                print("出现次数最多的网站标题--->",end=" ")
                for element, count in sorted_frequency:
                    if count >= 10:
                        print(count, html.unescape(element.strip()), end=" ")
                        for i in fofa_result["results"]:
                            if i[1] == element:
                                print(i[0])
                                break
                print("==========================================================================")
                
    except Exception as e:
        # print e
        print("e")
        pass





if __name__ == '__main__':
    # fofa_search("科技")
    # 打开公司列表，获取公司名称
    print("开始收集--------")
    for f in open('gs.txt', 'rb'):
        gs = str(f, "utf-8")
        gs = gs.strip()

        # 获取科技前面的字段
        try:
            if re.search(r'科技', gs):
                start = re.search(r'科技', gs).span()[1]
                kj = gs[:start]

                # 去除括号内容
                if '(' in kj:
                    start = re.search(r'\(', kj).span()[0]
                    end = re.search(r'\)', kj).span()[1]

                    kj_last = kj.replace(kj[start:end], '')

                    fofa_search(kj_last, gs)
                    # q.put(kj_last)
                else:
                    fofa_search(kj, gs)
                    # q.put(kj)

            elif re.search(r'技术', gs):
                start = re.search(r'技术', gs).span()[1]
                kj = gs[:start]
                if '(' in kj:
                    start = re.search(r'\(', kj).span()[0]
                    end = re.search(r'\)', kj).span()[1]

                    kj_last = kj.replace(kj[start:end], '')

                    fofa_search(kj_last, gs)
                    # q.put(kj_last)
                else:
                    fofa_search(kj, gs)
                    # q.put(kj)

            elif re.search(r'软件', gs):
                start = re.search(r'软件', gs).span()[1]
                kj = gs[:start]
                if '(' in kj:
                    start = re.search(r'\(', kj).span()[0]
                    end = re.search(r'\)', kj).span()[1]

                    kj_last = kj.replace(kj[start:end], '')

                    fofa_search(kj_last, gs)
                    # q.put(kj_last)
                else:
                    fofa_search(kj, gs)
                    # q.put(kj)

            elif re.search(r'股份', gs):
                start = re.search(r'股份', gs).span()[0]
                kj = gs[:start]
                if '(' in kj:
                    start = re.search(r'\(', kj).span()[0]
                    end = re.search(r'\)', kj).span()[1]

                    kj_last = kj.replace(kj[start:end], '')

                    fofa_search(kj_last, gs)
                    # q.put(kj_last)
                else:
                    fofa_search(kj, gs)
                    # q.put(kj)

            elif re.search(r'有限', gs):
                start = re.search(r'有限', gs).span()[0]
                kj = gs[:start]
                if '(' in kj:
                    start = re.search(r'\(', kj).span()[0]
                    end = re.search(r'\)', kj).span()[1]

                    kj_last = kj.replace(kj[start:end], '')

                    fofa_search(kj_last, gs)
                    # q.put(kj_last)
                else:
                    fofa_search(kj, gs)
                    # q.put(kj)

            else:
                if '(' in gs:
                    start = re.search(r'\(', gs).span()[0]
                    end = re.search(r'\)', gs).span()[1]

                    gs_last = gs.replace(gs[start:end], '')

                    fofa_search(gs_last, gs)
                    # q.put(kj_last)
                else:
                    kj = gs
                    # print(kj,gs)
                    fofa_search(kj, gs)
                    # q.put(kj)
        except Exception as u:
            print('main_err:', u)
