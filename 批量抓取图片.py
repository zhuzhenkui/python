# 导入爬虫包
import  requests
import parsel
# 获取目标数据地址
url="https://pic.netbian.com/"
# 抓取整个网页的代码数据
request = requests.get(url).text
# 对数据进行转化并解析
html= parsel.Selector(request)
# 提取图片链接"https://pic.netbian.com"+
imgurl_list=html.css('.clearfix  img::attr(src)').getall()

# 提取列表里的数据 遍历
# print(imgurl_list)
for i in imgurl_list:
    # 抓取每一个图片数据
    i=url+i
    data =requests.get(i).content
    # 提取名字
    name=i.split('/')[-1]
    # 打开图片文件存数据
    open(name,'wb').write(data)