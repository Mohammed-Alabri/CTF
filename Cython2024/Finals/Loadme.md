challange ```LoadMe```

```python
import ctypes


dll = ctypes.CDLL("c:/Users/...path_to_dll.../LoadMe.dll")

print(dll.CallMe())
```