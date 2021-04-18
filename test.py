#!/use/bin/env python
from PIL import Image
import hashlib
image = Image.open("0_rechange.bmp", "r")
w, h = image.size
img_format = image.format
print(img_format)
img_mode = image.mode
print(img_mode)
print('获得图片大小：%sx%s' % (w, h))
px = image.load()
rlist = [0]*256
glist = [0]*256
blist = [0]*256
s = ""
for i in range(w):
        for j in range(h):
            r, g, b = px[i, j]
            rlist[r] = rlist[r]+1
            glist[g] = glist[g]+1
            blist[b] = blist[b]+1
            s += str(r)+str(g)+str(b)
m = hashlib.new('md5')
m.update(s.encode('UTF-8'))
m_hash_hex = m.hexdigest()
print(m_hash_hex)