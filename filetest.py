#!/use/bin/env python

with open('s.txt', 'w') as f:
    f.write('12\n')
    f.write('155\n')
    f.write('0\n')
with open('s.txt', 'r') as f:
    s = f.readlines()
ss = [x.strip() for x in s]
print(ss)
