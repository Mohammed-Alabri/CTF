* challange: ```legacyopt```
* link: https://dreamhack.io/wargame/challenges/1532

```python
hashh = b"\x88\x66\x44\x11\x77\x55\x22\x33"

enc_flag = bytes.fromhex(
    "220c6a33204455fb390074013c4156d704316528205156d70b217c14255b6ce10837651234464e")

i = 8 - len(enc_flag) % 8
flag = ""
for j in range(len(enc_flag)):
    flag += chr(hashh[i % 8] ^ enc_flag[j])
    i += 1
    
print(flag)
```
