from PIL import Image, ImageFile, ImageOps
from numpy import double

img=Image.open('54.jpg')
pix=img.load()
# img=img.convert('L')
# img2=img.copy();
# img2=ImageOps.invert(img)
# width,height=img2.size
a=1.3
for x in range (img.width):
    for y in range(img.height):
        r,g,b=pix[x,y]
        # a=img.getpixel((x,y))
        # b=img2.getpixel((x,y))
        # img.putpixel((x,y),(int(a[0]*0.1),int(a[1]*0.1),int(a[2]*0.1)))
        r=min(int(r**a),255)
        g=min(int(g**a),255)
        b=min(int(b**a),255)
        pix[x,y]=(r,g,b)
img.show()
