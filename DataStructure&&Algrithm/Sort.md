# Insertion Sort
```python
def insertion(array:list):
    for i in range(array):
        cursor = array[i]
        index = i
        while index>0 and array[index-1]>array[index]:
            array[index] = array[index-1]
            index-=1
```