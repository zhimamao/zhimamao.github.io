---
title: Hexo+git 在线-本地 图床配置
date: 2022-08-14 0:11:45
categories : 
- hexo
tags: 
- hexo

---
喵
![miao1](./hexo%2Bgittuchuang/tuchuang.jpg)

-----------------------------------
# 图床是什么
- 放图片的地方
- 因为本地文件可能遗失，保存一份在github里
- 没什么用
-----------------------------------
# 工具
PicGo[地址](https://github.com/Molunerfinn/PicGo/releases)

------------------------------------
1. 创建Github 新仓库
    - 创建好后，需要在 GitHub 上生成一个 token 以便 PicGo 来操作我们的仓库，来到个人中心（点击网页右上角的个人头像，选 Settings ），选择 Developer settings 就能看到 Personal access tokens，选择此 tab ，我们在这里创建需要的 token
    - 点击 Generate new token 创建一个新 token，选择 repo，同时它会把包含其中的都会勾选上，我们勾选这些就可以了。然后拉到最下方点击绿色按钮，Generate token 即可。之后就会生成一个 token ，记得复制保存到便签，这个 token 只显示一次
2. PicGo配置
    - 在github图床里填写
    - 设置token
    - 路径可不填
    - 调整默认仓库为github
    - 上传直接拖拽就好了
3. 图片引用格式
    ```
    ![miaomiao](http...)
    或 本地
    ![miaomiao](./wenjianming.png)
    ```