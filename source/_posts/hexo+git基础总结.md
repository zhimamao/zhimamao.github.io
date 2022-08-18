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



<table><tr><td bgcolor=white>
本文主要适用于要在两台以上电脑设备使用一个github账号编辑同一个Hexo博客的同步和配置基础
</td></tr></table>

-----------------------------------
# 目录
1. [每台电脑都要执行的准备操作](#1)
2. [第一台电脑的初始创建工作](#2)
3. [其它电脑的同步操作](#3)
4. [Hexo 的基本用法和其中遇到的问题](#4)

-------------------------------------
<div id="1"></div>
<table><tr><td bgcolor=yellow>每台电脑都要执行的基本操作</td></tr></table>

* 准备a.新建一个文件夹 比如blog**

1.安装nodejs
<https://nodejs.org/en/download/>
此处会自动将npm一起安装

2.安装git [git链接](https://git-scm.com/download/win)(github创建账号创建新的库省略)

3.安装npm-Hexo 

``` 
npm install -g hexo-cli 
```



**配置密钥**<font color = red>(意思是当你每次从本地上传东西时不用再输入一遍账号密码)</font>

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

<div id="2"></div>

* <table><tr><td bgcolor=yellow>仅在第一台需要创建初始博客的电脑进行一下操作</td></tr></table>

---------------------------------

## a.先创建一个新的仓库 

**名称 username.github.io**

注意 <font color = red>新建的仓库名字一定要和你的用户名相同</font>  



----------------------------------

## b.在Github的username.github.io仓库上新建一个xxx(比如main)分支  

-------------------------------------------

## c.该仓库->Settings->Branches->Default branch中将默认分支设为xxx，update保存；  

-------------------------------------------------

## d.将该仓库克隆到本地(上面创建的blog文件夹里)

  ```
   git clone git@github.com:xxx/xxx.github.io (替换成你的仓库)
  ```

--------------------------------------------

## e.进入xxx.github.io 文件夹

# **<font color = red>现在所有操作都在仓库文件夹里完成</font>**

**首先检查文件夹是否里面有且只有.git**

---------------------------------------------------

## 初始化博客文件
```
hexo init blog
hexo new test_my_site
hexo g 
hexo s #(可本地点击链接打开)
```
如果有出现local---4000 网站 则成功

--------------------------------------------------
## hexo 博客连接git的基本设置
1.  <font color = red>改yml 中内容(翻到最后修改)</font>


```deploy:
type: git
repo: 这里填入你之前在GitHub上创建仓库的完整路径，记得加上 .git
branch: main
```

注意:

    a. 分支名为你刚才新创的名字
    b. repo中为 git@github.com:xxx/xxx.github.io.git


2. 装连接git插件
```
npm install hexo-deployer-git --save
```

现在第一台电脑配置完成

---------------------------------------------------

<div id="3"></div>

## <table><tr><td bgcolor=yellow>下面是第二台电脑的配置</td></tr></table>

1. 新建blog 本地文件夹

2. 执行上面的三个程序安装 :git(和密钥配置)， nodejs，hexo
* 注意检查是否均为最新版本 

3. clone 到本地
```
git clone git@github.com:xxx/xxx.github.io.git
```


4. 装连接git插件
```
npm install hexo-deployer-git --save
```

5. 同步
```
git pull
```

 **<font color = red>现在每台电脑操作就完成了</font>**

------------------------------------------------
<div id="4"></div>

1. 如果你在拷贝文件到第二台电脑时不时用的clone而是直接硬盘拷贝的
需要
- 把本地除了.git 的都删掉  
    - 如果删不掉无权限 就先去post文件夹把.md都删掉  
    - 然后把根目录.deploy_git删掉
- 把博客里其它所有复制过来，除了 *deploy_git*


**写完文件的同步问题**

2. 每次在开始之前工作/写文章之前 都必须执行执行git pull 同步 

如果遇到问题
```
git reset --hard
git pull
```

3. **上传新文件到github**
```
git add .
git commit -m "一定要随便写个参数"
git push
```

4. **hexo同步更改**
```
hexo clan
hexo g -d
```

5.hexo 本地预览
```
hexo s
```

6.hexo 新建文章
```
hexo n xxx(文章名)
```

地址在scoure-post 下






