* challenge ```SingleByteXor```
* link: https://dreamhack.io/wargame/challenges/559

```python
hashh = "54586b6458754f7b215c7c75424f21634f744275517d6d"
hexx = [int(hashh[i:i+2], 16) for i in range(0, len(hashh), 2)]

for i in range(256):
    res = ""
    for j in hexx:
        res += chr(j ^ i)
    if "DH" in res:
        print(res)
        break


```
