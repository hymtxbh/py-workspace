#!/use/bin/env python
from PIL import Image
import hashlib
from convertToBinString import bin_to_hex

with open('rgb_min.txt', 'r') as f:
    rgb_key = f.readlines()
ss = [x.strip() for x in rgb_key]
r_min_px = int(ss[0])
r_max_px = int(ss[1])
g_min_px = int(ss[2])
g_max_px = int(ss[3])
b_min_px = int(ss[4])
b_max_px = int(ss[5])
image = Image.open("0_change.bmp", "r")
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
            s += str(r)+str(g)+str(b)
m = hashlib.new('md5')
m.update(s.encode('UTF-8'))
m_hash_hex = m.hexdigest()
print(m_hash_hex)
m_hash_bin = ''
r_m = ''
g_m = ''
b_m = ''
r_head_len = ''
g_head_len = ''
b_head_len = ''
r_position = ''
g_position = ''
b_position = ''
if r_max_px < r_min_px:
    numb = int(0)
    for i in range(w):
        for j in range(h):
            r, g, b = px[i, j]
            if r == r_max_px:
                if numb < 10:
                    r_head_len += '0'
                    numb += 1
                elif 10 <= numb < (10+int('0b' + r_head_len, 2)):
                    r_position += '0'
                    numb += 1
                else:
                    r_m += '0'
                    numb += 1
            elif r == r_max_px + 1:
                if numb < 10:
                    r_head_len += '1'
                    numb += 1
                elif 10 <= numb < (10+int('0b' + r_head_len, 2)):
                    r_position += '1'
                    numb += 1
                else:
                    r_m += '1'
                    numb += 1
                image.putpixel((i, j), (r_max_px, g, b))
            if numb > 10 and numb == (53 + int('0b' + r_head_len, 2)):
                break
        if numb > 10 and numb == (53 + int('0b' + r_head_len, 2)):
                break
    for i in range(w):
        for j in range(h):
            r, g, b = px[i, j]
            if r_max_px < r <= r_min_px:
                image.putpixel((i, j), (r-1, g, b))
    for k in range(int(int('0b'+r_head_len, 2)/32)):
        c_i = int('0b'+r_position[0+(k*32):16+(k*32)], 2)
        c_j = int('0b'+r_position[16+(k*32):32+(k*32)], 2)
        r, g, b = px[c_i, c_j]
        image.putpixel((c_i, c_j), (r_min_px, g, b))
elif r_min_px < r_max_px:
    numb = int(0)
    for i in range(w):
        for j in range(h):
            r, g, b = px[i, j]
            if r == r_max_px:
                if numb < 10:
                    r_head_len += '0'
                    numb += 1
                elif 10 <= numb < (10+int('0b' + r_head_len, 2)):
                    r_position += '0'
                    numb += 1
                else:
                    r_m += '0'
                    numb += 1
            elif (r_max_px-1) == r:
                if numb < 10:
                    r_head_len += '1'
                    numb += 1
                elif 10 <= numb < (10+int('0b' + r_head_len, 2)):
                    r_position += '1'
                    numb += 1
                else:
                    r_m += '1'
                    numb += 1
                image.putpixel((i, j), (r_max_px, g, b))
            if numb > 10 and numb == (53 + int('0b' + r_head_len, 2)):
                break
        if numb > 10 and numb == (53 + int('0b' + r_head_len, 2)):
                break
    for i in range(w):
        for j in range(h):
            r, g, b = px[i, j]
            if r_min_px <= r < r_max_px:
                image.putpixel((i, j), (r+1, g, b))
    for k in range(int(int('0b'+r_head_len, 2)/32)):
        c_i = int('0b' + r_position[0 + (k * 32):16 + (k * 32)], 2)
        c_j = int('0b' + r_position[16 + (k * 32):32 + (k * 32)], 2)
        r, g, b = px[c_i, c_j]
        image.putpixel((c_i, c_j), (r_min_px, g, b))
if g_max_px < g_min_px:
    numb = int(0)
    for i in range(w):
        for j in range(h):
            r, g, b = px[i, j]
            if g == g_max_px:
                if numb < 10:
                    g_head_len += '0'
                    numb += 1
                elif 10 <= numb < (10+int('0b' + g_head_len, 2)):
                    g_position += '0'
                    numb += 1
                else:
                    g_m += '0'
                    numb += 1
            elif g == g_max_px + 1:
                if numb < 10:
                    g_head_len += '1'
                    numb += 1
                elif 10 <= numb < (10+int('0b' + g_head_len, 2)):
                    g_position += '1'
                    numb += 1
                else:
                    g_m += '1'
                    numb += 1
                image.putpixel((i, j), (r, g_max_px, b))
            if numb > 10 and numb == (53 + int('0b' + g_head_len, 2)):
                break
        if numb > 10 and numb == (53 + int('0b' + g_head_len, 2)):
                break
    for i in range(w):
        for j in range(h):
            r, g, b = px[i, j]
            if g_max_px < r <= g_min_px:
                image.putpixel((i, j), (r, g-1, b))
    for k in range(int(int('0b'+g_head_len, 2)/32)):
        c_i = int('0b'+g_position[0+(k*32):16+(k*32)], 2)
        c_j = int('0b'+g_position[16+(k*32):32+(k*32)], 2)
        r, g, b = px[c_i, c_j]
        image.putpixel((c_i, c_j), (r, g_min_px, b))
elif g_min_px < g_max_px:
    numb = int(0)
    for i in range(w):
        for j in range(h):
            r, g, b = px[i, j]
            if g == g_max_px:
                if numb < 10:
                    g_head_len += '0'
                    numb += 1
                elif 10 <= numb < (10+int('0b' + g_head_len, 2)):
                    g_position += '0'
                    numb += 1
                else:
                    g_m += '0'
                    numb += 1
            elif (g_max_px-1) == g:
                if numb < 10:
                    g_head_len += '1'
                    numb += 1
                elif 10 <= numb < (10+int('0b' + g_head_len, 2)):
                    g_position += '1'
                    numb += 1
                else:
                    g_m += '1'
                    numb += 1
                image.putpixel((i, j), (r, g_max_px, b))
            if numb > 10 and numb == (53 + int('0b' + g_head_len, 2)):
                break
        if numb > 10 and numb == (53 + int('0b' + g_head_len, 2)):
                break
    for i in range(w):
        for j in range(h):
            r, g, b = px[i, j]
            if g_min_px <= g < g_max_px:
                image.putpixel((i, j), (r, g+1, b))
    for k in range(int(int('0b'+g_head_len, 2)/32)):
        c_i = int('0b' + g_position[0 + (k * 32):16 + (k * 32)], 2)
        c_j = int('0b' + g_position[16 + (k * 32):32 + (k * 32)], 2)
        r, g, b = px[c_i, c_j]
        image.putpixel((c_i, c_j), (r, g_min_px, b))
if b_max_px < b_min_px:
    numb = int(0)
    for i in range(w):
        for j in range(h):
            r, g, b = px[i, j]
            if b == b_max_px:
                if numb < 10:
                    b_head_len += '0'
                    numb += 1
                elif 10 <= numb < (10+int('0b' + b_head_len, 2)):
                    b_position += '0'
                    numb += 1
                else:
                    b_m += '0'
                    numb += 1
            elif b == b_max_px + 1:
                if numb < 10:
                    b_head_len += '1'
                    numb += 1
                elif 10 <= numb < (10+int('0b' + b_head_len, 2)):
                    b_position += '1'
                    numb += 1
                else:
                    b_m += '1'
                    numb += 1
                image.putpixel((i, j), (r, g, b_max_px))
            if numb > 10 and numb == (52 + int('0b' + b_head_len, 2)):
                break
        if numb > 10 and numb == (52 + int('0b' + b_head_len, 2)):
                break
    for i in range(w):
        for j in range(h):
            r, g, b = px[i, j]
            if b_max_px < b <= b_min_px:
                image.putpixel((i, j), (r, g, b-1))
    for k in range(int(int('0b'+b_head_len, 2)/32)):
        c_i = int('0b'+b_position[0+(k*32):16+(k*32)], 2)
        c_j = int('0b'+b_position[16+(k*32):32+(k*32)], 2)
        r, g, b = px[c_i, c_j]
        image.putpixel((c_i, c_j), (r, g, b_min_px))
elif b_min_px < b_max_px:
    numb = int(0)
    for i in range(w):
        for j in range(h):
            r, g, b = px[i, j]
            if b == b_max_px:
                if numb < 10:
                    b_head_len += '0'
                    numb += 1
                elif 10 <= numb < (10+int('0b' + b_head_len, 2)):
                    b_position += '0'
                    numb += 1
                else:
                    b_m += '0'
                    numb += 1
            elif (b_max_px-1) == b:
                if numb < 10:
                    b_head_len += '1'
                    numb += 1
                elif 10 <= numb < (10+int('0b' + b_head_len, 2)):
                    b_position += '1'
                    numb += 1
                else:
                    b_m += '1'
                    numb += 1
                image.putpixel((i, j), (r, g, b_max_px))
            if numb > 10 and numb == (52 + int('0b' + b_head_len, 2)):
                break
        if numb > 10 and numb == (52 + int('0b' + b_head_len, 2)):
                break
    for i in range(w):
        for j in range(h):
            r, g, b = px[i, j]
            if b_min_px <= b < b_max_px:
                image.putpixel((i, j), (r, g, b+1))
    for k in range(int(int('0b'+b_head_len, 2)/32)):
        c_i = int('0b' + b_position[0 + (k * 32):16 + (k * 32)], 2)
        c_j = int('0b' + b_position[16 + (k * 32):32 + (k * 32)], 2)
        r, g, b = px[c_i, c_j]
        image.putpixel((c_i, c_j), (r, g, b_min_px))
m_hash_bin = r_m + g_m + b_m
s = bin_to_hex(m_hash_bin)
print(s)
image.save("0_rechange.bmp")

#'''