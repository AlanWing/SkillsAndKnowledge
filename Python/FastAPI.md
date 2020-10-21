# Path operation functions
When you declare a path operation function with normal **def** instead of **async def**, it is run in an external **threadpool** that is then awaited, instead of being called directly (as it would block the server).

If your **utility function** is a normal function with def, it will be called directly (as you write it in your code), not in a threadpool, if the function is created with async def then you should await for that function when you call it in your code.

# Path Parameters
+ Declare the path parameters with { }
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/items/iten_id")
def read(item_id:str):
    return {"item_id":item_id}
```

+ Specify the path if you pass a path parameter
```python
@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}
```

# Query Parameters

+ Specify default parameters
```python
fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]
# Here parameter "skip" nad "limit" are default.



#The same way, you can declare optional query parameters, by setting their default to None
from typing import Optional
from fastapi import FastAPI
app = FastAPI()
@app.get("/items/{item_id}")
async def read_item(item_id: str, q: Optional[str] = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}
```


