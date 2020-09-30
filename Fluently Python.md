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

+ os.mkdir() and os.makedirs()
os.mkdir(): If you give a long path, any segment of the path should be created before the last one.
os.makedirs(): Recursive.