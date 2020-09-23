# Optimization

+ UniqueConstraint
Usually when we want to optimize the speed of query or insert under a big amount of items, we can add a unique constraint among columns.

In this case, we are suppoed to look for some colums that could determine this item unique. For example, "date" for distinguishing different days, "subject_code","amount" for distinguishing different items. 

But not too many columns for the constraint.The fewer, the better.

```python
sqlalchemy:   
    class Fund(Base):
        __tablename__ = ""
        id = Column(Integer,primary=True,autoincrement=True)

        __tableargs__ = (
            UniqueConstraint("column1","column2","column3"),
        )
```