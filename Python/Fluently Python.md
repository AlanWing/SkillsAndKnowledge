# classmethod and staticmethod

+ classmethod
```markdown
classmethod is uesd more often in factorial pattern codes, with a decorator "@classmethod" above the function you defined you can call this function without creating an instance. The most important thing is that classmethod can modify the state of a class,  
eg:
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

# os.mkdir() and os.makedirs()
os.mkdir(): If you give a long path, any segment of the path should be created before the last one.   
os.makedirs(): Recursive.

# Concurrency and Parallelism
+ Concurrency(并发)  
Concurrency are used in those programs which have many I/O waitings. Frameworks can deal with other requests during the waitings of previous' requests.

+ Parallelism(并行)    
Parallelism refers to process one by one, with several processors. In contrast, the main program has to wait during processing with current request.

# *args and **kwargs
+ args  
*args is a length-variable parameter, whatever the para you give, it will be covered by a tuple in the function.   
eg:
```python
def main(*args):
    print(args)
    print(*args)

if __name__ == "__main__":
    main([1,2,3])
    # ([1,2,3],)
    # [1,2,3]
    main()
```

+ kwargs    
kwargs is key-value parameter, we can pass a format like key=value, and it will become a dict in the function. 
eg:  
```python
def main(**kwargs):
    print(kwargs)

if __name__ == "__main__":
    main(a=1)
    # {"a":1}
```


# functools.partial
It returns a new function object with partial arguments in it.
```python
from functool import partial
def multiply(x,y):
    return x*y

partial_func = partial(multiply,5)
pritial__func(y=6)    

Output:30
```