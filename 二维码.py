# 1.导包 借了一个 二维码工具来用 helpers=二维码工具
from segno import helpers

# 2.用工具来编辑个人信息 并且放到变量里面去
a = helpers.make_mecard(name="v",email="2443057264@qq.com",phone='18368214405')
# 3.将变量a的数据保存到 图片文件里面去 并且取名，scale=设置图片比例大小
a.save("v.png", scale="20")
