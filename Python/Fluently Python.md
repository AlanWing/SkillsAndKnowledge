# classmethod and staticmethod

+ classmethod
```markdown
classmethod is uesd more often in factorial pattern codes, with a decorator "@classmethod" above the function you defined you can call this function without creating an instance. The most important thing is that classmethod can modify the state of a class,  
```
eg:
```python
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

+ staticmethod 
```markdown
staticmethod is just like a normal function, it doesn't need any attribute of the class or the instance.
In other words, you can just put it outside of the class.
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

# event loop

This will be a simplified version of asyncio. There are many details that are glossed over here, but it still conveys the idea of how it works.

The general concept of asyncio is that a single Python object, called the event loop, controls how and when each task gets run. The event loop is aware of each task and knows what state it’s in. In reality, there are many states that tasks could be in, but for now let’s imagine a simplified event loop that just has two states.

The ready state will indicate that a task has work to do and is ready to be run, and the waiting state means that the task is waiting for some external thing to finish, such as a network operation.

**Your simplified event loop maintains two lists of tasks, one for each of these states. It selects one of the ready tasks and starts it back to running. That task is in complete control until it cooperatively hands the control back to the event loop.**

**When the running task gives control back to the event loop, the event loop places that task into either the ready or waiting list and then goes through each of the tasks in the waiting list to see if it has become ready by an I/O operation completing. It knows that the tasks in the ready list are still ready because it knows they haven’t run yet.**

**Once all of the tasks have been sorted into the right list again, the event loop picks the next task to run, and the process repeats. Your simplified event loop picks the task that has been waiting the longest and runs that. This process repeats until the event loop is finished.**

An important point of asyncio is that the tasks never give up control without intentionally doing so. They never get interrupted in the middle of an operation. This allows us to share resources a bit more easily in asyncio than in threading. You don’t have to worry about making your code thread-safe.

That’s a high-level view of what’s happening with asyncio. If you want more detail, this StackOverflow answer provides some good details if you want to dig deeper.


# MixIn programming

+ description  
```markdown
Mixin is a kind of base class that should be inherited by sub classes, which will provide some extra methods for instances but don't create a instance. 
```
+ The basic example is something like below
```python
    class MyMixin:

        def setname(this, name):
            this.name = name

        def getname(this):
            return this.name


    class MyClass(MyMixin):
        def __init__(self):
            self.name = "Default"

    my_object = MyClass()
```