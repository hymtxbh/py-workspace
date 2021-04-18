#!/use/bin/env python
from PIL import Image
import cv2
import os
from convertToBinString import hex_to_bin


def bin_str(n: 'int', s_s: 'int'):
    str_num = str(bin(s_s).replace('0b', ''))
    str_num = '0' * (n - len(str_num)) + str_num
    return str_num

# 8c373318dda8669ce702869d08f0282b
# 8c373318dda8669ce702869d08f0282b
# 8c373318dda8669ce702869d08f0282b


cap = cv2.VideoCapture(0)
i = 0
while (1):
    ret, frame = cap.read()
    k = cv2.waitKey(1)
    if k == ord('q'):
        cv2.imwrite('D:/py-workspace/'+str(i)+'.bmp', frame)
        i += 1
        break
    cv2.imshow("capture", frame)
cap.release()
cv2.destroyAllWindows()
image = Image.open("0.bmp", "r")
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
# print(r, g, b)
with open(r'C:\Users\hy\Desktop\use\0.txt', 'w') as f:
    f.write(s)
'''
s = ""
#d4174001403fb6f0d2a620bc87748121
for i in range(w):
    for j in range(h):
        aa[grayscale_px[i, j]] = aa[grayscale_px[i, j]] + 1
        s += str(grayscale_px[i, j])
m.update(s.encode('UTF-8'))
m_hash_hex = m.hexdigest()
print(m_hash_hex)
'''
f = os.popen('MD5' + r' C:\Users\hy\Desktop\use\0.txt')

strs = f.readlines()
print(strs[0])
m_hash_bin = hex_to_bin(strs[0])

r_min_v = rlist[0]
r_max_v = rlist[0]
r_min_px = 0
r_max_px = 0
g_min_v = glist[0]
g_max_v = glist[0]
g_min_px = 0
g_max_px = 0
b_min_v = blist[0]
b_max_v = blist[0]
b_min_px = 0
b_max_px = 0
for i in range(256):
    if rlist[i] >= r_max_v:
        r_max_v = rlist[i]
        r_max_px = i
    if glist[i] >= g_max_v:
        g_max_v = glist[i]
        g_max_px = i
    if blist[i] >= b_max_v:
        b_max_v = blist[i]
        b_max_px = i
for i in range(256):
    if rlist[i] < r_min_v or (rlist[i] == r_min_v and abs(r_max_px - i) < abs(r_max_px - r_min_px)):
        r_min_v = rlist[i]
        r_min_px = i
    if glist[i] < g_min_v or (glist[i] == g_min_v and abs(g_max_px - i) < abs(g_max_px - g_min_px)):
        g_min_v = glist[i]
        g_min_px = i
    if blist[i] < b_min_v or (blist[i] == b_min_v and abs(b_max_px - i) < abs(b_max_px - b_min_px)):
        b_min_v = blist[i]
        b_min_px = i
print(r_min_v)
print(r_min_px)
print(r_max_v)
print(r_max_px)
print(g_min_v)
print(g_min_px)
print(g_max_v)
print(g_max_px)
print(b_min_v)
print(b_min_px)
print(b_max_v)
print(b_max_px)
with open('rgb_min.txt', 'w') as f:
    f.write(str(r_min_px) + '\n')
    f.write(str(r_max_px) + '\n')
    f.write(str(g_min_px) + '\n')
    f.write(str(g_max_px) + '\n')
    f.write(str(b_min_px) + '\n')
    f.write(str(b_max_px) + '\n')
r_position = ''
b_position = ''
g_position = ''
if r_min_v != 0:
    for i in range(w):
        for j in range(h):
            r, g, b = px[i, j]
            if r_min_px == r:
                r_position = r_position + bin_str(16, i) + bin_str(16, j)
                if r_max_px < r_min_px < 255:
                    image.putpixel((i, j), (r_min_px + 1, g, b))
                elif r_min_px == 255:
                    image.putpixel((i, j), (254, g, b))
                elif 0 < r_min_px < r_max_px:
                    image.putpixel((i, j), (r_min_px - 1, g, b))
                elif r_min_px == 0:
                    image.putpixel((i, j), (1, g, b))
if g_min_v != 0:
    for i in range(w):
        for j in range(h):
            r, g, b = px[i, j]
            if g_min_px == g:
                g_position = g_position + bin_str(16, i) + bin_str(16, j)
                if g_max_px < g_min_px < 255:
                    image.putpixel((i, j), (r, g_min_px + 1, b))
                elif g_min_px == 255:
                    image.putpixel((i, j), (r, 254, b))
                elif 0 < g_min_px < g_max_px:
                    image.putpixel((i, j), (r, g_min_px - 1, b))
                elif g_min_px == 0:
                    image.putpixel((i, j), (r, 1, b))
if b_min_v != 0:
    for i in range(w):
        for j in range(h):
            r, g, b = px[i, j]
            if b_min_px == b:
                b_position = b_position + bin_str(16, i) + bin_str(16, j)
                if b_max_px < b_min_px < 255:
                    image.putpixel((i, j), (r, g, b_min_px + 1))
                elif b_min_px == 255:
                    image.putpixel((i, j), (r, g, 254))
                elif 0 < b_min_px < b_max_px:
                    image.putpixel((i, j), (r, g, b_min_px - 1))
                elif b_min_px == 0:
                    image.putpixel((i, j), (r, g, 1))
r_len_bin = bin_str(10, len(r_position))
g_len_bin = bin_str(10, len(g_position))
b_len_bin = bin_str(10, len(b_position))
r_m_hash_bin = r_len_bin + r_position + m_hash_bin[0:43]
g_m_hash_bin = g_len_bin + g_position + m_hash_bin[43:86]
b_m_hash_bin = b_len_bin + b_position + m_hash_bin[86:128]
if r_max_px < r_min_px:
    for i in range(w):
        for j in range(h):
            r, g, b = px[i, j]
            if r_max_px < r < r_min_px:
                image.putpixel((i, j), (r+1, g, b))
    numb = int(0)
    for i in range(w):
        for j in range(h):
            r, g, b = px[i, j]
            if numb == len(r_m_hash_bin):
                break
            if r_max_px == r:
                temp = r + int(r_m_hash_bin[numb])
                image.putpixel((i, j), (temp, g, b))
                numb = numb + 1
        if numb == len(r_m_hash_bin):
            break

elif r_min_px < r_max_px:
    for i in range(w):
        for j in range(h):
            r, g, b = px[i, j]
            if r_min_px < r < r_max_px:
                image.putpixel((i, j), (r-1, g, b))
    numb = int(0)
    for i in range(w):
        for j in range(h):
            r, g, b = px[i, j]
            if numb == len(r_m_hash_bin):
                break
            if r_max_px == r:
                temp = r - int(r_m_hash_bin[numb])
                image.putpixel((i, j), (temp, g, b))
                numb = numb + 1
        if numb == len(r_m_hash_bin):
            break
if g_max_px < g_min_px:
    for i in range(w):
        for j in range(h):
            r, g, b = px[i, j]
            if g_max_px < g < g_min_px:
                image.putpixel((i, j), (r, g+1, b))
    numb = int(0)
    for i in range(w):
        for j in range(h):
            r, g, b = px[i, j]
            if numb == len(g_m_hash_bin):
                break
            if g_max_px == g:
                temp = g + int(g_m_hash_bin[numb])
                image.putpixel((i, j), (r, temp, b))
                numb = numb + 1
        if numb == len(g_m_hash_bin):
            break

elif g_min_px < g_max_px:
    for i in range(w):
        for j in range(h):
            r, g, b = px[i, j]
            if g_min_px < g < g_max_px:
                image.putpixel((i, j), (r, g-1, b))
    numb = int(0)
    for i in range(w):
        for j in range(h):
            r, g, b = px[i, j]
            if numb == len(g_m_hash_bin):
                break
            if g_max_px == g:
                temp = g - int(g_m_hash_bin[numb])
                image.putpixel((i, j), (r, temp, b))
                numb = numb + 1
        if numb == len(g_m_hash_bin):
            break
if b_max_px < b_min_px:
    for i in range(w):
        for j in range(h):
            r, g, b = px[i, j]
            if b_max_px < b < b_min_px:
                image.putpixel((i, j), (r, g, b+1))
    numb = int(0)
    for i in range(w):
        for j in range(h):
            r, g, b = px[i, j]
            if numb == len(b_m_hash_bin):
                break
            if b_max_px == b:
                temp = b + int(b_m_hash_bin[numb])
                image.putpixel((i, j), (r, g, temp))
                numb = numb + 1
        if numb == len(b_m_hash_bin):
            break

elif b_min_px < b_max_px:
    for i in range(w):
        for j in range(h):
            r, g, b = px[i, j]
            if b_min_px < b < b_max_px:
                image.putpixel((i, j), (r, g, b-1))
    numb = int(0)
    for i in range(w):
        for j in range(h):
            r, g, b = px[i, j]
            if numb == len(b_m_hash_bin):
                break
            if b_max_px == b:
                temp = b - int(b_m_hash_bin[numb])
                image.putpixel((i, j), (r, g, temp))
                numb = numb + 1
        if numb == len(b_m_hash_bin):
            break
image.save("0_change.bmp")
# image.show()
