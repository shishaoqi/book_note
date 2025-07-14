### 别名设置
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.ci commit
git config --global alias.br branch
git config --global alias.lg "log --color --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit"

### 重写历史
https://git-scm.com/book/zh/v2/Git-%E5%B7%A5%E5%85%B7-%E9%87%8D%E5%86%99%E5%8E%86%E5%8F%B2

### 用户设置
$ git config --global user.name shishaoqi
$ git config --global user.email shishaoqi@huayun.com

### 回退
先使用 git log 查看 commit日志 或 git reflog，找到需要回退的那次commit的 哈希值，
git reset --hard commit_id

### 回退上一次
git reset --hard HEAD^

### 取消暂存
git reset HEAD --
取消暂存别名：
git config --global alias.unstage 'reset HEAD --'
### 取消指定文件暂存
git reset HEAD <文件>

### 修改提交信息
https://www.jianshu.com/p/0f1fbd50b4be
git commit --amend

### 撤销更改
git checkout -- file
即直接丢弃**工作区**的修改

### 取消本地增加的文件
git clean -df

### 查看最近或某一次提交修改的文件列表相关命令整理
git log --name-status 每次修改的文件列表, 显示状态
git log --name-only 每次修改的文件列表
git log --stat 每次修改的文件列表, 及文件修改的统计
git log -p \<filename\>查看某个文件的修改历史
git log -p -2查看最近2次的更新内容
git whatchanged 每次修改的文件列表
git whatchanged --stat 每次修改的文件列表, 及文件修改的统计
git show 显示最后一次的文件改变的具体内容  
git show commitId 显示某个 commitid 改变的具体内容
git show -5 显示最后 5 次的文件改变的具体内容

### 拉取远程分支
git checkout -b 本地分支名xxx origin/远程分支名xxx

### 删除远程分支
git push origin --delete \<branchName\>

### 删除不存在对应远程分支的本地分支
可以将(其)从本地版本库中去除
git remote prune origin
简单的方法是使用这个命令:
git fetch -p

### 从版本控制中去除
git rm -r -n --cached "bin/" //-n：加上这个参数，执行命令时，是不会删除任何文件，而是展示此命令要删除的文件列表预览。
git rm -r --cached  "bin/"      //最终执行命令. 
git commit -m" remove bin folder all file out of control"    //提交
git push origin master   //提交到远程服务器

### git分支改名
如果对于分支不是当前分支，可以使用下面代码：
    git branch -m 原名 新

如果是当前，那么可以使用加上新名字
    git branch -m  新分支名

### 重命名远程分支
在git中重命名远程分支，其实就是先删除远程分支，然后重命名本地分支，再重新提交一个远程分支。
git push --delete origin \<remote branchName\>
git branch -m \<local branchName\> \<new local branchName\>
git push origin \<new local branchName\>


### 提交到远程库
git remote add origin git@github.com:shishaoqi/huobi-api.git
git remote add origin git@shishao.320.io:/usr/local/git-repository/huobi.git

### 把本地分支提交到远程
git push --set-upstream origin local


### git库 忽略filemode变更
git config --add core.filemode false


### 将本地所有标签一次性提交到git服务器
git push origin -–tags



### If the identity used for this commit is wrong, you can fix it with:
git commit --amend --author='Your Name <you@example.com>'

//http://ruby-china.org/topics/939
git log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr)%Creset' --abbrev-commit --date=relative

### 可以查找某一个作者所有的提交
git log --author=“author”

### tag标签操作
git tag -a v1.0.5 -m '版本1.0.5'
git push origin v1.0.5

### tag del
git tag -d v1.4-lw
### 从任何远程仓库中移除这个标签
git push origin :refs/tags/v1.4-lw

### 一次性推送很多标签
git push origin --tags

### 增量更新打包
git diff  59082e980 533132c8 --name-only | xargs tar -czvf ../updateUserconsole.tar.gz