#!/use/bin/env python
import cv2
from convertToBinString import hex_to_bin,bin_to_hex
s = 12
print(s.bit_length())
print(s.__sizeof__())
print(str(s))
str_num = str(bin(s).replace('0b',''))
str_num = '0'*(16 - len(str_num)) + str_num
print(str_num)
num = int('0b' + str_num, 2)
print(num)
position = ('0'*63)+'1'+('0'*15)+'1'+('0'*31)+'1'+('0'*15)+'1'
head_len = str(bin(len(position)).replace('0b', ''))
head_len = '0'*(10-len(head_len)) + head_len
grayscale_px =[([0]*2) for i in range(2)]
print(type(grayscale_px))
min_px = 1
print(len(position))
print(grayscale_px)
print(position)
print(grayscale_px)
sss = 'ss'
sss += 's'
print(sss)
s = int('0b1101101101', 2)
print(s)
'''
0000000000000000
0000000000000000
0000000000000000
0000000000000001
0000000000000001
0000000000000000
0000000000000001
0000000000000001
'''

sx = hex_to_bin("abc")
ssx = bin_to_hex(sx)
print(ssx)
lx = len(ssx)
print(ssx[0:int(lx/3)])
print(ssx[int(lx/3):int(2*lx/3)])
print(ssx[int(2*lx/3):lx])






# 打开摄像头并显示

'''
cap=cv2.VideoCapture(0)
i=0
while (1):
    ret, frame = cap.read()
    k=cv2.waitKey(1)
    if k==27:
        break
    elif k==ord('s'):
        cv2.imwrite('D:/py-workspace/'+str(i)+'.bmp',frame)
        i+=1
        break
    cv2.imshow("capture", frame)
cap.release()
cv2.destroyAllWindows()
'''
