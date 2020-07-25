# Tornado

线程安全问题：

```markdown
Tornado框架是基于单线程运行，RequestHandler内的方法都不是线程安全的，对于write()，finish()等方法 必须在主线程上调用 
如果使用多线程则在调用上述方法之前 需调用IOLoop.add_callback 将控制切换为主线程
```



RequestHandler.get_argument(name:str,default:None或者Raise error)

```markdown
根据name获取请求参数
如果同一个名字对应多个参数 只取最后一个
会从query和body中寻找
```

RequestHandler.get_arguments(name:str)     --->List

~~~markdown
根据name获取请求参数 返回一个列表
不存在返回空
会从query和body中寻找

~~~

RequestHandler.get_query_argument(name:str,default:None或者Raise error)

```markdown
根据name获取请求URI的参数，若未获取到且未设置默认 则会报错  
若name在URI出现多次 只获取最后一个
```

RequestHandler.get_query_arguments(name:str,)      --->List

```markdown
根据name获取请求URI参数 返回一个列表 
若未获取到则返回空
```

RequestHandler.get_body_argument(name:str,default:None或者Raise error)

```markdown
根据name获取请求参数 
未获取到且未设置默认 报错
从request body中寻找数据
若参数在URI中出现多次 只取最后一次数据
```

RequestHandler.get_body_arguments(name:str)   --->List

```markdown
根据name获取请求参数  返回一个列表
从request body中寻找参数
不存在返回空
```





RequestHandler.finish()   --->Future对象

```markdown
结束响应，结束HTTP请求
将数据传入finish() 等价于 将数据传入write() 再无参调用finish()
```

RequestHandler.render()  --->Future对象

```markdown
根据参数返回模板文件作为响应 渲染一个HTML页面
在调用render()之后会自动调用finish() 因此在render()之后不可再调用任何方法
```

RequestHandler.redirect()  --->None

```markdown
重定向到指定页面
```

RequestHandler.wite()   --->None

```markdown
将数据写入缓冲区
若要将数据返回到网络 调用flush()

若传入的参数为字典 则会自动转成JSON格式 并设置响应头信息"Content-Type"为application/json 
若想更换头信息 则需要在write()之后 调用set_header()
```

RequestHandler.flush()    --->Future对象

```markdown
将缓冲区的数据返回到网络

```



