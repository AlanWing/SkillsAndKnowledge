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