# markdown
此文档编写于https://dillinger.io/

# git
安装以及配置：
  - sudo apt-get install git
  - git config --global user.name "liuzhihong"
  - git config --global user.email "eliuzhihong@163.com"
  - git config --list
  - ssh-keygen -t rsa -C "eliuzhihong@163.com"
  - 进入 cd ~/.ssh ，复制.pub到github账号
  - cd /data
  - sudo git clone https://github.com/EdwinChanYi/jigeyi

拉取代码（在服务器拉取合并代码需切换到root，su root）：
  - git branch
  - git checkout your-self-branch
  - git fetch
  - git rebase origin/master
  
提交代码：
  - git checkout your-self-branch
  - git status
  - git add file
  - git commit -m'fix'
  - git fetch
  - git rebase origin/master
  - 若有冲突文件,修改冲突文件，然后 git add file, git rebase --continue，有多个冲突文件只能逐一修改
  - git push origin yout-self-branch
 
其他使用：
  - 查看合并日志 git log
  - 查看修改 git diff file
  - 切提交 git cherry-pick commit-id

# 部署信息

  - 服务器：
   外网ip：120.77.39.207
   操作系统：Ubuntu 16.04.2
  - 登录账号(密码)：
  - 数据库:
   host:rm-wz9w892l7tx6jooryco.mysql.rds.aliyuncs.com
   user:root
   port:3306
   pwd:Jigeyi666
  - redis（不允许外网连接，只能从服务器上连接）：
   host:r-wz9c0b83bea39e74.redis.rds.aliyuncs.com
   port:6379
   pwd:Jigeyi666
  
### 部署步骤
1.系统自带python2.7和python3.5，对应命令是python，python3
2.安装pip，系统自带了python2.7对应的pip，安装python3.5对应的pip3，指令：sudo apt-get install python3-pip

### 本地开发设置测试变量
设置本地环境变量DEBUG_JIGEYI=1
调用common.Function.isDebug()判断是否是开发环境

### 设置项目下library为项目路径
1.在模块下载默认目录，通常为/usr/local/lib/python3.6/site-packages下新增文件jigeyi.pth
2.在jigeyi.pth中输入/data/jigeyi/library保存退出
3.则会引入/data/jigeyi/library下面的模块
4.每将一个模块移至library，需在library下的__init__下import对应模块

nohup python3 main.py >main.log 2>&1 &




