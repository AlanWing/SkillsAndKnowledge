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

# Copy Databases
Usually we need to copy the total databases on condition that we publish a new version and flush the data of the old tables.  
+ mysqldump   
1.Copy inserts.  
**command**: mysqldump -u root -p classicmodels > d:\db\classicmodels.sql  
Enter password:   
2.Copy database creation and inserts  
**command**: mysqldump -u root -p --databases classicmodels > d:\db\db.sql  
Enter password: 

+ mysql  
**command**: mysql -u root -p classicmodels_backup < d:\db\classicmodels.sql



