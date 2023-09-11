import requests
# 正则表达式
import re
# view-source 在网页中打开网页源代码
# 1号url='https://read.qidian.com/chapter/vUbculV4XEVY1sEsPcaxkg2/9uoR8aVLTz34p8iEw--PPw2/'
url='https://www.qidian.com/book/1036843680/'
#伪装
headers={
'Cookie':'_yep_uuid=b704d83f-e147-7942-14f8-a96fee9f3022; e1=%7B%22l6%22%3A%221%22%2C%22pid%22%3A%22qd_P_xiangqing%22%2C%22eid%22%3A%22qd_G55%22%2C%22l1%22%3A14%7D; e2=%7B%22l6%22%3A%221%22%2C%22pid%22%3A%22qd_P_xiangqing%22%2C%22eid%22%3A%22qd_G55%22%2C%22l1%22%3A14%7D; _csrfToken=YZpXuFCE1oEWKX4tsVf7m2WUrJ4Ekpl1b8OftUCU; newstatisticUUID=1692702697_1808570455; fu=1600134055; Hm_lvt_f00f67093ce2f38f215010b699629083=1692702699; _gid=GA1.2.1918089117.1692702699; supportwebp=true; supportWebp=true; trkf=1; traffic_utm_referer=https%3A//cn.bing.com/; qdrs=0%7C3%7C0%7C0%7C1; navWelfareTime=1692703149909; showSectionCommentGuide=1; qdgd=1; lrbc=1036843680%7C750089779%7C0; rcr=1036843680; bc=1036843680; Hm_lpvt_f00f67093ce2f38f215010b699629083=1692703150; _ga=GA1.1.471419996.1692702699; _ga_FZMMH98S83=GS1.1.1692702699.1.1.1692703168.0.0.0; _ga_PFYW0QLV3P=GS1.1.1692702699.1.1.1692703168.0.0.0',
# 防盗链
'Referer':'https://www.qidian.com/free/',
'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.203'
}
# 1号request=requests.get(url,headers=headers).text
request = requests.get(url, headers=headers).text
list=re.findall('<li class="chapter-item" .*?"><a class="chapter-name" href="(.*?)" .*?">(.*?)</a>  </li> ',request)
for link ,title in list:
    link='https:'+link
    request = requests.get(link, headers=headers).text
#     # 获取数据
    data=request.text
#
#     # 第一参数匹配的规则（.*？）匹配任意字符 换行除外
#     # 第二参数是匹配地址
#     # re。S匹配换行
#     # 以列表返回
    text=re.findall(' <div class="read-content j_readContent" id=".*?">(.*?)</div>',data,re.S)[0]
#     # 小说内容处理 \n为换行
    text=title+'\n\n'+text.replace('<p>' ,'\n')
    # text=text.replace('</p>','')
#     print(text)
#     # 保持数据
    with open('大明：登基第一剑，先斩太上皇.txt',mode='a' ,encoding='utf-8') as f:
        f.write(text)