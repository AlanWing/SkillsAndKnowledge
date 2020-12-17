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


# Connection in  python
+ mysqlclient
```markdown
1. C compiled  
2. difficult to install 
```

+ pymysql 
```markdown
1. Pure python  
2. easy to install
```




# SQL Injection
## example
If you have a login page for admins of you system, your sql expression maybe like this in the backend server:
```python
def is_admin(username: str) -> bool:
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT
                admin
            FROM
                users
            WHERE
                username = '%s'
        """ % username)
        result = cursor.fetchone()

    if result is None:
        # User does not exist
        return False

    admin, = result
    return admin
```
The "username" should be like "Alan", "Haki", or some normal names, but if i passed a string like **"'; select true; --"**, the sql command will become this:
```sql
SELECT admin FROM users WHERE username = ''; select true; --'
```
Mind here! This expression will always return True!
So you will always pass this page.

Not only for select expressions, but also update expressions which it will cause permenant damage
```sql
"'; update users set admin = 'true' where username = 'haki'; select true; --"
```
**"';** here will terminate any expressions and add a new one next:
```sql
update users set admin = 'true' where username = 'haki';
```
And then return True:
```sql
select true; --"
```
## solution
```python
1. cursor.execute("SELECT admin FROM users WHERE username = %s'", (username, ));
2. cursor.execute("SELECT admin FROM users WHERE username = %(username)s", {'username': username});
3. orm
```
