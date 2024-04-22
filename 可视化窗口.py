import sys;
import pygame
# #pygame必须初始化
pygame.init()
# 初始化
# 设置窗口为600*600
screen = pygame.display.set_mode((600, 500))
# 设置字体
pygame.display.set_caption('Drawing Circles')
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
screen.fill = ((0, 0, 200))
color = 255, 255, 0
position = 300, 250
radius = 100
width = 10
pygame.draw.circle(screen, color, position, radius, width)
pygame.display.update()
# #设置主屏窗口
# screen=pygame.display.set_mode((400,400))
# #设置窗口的标题
# pygame.display.set_caption('hello world')
# #导入字体
# f=pygame.font.Font()
# # 生成文本信息，第一个参数文本内容；第二个参数，字体是否平滑；
# # 第三个参数，RGB模式的字体颜色；第四个参数，RGB模式字体背景颜色
# text=f.render('zzk',True,(255,255,0),(0,0,0))
# #获取显示对象的rect区域
# textRect=text.get_rect()
# #设置居中
# textRect.center=(200,200)
# # 将准备好的文本信息，绘制到主屏幕 Screen 上。
# screen.blit(text,textRect)
# while True:
#     # 循环获取事件，监听事件状态
#     for event in pygame.event.get():
#         # 判断用户是否点了"X"关闭按钮,并执行if代码段
#         if event.type == pygame.QUIT:
#             #卸载所有模块
#             pygame.quit()
#             #终止程序，确保退出程序
#             sys.exit()
#     pygame.display.flip() #更新屏幕内容

