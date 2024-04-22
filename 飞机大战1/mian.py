from PIL import Image, ImageTk
import tkinter as tk
root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=700)
background_img=tk.PhotoImage(file="background.png")
canvas.create_image(0,0,anchor=tk.NW,image=background_img)
canvas.pack()
image = Image.open("me1.png")
image_tk = ImageTk.PhotoImage(image)
image_obj = canvas.create_image(0, 0, anchor="nw", image=image_tk)
step = 10
def move_image(event):
    key = event.keysym
    if key == "Up":
        canvas.move(image_obj, 0, -step)
    elif key == "Down":
        canvas.move(image_obj, 0, step)
    elif key == "Left":
        canvas.move(image_obj, -step, 0)
    elif key == "Right":
        canvas.move(image_obj, step, 0)
canvas.bind("<KeyPress>", move_image)
canvas.focus_set()
# 定义鼠标点击事件的处理函数
# def start_move(event):
#     global start_x, start_y
#     start_x = event.x
#     start_y = event.y
#
# # 定义鼠标移动事件的处理函数
# def move_image(event):
#     global start_x, start_y
#     if start_x is not None and start_y is not None:
#         # 获取移动的位移
#         dx = event.x - start_x
#         dy = event.y - start_y
#         # 移动图片的位置
#         canvas.move(image_obj, dx, dy)
#         # 更新鼠标点击的位置
#         start_x = event.x
#         start_y = event.y
#
# # 处理鼠标点击事件
# canvas.bind("<Button-1>", start_move)
#
# # 处理鼠标移动事件
# canvas.bind("<B1-Motion>", move_image)
# 启动主循环
root.mainloop()

