```python
from numpy import uint8
FIRST = b'\xde\xad\xbe\xef'
MIDDLE = b'\xef\xbe\xad\xde'
LAST = b'\x113Uw\x99\xbb\xdd'

encoded_flag = list(b"\xf8\xe0\xe6\x9e\x7f2h1\x05\xdc\xa1\xaa\xaa\t\xb3\xd8A\xf06\x8c\xce\xc7\xacf\x91L2\xff\x05\xe0\xd9\x91")
# from buttom
for i in range(len(encoded_flag)):
    encoded_flag[i] = uint8(LAST[i % len(LAST)] ^ encoded_flag[i])

for i in range(len(encoded_flag)):
    encoded_flag[i] = uint8(encoded_flag[i] - 0xf3)

for i in range(len(encoded_flag)):
    encoded_flag[i] = uint8(encoded_flag[i] + 0x4d)

for i in range(len(encoded_flag)):
    encoded_flag[i] = uint8(MIDDLE[i % len(MIDDLE)] ^ encoded_flag[i])

for i in range(len(encoded_flag)):
    encoded_flag[i] = uint8(encoded_flag[i] + 0x5a)

for i in range(len(encoded_flag)):
    encoded_flag[i] = uint8(encoded_flag[i] - 0x1f)


for i in range(len(encoded_flag)):
    encoded_flag[i] = uint8(FIRST[i % len(FIRST)] ^ encoded_flag[i])
    
print("".join([chr(i) for i in encoded_flag]))

```
