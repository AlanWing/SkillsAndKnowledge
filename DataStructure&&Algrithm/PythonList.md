# two_dimentional list

```python
Wrong: [[0]*10]*10 
# In this way, every one-dimentional list will point to the same place in heap.

Right: [[0]*10 for i in range(10)]
```