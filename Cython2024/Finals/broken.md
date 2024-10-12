challange ```Broken```

* In this challange we got pcap file, follow 

```python
file = open("patterns.exe.enc", "rb").read()

out = open("out.exe", "wb")

pattern = b"C7T#F!G8"


for i in range(len(file)):
    out.write(bytes([file[i] ^ pattern[i % len(pattern)]]))


out.close()
```