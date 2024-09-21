hashh = b"IQ\x01CM\x00fS2\x0f\"\x0fX$\x11EXiiX$XEi\x01$\"X\x0c\x0fff\x012fSf2h"
res = ""
for i in hashh:
    for j in range(1, 256):
        if i == (j * 0x34) % 0x7b:
            res += chr(j)
            break
print(res)
