challange ```cython2```

```python
import cython2

cython2.initialize_global_vars()

enc_flag = cython2.base64.b64decode(cython2.ciphertext_b64)
iv = bytes.fromhex(cython2.IV_hex_str)
key = bytes.fromhex(cython2.KEY_hex_str)


print(cython2.decrypt(enc_flag, iv, key))
```