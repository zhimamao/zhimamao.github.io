---
title: Hexo 多台电脑配置+github基础
date: 2022-08-12 22:44:45
categories : 
- hexo
tags: 
- hexo

---
喵
![miao](./hexo%2Bgit%E5%9F%BA%E7%A1%80%E6%80%BB%E7%BB%93/%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20220813230711.jpg)
----------------------------------------------
<table><tr><td bgcolor=white>
本文主要适用于要在两台以上电脑设备使用一个github账号编辑同一个Hexo博客的同步和配置基础
</td></tr></table>
------------------------------------
**准备a.新建一个文件夹 比如blog**

<table><tr><td bgcolor=yellow>在此处执行单一电脑安装Hexo的基本操作</td></tr></table>
1.安装nodejs
<https://nodejs.org/en/download/>
此处会自动将npm一起安装

2.安装npm-Hexo 

``` 
npm install -g hexo-cli 
```

3.安装git [git链接](https://git-scm.com/download/win)(github创建账号创建新的库省略)

**配置密钥**<font color = red>(意思是当你每次从本地上传东西时不用再输入一遍账号密码)

<font color = blue>右键git bash输入 </font> 

```
        git config --global user.name "你的GitHub用户名" 
        git config --global user.email "你的GitHub注册邮箱"
```

<font color = blue>生成ssh密钥文件</font> 
```
ssh-keygen -t rsa -C "你的GitHub注册邮箱"
```

然后直接三个回车即可，默认不需要设置密码  
然后找到生成的.ssh的文件夹中的id_rsa.pub密钥，将内容全部复制  
<font color = red>地址理论上在c-用户-username-.ssh-id_rsa.pub里</font>  
打开GitHub_Settings_keys 页面，新建new SSH Key<https://github.com/settings/keys>  
可用
 ```
ssh git@github.com 
```
自行检验是否连接成功  

--------------------------------------
# 1. Hexo 多台电脑同步问题
 
**主要使用分支合并方法**

**准备b.对username.github.io仓库新建分支，并克隆**
(1)在Github的username.github.io仓库上新建一个xxx分支  
(2)该仓库->Settings->Branches->Default branch中将默认分支设为xxx，update保存；  
(3)将该仓库克隆到本地，进入该username.github.io文件目录  

--------------------------------------------
**c.多边电脑均为 先将文件拷贝到本地仓库**
<font color = blue>用克隆或本地从其它地方拷都可以 </font> 
```
git clone git@github.com:xxx/xxx.github.io.git(替换成你的仓库)
```
**<font color = red>现在所有操作都在仓库文件夹里完成</font>**
- 先初始化
```
hexo init blog
hexo new test_my_site
hexo g 
hexo s #(可本地点击链接打开)
```

######新创建的跳过这一步##########
仅在本地io文件夹里有东西时使用
- 把本地除了.git 的都删掉  
    - 如果删不掉无权限 就先去post文件夹把.md都删掉  
    - 然后把根目录.deploy_git删掉
- 把博客里其它所有复制过来，除了 *deploy_git*
###############################

- <font color = red>改yml 中内容(翻到最后修改)</font>
<font color = blue>
```deploy:
type: git
repo: 这里填入你之前在GitHub上创建仓库的完整路径，记得加上 .git
branch: master
```</font>
参考如下：
分支名为你刚才新创的名字

- 装连接git插件
```
npm install hexo-deployer-git --save
```

 **<font color = red>现在每台电脑操作就完成了</font>**

------------------------------------------------
<font color = red>

**写完文件的同步问题**

执行git pull 同步 可本地覆盖

如果遇到问题
```
git reset --hard
git pull
```

**上传新文件到github**
```
git add .
git commit -m "一定要随便写个参数"
git push
```

**hexo同步更改**
```
hexo g -d
```</font>







