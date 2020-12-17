# Core

## Column INSERT/UPDATE defaults

### sclar defaults
```python
Table("mytable",meta,
    Column("some_column", Integer,default=12)
)
# This column's default value is 12
```
```python
Table("mytable", meta,
    Column("somecolumn", Integer,onupdate=25)
)
# This column's 
```

### function
```python
count = 0
def loop():
    global count
    count += 1
    return count

Table("my_table",meta,
    Column(Integer,primary_key=True,default=loop)
)
# same as auto_increment
```

```python
import datetime

t = Table("mytable", meta,
    Column('id', Integer, primary_key=True),
    # define 'last_updated' to be populated with datetime.now()
    Column('last_updated', DateTime, onupdate=datetime.datetime.now),
)
```

### context
```python
def mydefault(context):
    return context.get_current_parameters()['counter'] + 12

t = Table('mytable', meta,
    Column('counter', Integer),
    Column('counter_plus_twelve', Integer, default=mydefault, onupdate=mydefault)
)
# plus 12 over the previous value
```

## Computed Columns
```python
from sqlalchemy import Table, Column, MetaData, Integer, Computed

metadata = MetaData()

square = Table(
    "square",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("side", Integer),
    Column("area", Integer, Computed("side * side")),
    Column("perimeter", Integer, Computed("4 * side")),
)
```

## Identity Columns
```python
from sqlalchemy import Table, Column, MetaData, Integer, Computed

metadata = MetaData()

data = Table(
    "data",
    metadata,
    Column('id', Integer, Identity(start=42, cycle=True), primary_key=True),# 
    Column('data', String)
)
```

## Constraint
+ Core: Write in the table definetion
+ ORM: \_\_table_args\_\_
+ **difference between index and constraint : inline and optside**
refer to https://stackoverflow.com/questions/43275547/slqlalchemy-uniqueconstraint-vs-indexunique-true

### Unique Constraint
```python
from sqlalchemy import UniqueConstraint

meta = MetaData()
mytable = Table('mytable', meta,
    # per-column anonymous unique constraint
    Column('col1', Integer, unique=True),
    Column('col2', Integer),
    Column('col3', Integer),
    # explicit/composite unique constraint.  'name' is optional.
    UniqueConstraint('col2', 'col3', name='uix_1')
    )
```

### Check Constraint
Column level check constraints generally should only refer to the column to which they are placed, while table level constraints can refer to any columns in the table.

**Note that some databases do not actively support check constraints such as MySQL.**
```python
from sqlalchemy import CheckConstraint

meta = MetaData()
mytable = Table('mytable', meta,
    # per-column CHECK constraint
    Column('col1', Integer, CheckConstraint('col1>5')),
    Column('col2', Integer),
    Column('col3', Integer),
    # table level CHECK constraint.  'name' is optional.
    CheckConstraint('col2 > col3 + 5', name='check1')
    )

mytable.create(engine)
```

### Primary Constraint
```python
from sqlalchemy import PrimaryKeyConstraint

my_table = Table('mytable', metadata,
            Column('id', Integer),
            Column('version_id', Integer),
            Column('data', String(50)),
            PrimaryKeyConstraint('id', 'version_id', name='mytable_pk')
        )
```