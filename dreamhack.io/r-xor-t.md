* challenge ```r-xor-t```
* link: https://dreamhack.io/wargame/challenges/901

  
* bruteforce way:
```python
hashh = b"C@qpl==Bppl@<=pG<>@l>@Blsp<@l@AArqmGr=B@A>q@@B=GEsmC@ArBmAGlA=@q"
res = ""
for i in hashh:
    for j in range(256):
        n = j
        j = (j + 0xd) & 0x7f
        j ^= 3
        if j == i:
            res += chr(n)
            break
        
print(res[::-1])
```

* reverse engineering way:
```python
hashh = b"C@qpl==Bppl@<=pG<>@l>@Blsp<@l@AArqmGr=B@A>q@@B=GEsmC@ArBmAGlA=@q"
hashh = bytearray(hashh)

for i in range(len(hashh)):
    hashh[i] = hashh[i] ^ 3

hashh = hashh[::-1]

for i in range(len(hashh)):
    hashh[i] = hashh[i] - 0xd
print(hashh.decode())
```
