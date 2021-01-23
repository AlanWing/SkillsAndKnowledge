# classmethod and staticmethod

+ classmethod  
classmethod is uesd more often in factorial pattern codes, with a decorator "@classmethod" above the function you defined you can call this function without creating an instance. The most important thing is that classmethod can modify the state of a class.  
eg:
```markdown
class Car(object):
    wheels = 4

    @classmethod
    def modify(cls,number):
        cls.wheels = number

    @classmethod
    def show_wheels(cls):
        print(cls.wheels)
A basic class is like something above, once you want to call "modify" function, you do like

Car.modify(5)

After this when you want to check the wheels of this class.
Car.show_wheels()
The result is 5.
```

# OS
## os.mkdir() and os.makedirs()   
+ os.mkdir():  
If you give a long path, any segment of the path should be created before the last one.  
+ os.makedirs(): 
Recursive.


# List
+ Dynamic Array   
Usually when we initialize an array in python(class List), it has a certain length, if we add more elements into this array, it will be expanded dynamically.  
And usually it obeys the steps below.
```mardown
1. Create a larger array.
2. B[i] = A[i], which means array B has the same pointer as array A.
3. Append the new elements in the new array.
```
Tips: Usually we expand 2 times length than before.

+ Amortization （摊销）  
只有当数组涉及到扩容时，才会消耗时间创建新的数组，只向末尾增添元素时间复杂度为O（1） 
为了做摊销分析 我们使用一种特殊的方法来证明
<!-- Only when we expand the array we need time to create,while the time complexity of append method is O(1).   
In order to calculate the time complexity of the dynamic changing. We use amortized analysis algorithem. -->
```markdown
Question: S是一个具有初始大小的动态数组 当数组已满时 将该数组扩大到2倍 
Prove: 假定每次append需要支付一枚硬币,假定扩大数组(从k到2k) 需要支付k枚硬币 我们对每一次增添操作索要3枚硬币.因此 对不需要扩大数组的append操作我们多付了2枚硬币.
```

