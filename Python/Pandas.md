# Pandas

## Series-类似一维数组的对象

特征：索引在左边 值在右边

### Series创建

~~~ python
默认数组创建
obj=Series([4,-7,5,3])   生成一个Series   index默认从0开始
obj2=Series([4,-7,5,3],index=["a","b","c","d"])

通过字典创建：
obj3=Series({"a":1,"b":2,"c":3})
~~~

### Series索引取值

~~~python
可以通过index取值：
obj2["a"]    ---->   4
obj2[["a","b","c"]]    --->返回一个新的Seires 索引与值一一对应
~~~

### Numpy数组运算 （都会保留索引与数的链接）

~~~python
obj2[obj2>0]    ---> 返回一个新的Series 去除小于0的数据

obj2*2  ---> 返回一个新的Series 每一个数字乘2

obj2**2   --->返回一个新的Series 每一个数字平方

np.exp(obj2)   ---> 返回一个新的Series  e的n次幂  (e为一个常数 大概为2.7182)
~~~

### 成员运算 （对于Series的索引）

~~~python
"a" in obj2    ---> True
"e" in obj2    ---> False
~~~

### 数据缺失NaN

~~~python
通过字典创建：
obj3=Series({"a":1,"b":2,"c":3}，index=["b","c","d"])
此时给了一个索引列 结果会显示d对应的数据为NaN 
pandas和Series都有检测数据表是否存在数据缺失的情况
pd.isnull(obj3)   ---> True True False
obj3.isnull       ---> True True False

DataFrame计算时将特殊字段全部转换成Nan 这样计算时会自动被忽略 之后再用fillna()
~~~

### Series进行计算时的自动索引对应

~~~python
当两个Series含有相同部分的索引时 在进行算术运算时可自动找到相应索引进行计算
~~~

### name属性

~~~python
给一个Series对象赋name属性值 
obj3.name= "hello"
给一个Series对象的索引列赋name属性值
obj3.index.name="State"
修改Series对象的索引列值
obj3.index=[]	
~~~

## DataFrame-表格型数据结构

## 行和列全部显示

~~~python
全部显示
#显示所有列
pd.set_option('display.max_columns', None)
#显示所有行
pd.set_option('display.max_rows', None)
#设置value的显示长度为100，默认为50
pd.set_option('max_colwidth',100)
​# 也可用上下文管理器
with option_context('display.max_rows', 10, 'display.max_columns', 5):
~~~

### Dataframe的构建

~~~python
1. python字典结构创建
	data={"state":["Ohio","Ohio","California","Nevada"],
          "year":[2000,2001,2002,2003],
          "pop":[1.5,1.7,3.6,2.9]}
   df=DataFrame(data)
   此种创建会自动添加索引 且全部被有序排列
   
   另外 也可指定列顺序
   df=DataFrame(data,columns=['year','state','pop'])
   也可指定index的值
   df=DataFrame(data,columns=['year','state','pop'],index=['a','b','c','d'])
   可添加多余列 若未在data中找到 会自动填充为NaN

2. 嵌套字典创建
	data={
        "Nevada":{2001:2.4,2002:2.9},
        "Ohio":{2000:1.5,2001:1.7,2002:3.6}
    }
    df1=DataFrame(data)
    嵌套字典在被DataFrame接收时 会被解析成 外层key作为列索引 内层key会被作为行索引
    未对应上的地方自动补成NaN
    res：        Nevada    Ohio
          2000    NaN      1.5
          2001    2.4      1.7
          2002    2.9      3.6
    也可指定列  没有对应的index会自动填充NaN
    df1=DataFrame(data,index=[2001,2002,2003])
    
3. pdata=DataFrame({"Nevada":df1["Nevada"][:-1],
                    "Ohio":df1["Ohio"][:-1]
                   })

DataFrame接受的构建参数
二维ndarray、由数组、列表、元组构成的字典、NumPy结构化、记录数组、Series组成的字典、字典或Series组成的列表
由列表或元组组成的列表 另一个DataFrame、NumPy的MaskedArray
~~~

### 行和列

~~~python
frame.shape[1]    #计算列数
frame.shape[0]    #计算行数
len(frame)        #计算行数

取某一行的值
切片
df.ix["state"]
df.loc[index]

取某一列的值  df.columnindex  df[columnindex]

取某一行某一列  df.loc[index,columnindex]
获取第一列     first_column = df.iloc[:, 0]

添加新的一行de.append(ignore_index=True)
~~~



### DataFrame的赋值取值

~~~python
取列转成一个Series
通过类似字典取键的方式 df["state"]  ---> 得到一个 Series
通过直接调用属性的方式 df.state     ---> 得到一个 Series

新增列或修改当前列并赋值
df["debt"]=16.5  -->全部赋值为16.5
df["debt"]=[i for i in range(4)]  -->从0到3 此种赋值必须长度对应 否则报错
df["debt"]=np.arange(5.) 

将一个Series赋值给DataFrame的某列
val=Series([-1.2,-1.5,-1.7],index=['b','c','d'])
df["debt"]=val
这种赋值索引没有对应的列会自动填充NaN
~~~

### 删除列

~~~python
del df["debt"]
# del df.debt 会报错
~~~

### 嵌套字典创建的转置

~~~python
df.T  --->行于列互换
~~~

### DataFrame添加行与列name

~~~python
df.index.name="year"
df.columns.name="state"
~~~

### df.values

~~~python
df.values()  ---> 返回一个二维ndarray对象
~~~

## 索引对象index

~~~python
Series和DataFrame都有index对象 
~~~

### 重新索引

~~~ python
obj=Series([4.5,7.2,-5.3,3.6],index=["d","c","a","b"])
obj.index=["d","e","f","g"]   这个操作重新换了索引 更改了索引与数据的对应关系
obj.reindex(["a","b","c","d","e"])  根据索引重新排列 对应关系不变 若存在了多的索引自动补NaN

前向填充：
obj=Series([1,2,3,4,5,6],index=[0,2,4])
obj.reindex(range(6),method="ffill")  #bfill/backfill向后填充


DataFrame的重新索引
frame=DataFrame(np.arange(9).reshape((3,3)),index=["a","b","c"],columns=["Ohio","Texas","California"])
res:       Ohio   Texas   California
     a      0       1          2
     b      3       4          5
     c      6       7          8
行重新索引：frame.reindex(['a','b','c','d'])
列重新索引：frame.reindex(columns=['California','Utah','Ohio']) 不存在自动补NaN
~~~

### 丢弃指定轴的项

~~~python
Series:
    s.drop([index1,index2,...])
DataFrame:
    丢弃行：
    df.drop([index1,index2],axis=1)  #axis=1表示对行索引进行操作
    丢弃列：
    df.drop([column1,column2])
~~~

### 索引、选取、过滤

~~~python
Series:
    obj=Series(np.arange(4),index=["a","b","c","d"])
    索引取值可以用index 也可用数字
    obj["a"] obj[0]
    obj[obj<3]

    切片： obj["a":"c"] 封闭区间！！
    也可以切片设置： obj["a":"c"]=5


DataFrame:
    取值：df["two"]    取列名为two的Series
         df[["three","two"]]   取两列
         df [0:1] 取第一行   df[0:2] 取前两行 
    过滤：df[df["three"]>5] 取列名为three并且值大于5的数据
    	 
         df[df>5]=0  将大于5的数据全部赋值为0  
         # 筛选第一列中含有"科目代码"的行
         df.iloc[:,0].str.contains("科目代码")
         # 筛选第一列中含有"科目代码"的行 或者以数字开头的行
         df = df[(df.iloc[:,0].str.contains("科目代码|\d"))]
         # 注:contain在含有Nan的列无法使用,因此要加 nv=False
         df.columns = list(df[df.iloc[:, 0].str.contains("科目代码", na=False)]
~~~

## 算术运算

### 算术中填充值

```python
在两个数据结构进行基本算术操作时 可直接用符号+-*/运算 结果为相同索引行与列的部分进行计算后的并集 相差处自动补NaN

而我们希望将NaN换为指定数字 那么在运算时需调用方法
   df1.add(df2,fill_value=0)   #调用加法方法 NaN位置用0填充
   df1.sub(df2,fill_value=0)   #调用减法方法 NaN位置用0填充
   df1.div(df2,fill_value=0)   #调用除法方法 NaN位置用0填充
   df1,mul(df2,fill_value=0)   #调用乘法方法 NaN位置用0填充
```

### Dataframe与Series之间的运算

~~~python
广播
默认情况根据Series的索引在DataFrame中找对应关系 某个找不到就会形成并集 自动补NaN
若希望使用广播 则需要调用上述方法 需要加axis参数 表名希望在行还是列做广播
~~~

### 函数应用

~~~python
NumPy的函数可直接作用于pandas对象
np.abs(frame)  #取DataFrame的所有数据的绝对值
df.apply(func)  #将某个函数应用到某一行或某一列
df.apply(lambda x:x.max()-x.min(),axis=0) #axis默认为0 每一列的最大值减最小值

format=lambda x:'%.2f'%x
df.applymap(format)

Series有一个应用于元素级的函数map
df["price"].map(format)
~~~

### 排序和排名

~~~python
df.sort_index(axis=0) 根据列索引排列  默认升序 ascending=False 降序
df.sort_index(axis=1) 根据行索引排列
df.sort_index(by="") 根据某一列的值进行排序

ranking:
    给出的序列先按照从小到大给出排名 再根据method对排名进行
obj.rank(method='',ascending=) ascending:可正序倒序

method选项
average：默认 平均排名
min：整个分组最小排名
max：镇个分组最大排名
first：按值在原始数据中出现顺序分配排名
~~~

### 	重复索引

~~~python
在数据表有重复的索引时，可以用is_unique属性判断值是否唯一
frame.index.is_unique  --->True or False
~~~

## 汇总和计算描述统计

### 按照条件分组

```python
关键字：groupby()


```



~~~python
一般是对整个表格进行操作
df.sum() 会统计当前数据表内的数据总和 按列或按列计算（默认axis=0） NA值自动排除
df.mean()求平均值

常用方法：
count 非NA值的数量 
describe 各列汇总统计
min、max  最小值 最大值
argmin、argmax  最小值与最大值的索引位置
idxmin、idxmax  最小值与最大值索引值
quantile 分位数
sum  求和 
mean  求平均
median  50%分位数
mad   根据平均值计算绝对离差
var   方差
std   标准差  
skew  偏度
kurt  峰度
cumsum  累计和(每一行等于本行加上一行的和)
cumprod  样本的累计积（每一行为本行与上一行的积）
pct_change 百分数变化率


Series的corr方法用于计算两个Series中非重叠的 非NA的 按索引对齐值的相关系数  cov用于计算协方差

DataFrame的corr和cov方法以DataFrame的形式返回完整的相关系数或协方差矩阵
~~~

### 唯一值、计数、成员资格 

~~~python
唯一值s.unique
对于一个含有重复元素的Series unique函数返回唯一值数列

计数pd.value_counts(obj,sort=False)
返回一个数列 其中记录了每个元素存在的次数 (只能检测一维数据)
而DataFrame希望实现计数功能时 使用data.apply(pd.value_counts)

成员isin obj.isin(["a","b"])
返回一个数列 其中存在于给定数列的返回True 不存在返回False
~~~

### 处理缺失数据

~~~python
dropna 通过阀值调节对缺失值的容忍度
fillna 指定值或前插入后插入填充数据
isnull 布尔显示数据是否缺失

df.dropna() #过滤掉所有存在na的行 
df.dropna(how="all") #只丢弃全部为na的行
对于列操作，加入axis参数即可


df.fillna(method="") 支持向前填充
参数：method：插值方式 axis：待填充轴 inplace：是否生成副本 limit：可连续填充的最大数量
~~~

### 层次化索引

~~~python
Series的层次化索引 给两层索引
data=Series(np.random.randn(10),index=[['a','a','a','b','b','b','c','c','d','d'],[1,2,3,1,2,3,1,2,2,3]])
DataFrame的层次化索引 行和列都可以有多层索引 在构造时的参数 index和columns都为二维数组

也可以单独创建一个MultiIndex然后可以选择多次复用
列：MultiIndex.from_arrays([l1,l2],names=[a,b])
~~~

### 重排分级顺序

~~~python
df.swaplevel("key1","key2") 互换索引列 数据不发生变化
df.sortlevel(1)  根据所指定的索引列 对索引指定的数据进行排序
~~~

### 根据级别汇总统计

~~~python
在上述的汇总统计函数中加入参数level="" 则可以按分级去计算总和
df.sum(level="index") 按行索引的分级计算总和
df.sum(level="column" axis=1)按列索引的分级计算总和
~~~

### 行索引与列索引转换

~~~python
df.set_index() 将一个或多个列转换成行索引
df.set_index(drop=False) 将一个或多个列转换成行索引 原有的数据会被保存

df.reset_index()将层次化级别的行索引转为列索引
~~~

## 数据加载、存储与文件读取

### 读写文本格式数据

#### 普通读取

~~~python
read_csv  从文件、URL、文件型对象加载带分隔符的数据  默认分隔符为逗号
read_table  从文件、URL、文件型对象加载带分隔符的数据 默认分隔符为\t

对于没有header的数据 可分配默认列名 也可自定义列名
pd.read_csv("",header=None)
pd.read_csv("",names=[])  自定义column列名
pd.read_csv("",names=[],index_col="") 将数据中的某一列作为行索引
pd.read_csv("",names=[],index_col=["",""]) 将数据中的某两列作为层次化行索引

pd.read_table("",sep="\s+") 利用正则 去除数据间的数量不定的空白符
pd.read_csv("",skiprow=[0,2,3]) 跳过某些行

处理缺失字符：
pd.read_csv("",na_values=["NULL"])
为不同列的缺失字符指定NA标记值
pd.read_csv("",na_values={"message":["foo","NA"],"something":["two"]})

常用参数：
path
sep/delimiter
header
index_col
names
skiprows
na_values
nrows
chunksize
~~~

#### 逐块读取

~~~python
指定行数：
read_csv("",nrows=)
逐块获取迭代对象
chunker=pd.read_csv("",chunksize=1000) #返回一个可迭代对象 1000行数据 后续通过循环添加到字典或列表
~~~

### 将数据输出到文本格式

~~~python
data.to_csv("")
data.to_csv(sys.stdout,sep="|")
parameters: 
    sep="|" 分隔符
    na_rep="NULL" 空值填充
    index=False 去除行索引
    header=False 去除列索引
    cols=["a","b","c"] 只写出一部分 并按照指定顺序排列
~~~

## round and fillna
在保留小数以及填充nan时候 要确保数据类型为float或int  
DataFrame.astype(float)

## filter contains
```
ali = ["a","b","c"]
df = df[df["name"].str.contains("|".join(ali),na =False)]
```