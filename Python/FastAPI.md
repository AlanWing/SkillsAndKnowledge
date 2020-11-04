# Path operation functions
+ **def and async def**   
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
```
+ The same way, you can declare optional query parameters, by setting their default to None
```python
from typing import Optional
from fastapi import FastAPI
app = FastAPI()
@app.get("/items/{item_id}")
async def read_item(item_id: str, q: Optional[str] = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}
```

+ Enforce the length of optional arguments
```python
from typing import Optional
from fastapi import FastAPI, Query
app = FastAPI()

@app.get("/items/")
async def read_items(q: Optional[str] = Query(None, max_length=50)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

#Another example
q: str = Query(None, max_length=50)
```
# Path Parameters
```python
#Pass "..." to mark it as required
from typing import Optional
from fastapi import FastAPI, Path, Query
app = FastAPI()

@app.get("/items/{item_id}")
async def read_items(
    item_id: int = Path(..., title="The ID of the item to get"),
    q: Optional[str] = Query(None, alias="item-query"),
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results
```
+ Make the Query parameters and Path parameters in order
```python
@app.get("/items/{item_id}")
async def read_items(
    *, item_id: int = Path(..., title="The ID of the item to get"), q: str
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results
```

# Request Body : Pydantic Models
+ Define a individual model class in the back end.   
+ When pass the arguments within POST method, make sure they are json 
```python
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

app = FastAPI()


@app.post("/items/")
async def create_item(item: Item):
    return item
```
**Pydantic model will offer type hints and completion**
+ Multiple body params and query
```python
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

class User(BaseModel):
    username: str
    full_name: Optional[str] = None


@app.put("/items/{item_id}")
async def update_item(
    *,
    item_id: int,
    item: Item,
    user: User,
    importance: int = Body(..., gt=0),
    q: Optional[str] = None
):
    results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
    if q:
        results.update({"q": q})
    return results
```
