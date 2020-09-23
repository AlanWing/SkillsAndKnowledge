# **pip下载国内站点**

~~~markdown
https://pypi.tuna.tsinghua.edu.cn/simple   清华
http://pypi.douban.com/simple   豆瓣

批量下载 pip install -r 123.txt
~~~

**linux**

~~~markdown
运行Pycharm：  进入到bin目录下   ./pycharm.sh
删除文件夹 rm -rf  (r向下递归 f强制删除)
~~~



**mysql本地终端连接虚拟机需要注意的点：**

~~~markdown
虚拟机的防火墙设置要开放3306端口：
	firewall-cmd --add-port=3306/tcp --permanent

MySQL 的user表 要开放权限：
	use mysql                                            #访问mysql库
	update user set host = '%' where user = 'root';      #使root能再任何host访问
	FLUSH PRIVILEGES;                                    #刷新

mysql的配置文件要默认端口号：
	vim /etc/my.cnf
	进入编辑模式
	再[mysqld]下方添加port=3306     #也可自定义
~~~

**redis本地终端连接虚拟机**

~~~markdown
1.虚拟机的防火墙设置端口放行
	firewall-cmd --add-port=6379/tcp --permanent
2.redis配置文件中bind127.0.0.1注释掉
3.protected-mode关闭
4.注释掉 bind 127.0.0.1

配置文件为/etc/redis/redis.conf(在线安装推荐)或者 /usr/local/redis/redis.conf(手动安装)
~~~



# **linux防火墙**

~~~Markdown、
在本地访问linux服务器时要在linux防火墙设置端口放行
1.查看防火墙状态
	查看防火墙状态 systemctl status firewalld
    开启防火墙 systemctl start firewalld  
    关闭防火墙 systemctl stop firewalld
    开启防火墙 service firewalld start 
    若遇到无法开启
    先用：systemctl unmask firewalld.service 
    然后：systemctl start firewalld.service
2.查看对外开放的端口状态
    查询已开放的端口 netstat  -ntulp | grep 端口号：可以具体查看某一个端口号
    查询指定端口是否已开 firewall-cmd --query-port=666/tcp
    提示 yes，表示开启；no表示未开启。
3.对外开发端口
    查看想开的端口是否已开：firewall-cmd --query-port=6379/tcp
    添加指定需要开放的端口：firewall-cmd --add-port=123/tcp --permanent
    重载入添加的端口：firewall-cmd --reload
    查询指定端口是否开启成功：firewall-cmd --query-port=123/tcp
    移除指定端口：firewall-cmd --permanent --remove-port=123/tcp
4. 防火墙目前已开放的端口：
	firewall-cmd --list-all
~~~

# **git**

## git 基本操作

~~~markdown
1. 获取仓库：
	1.本地初始化一个仓库 某一目录下 git init
	2.克隆远程仓库 在某一目录下 git clone git clone https://github.com/libgit2/libgit2
	             可自定义名字 git clone git clone https://github.com/libgit2/libgit2 mylib
2. 查看当前缓存区状态 git status(未改动情况下不会显示)
3. 追踪文件（未追踪、已追踪）：git add
    注意：当add已追踪文件时只暂存最后add那一版 如果之后修改为add commit时不会提交
         因此每修改一次add一次
4. 查看已追踪文件修改后与原来的区别：git diff 文件名

5. 提交更新（已追踪文件）： git commit 这个命令会调到注释界面
                     git commit -m "" 直接提交
6. 从缓存区删除:git rm
           git rm -f 对于已修改过的文件要强制删除
```
一般在本地目录中删除了文件 status会检测出与版本库的区别
如果希望删除 则git rm 然后git commit
如果不希望删除 git checkout -- 文件名
```

7. 版本回退(回退到最后一次提交的版本) git reset --hard SHA1计算后的文件名(需要从log里找) 

8. (未提交前,修改了,未add或已add) 回退到最后一次追踪或加入缓存区之前的状态 git checkout -- 文件名 

9. (未提交前,修改了,并add) 撤销缓存区的修改 git reset HEAD 文件名     意思是将HEAD指向上一个未修改的版本
```
情景一： 一顿乱改 未提交 git checkout -- 文件名
情景二： 一顿乱改 并add  git reset HEAD 文件名 到了场景一
场景三： 一顿乱改 add+commit 直接版本回退 git reset --hard SHA1文件名
场景四： 一顿乱改 add+commit+push    凉凉
```

10. 在缓存区文件改名 git mv

11. 远程仓库名称修改 git remote rename origin <新名字>

12. 修改提交日志	 git commit --amend 

13. merge多次提交为一次 
    git rebase -i HEAD~2   意思是合并之前的两次提交
git remote -v 检查remote内容
git remote rm origin 删除remote内容



git log 查看本地提交历史
git reflog 
git提交流程：
cd 到gitspace
	git init
	git remote add origin http://192.168.1.12:8000/Alan/tornado_test.git
	git add tornado.test.py
	git commit -m "此版本的备注"
	git push -u origin master 

~~~

## git 分支

```markdown
一开始 master分支是一条线 master指向当前文件 HEAD指向当前分支
当创建了分支后 master和dev同时指向当前文件 HEAD指向dev

创建分支： git branch name
查看当前分支：git status/ git branch
切换分支： git switch name/git checkout name
创建并切换： git switch -c name
合并分支： 在分支上commit 切换到主分支(先pull最新版本的代码到本地仓库) merge
删除分支： git branch -d name

一般的协同开发流程：
	master分支是比较稳定的 一般不在上面工作
	dev不稳定 用来版本更替 经测试后上传到master
	而开发组的小伙伴一人拉一条分支进行开发 开发完成之后合并到dev分支

Tips: 在开展新功能完成后需要合并到主分支 但如果未合并进行删除 需要强制-D
      git branch -D name
```

## bugs gix

```markdown
一般的修复bug流程
	在当前分支 git stash 
	切换到主分支 然后另开一条分支 git switch -c iss-101
	修复完bug后 git commit 
	切换主分支 git merge 
	切换到原来的工作分支 git stash list 查看工作状态保存的列表 
	恢复工作状态： 1.git stash apply 恢复工作状态 但list中仍然保留 需用git stash drop 删除
                 2.git stash pop 恢复的同时并删除	             
```



**tornado向前端传送json字符串**

~~~python
如果后端往前端传送到的是dict self.write方法会自动解析成json 但如果是别的类型 须要先转化成dict
在数据库查询到的数据data是列表包含module对象
利用json.dumps方法转换成json字符串
json_str=json.dumps(list(data),default=worksheet_default)
def worksheet_default(u):
    if isinstance(u, Worksheet):
        return {"id":u.id,"name":u.name,"work":u.work,"creat_time":u.create_time}
    
(if you want to send JSON as a different ``Content-Type``, call
        ``set_header`` *after* calling ``write()``).
源码如上 如果想要将json以其他格式传到前端，那么在write方法之后调用set_header()方法
~~~

**tornado后端接收json字符串**

~~~python
前端要以json串的格式发送请求（不能有空的键值对！！！）
jsonbyte = self.request.body   #从前端获取二进制json字符串
jsonstr = jsonbyte.decode("utf-8")   #将二进制json字符串转码为utf-8
obj=json.loads(jsonstr)   #将json字符串转化成python对象
~~~

**Tornado的orm使用--sqlalchemy**

**connection**:

~~~python
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

config={
    连接参数
}

DB_URL="mysql+pymysql://{user}:{password}@{host}:{port}/{database}?{charset}".format(**config)

engine=create_engine(DB_URL)
Base=declarative_base(engine)
Session=sessionmaker(engine)

~~~

**module**:

~~~python
import Base,
from sqlalchemy import Column,Integer,String,Boolean,Datetime
from sqlalchemy.sql import func #用于设置默认时间

class User(Base):
    __tablename__=""#表名
    id=Column(Integer,primary_key=True,autoincrement=True)
    name=Column(String(20),)
    password=Columen(String(50))
    creat_time=Columen(Datetime,default=func.now())

Base.metadata.creat_all(engine)
~~~

**增删改查**

~~~python
	 session=Session()
查:	session.query(User).all()      列表包含多个module对象
增:	session.add(User(name="",password=""))
     session.add(User(**dict{}))   #支持映射
     session.commit()
     session.close()
改:  session.query(User).filter(User.id=="").update({user.name:"",user.password:""})
     session.commit()
删:  session.query(User).filter(User.id=="")[0]
     session.delete()
     session.commit()
    #注意：session在使用的时候创建 在每一次数据库访问操作之后关闭
~~~

**上下文管理器**

```python
Session=sessionmaker(bind=engine)
@contextmanager
class session_context():
    session=Session()
    try:
        yield session
        session.commit()
    except:
        sessiojn.rollback()
    finally:
        session.close()
```



**redis缓存**

~~~markdown
基本是思想：
	在查询操作时，为了减少I/O操作，对于已经查询过的数据短时间内提到redis数据库中，重复访问即可查看
操作：
	在查询时，先查询redis缓存，如果有，直接返回到前端。如果没有，接着再去mysql查找，如果在mysql找到，先存入缓存（设置时限），再返回到前端
~~~

**定时任务CronTab**

~~~python
tornado本身可以去定时执行任务 但如果出现服务器终断 则会影响执行时间
因此加入一个Crontab 目的是为了判断任务倒没到准确的执行时间 具体实现：

update_wx_gzh_access_token_cron = '0 */2 * * *'  #给定一个执行的timetable 
def update_wx_gzh_access_token_timer():
    now = datetime.datetime.now()
    if not hasattr(update_wx_gzh_access_token_timer, 'next_time'):
        next_seconds = CronTab(update_wx_gzh_access_token_cron).next(default_utc=False)
        update_wx_gzh_access_token_timer.next_time = now + datetime.timedelta(seconds=next_seconds)
    if now >= update_wx_gzh_access_token_timer.next_time:
        next_seconds = CronTab(update_wx_gzh_access_token_cron).next(default_utc=False)
        update_wx_gzh_access_token_timer.next_time = now + datetime.timedelta(seconds=next_seconds)
        task_worker.apply_async(update_wx_gzh_access_token)
~~~

**定时任务apscheduler**

~~~python
from apscheduler.schedulers.background import BlockingScheduler
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.events import EVENT_JOB_EXECUTED, EVENT_JOB_ERROR
定时任务的存储SQLAlchemy、redis、mongodb
jobstores = {
    'default': SQLAlchemyJobStore(url='sqlite:///jobs.sqlite')
}
scheduler = BlockingScheduler(jobstores=jobstores,)
scheduler.add_job(func=download_excel_to_mysql,
                  trigger='cron',
                  day_of_week='mon-sun', hour='9-23', minute=45,
                  id='cron_dowload_excel_to_mysql',
                  replace_existing=True,
                  misfire_grace_time=2*24*60*60,
                  coalesce=True)
scheduler.start()
~~~



**linux连接远程服务器**

~~~markdown
ssh root@IP
输入密码
~~~

**OTC新控服务器**(生产环境)

~~~markdown
新控OTC
IP：112.74.115.50
root/Ruida@otc321
rss/xinkongotc@200506
~~~

**OTC新控(测试)**

~~~markdown
192.168.5.101
alyssa/123456
root/123456
~~~



**OTC茂源服务器**（14环境）

~~~markdown
茂源OTC
IP：192.168.1.14
rss
123456
~~~

**基金子平台服务器**（14环境）

~~~markdown
IP：192.168.1.14:9901
gss
123456

supervisor:rss/rsstest
~~~

**基金子平台服务器（生产环境）**

```markdown
IP:121.46.13.124
rss
double_nine#124@0909

supervisor:
    配置文件路径： /etc/supervisor/fund.conf
    fund_server web后端进程
    fund_apscheduler 定时任务进程
    fund_celery_worker celery_worker进程
版本发布：
14环境切换到master，执行 python3 /home/gss/fund_management_pro/rsync/rsync_.py  输入密码double_nine#124@0909
```

**OTC茂源服务器（生产环境）**

```markdown
IP:47.106.135.71   
rss/foolsday#0401
root/FoolsDay@0401
```



https://zb.citicsf.com/otcoption/SilverSoftFramework/SilverSoft.Robot.ashx