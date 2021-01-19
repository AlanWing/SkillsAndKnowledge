# C programming language

## Variable and assignment
+ int 
```markdown
1. Abbreviation of integer, is limited, generally maximum is 2147483647
``` 

+ float
```markdown
1. Abbreviation of floating-point can store a much bigger number than int.
2. But it is slower than int while computing.
3. Approximation, store a 0.1 of float, it may become 0.09999997.
```


## declaration
```markdown
1. we need to declare every variable before using it.
eg: int age;
    float height;

```
**Note: in c99, declarations don't have to be ahead of sentences.**
## assignment
```c
//int
int age;
age = 18;

//float
float height;
height = 192.1f;
```
**Notes: We are allowed to pass an integer to a float like variable,but it's not exactly safe**


## prinf
```c
float height = 192.1f;
printf("Height is %.2f\n ",height);
```

## initialization
```c
int a = 1,b = 2,c = 10; // all of them have an initialization

int a,b,c=10; //only c has an initalization
```

## read /print
```c
scanf("%d",&i);
// read an integer,store into i
```

