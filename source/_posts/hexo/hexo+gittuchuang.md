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
```
附
资源文件夹
资源（Asset）代表 source 文件夹中除了文章以外的所有文件，例如图片、CSS、JS 文件等。比方说，如果你的Hexo项目中只有少量图片，那最简单的方法就是将它们放在 source/images 文件夹中。然后通过类似于 ![](/images/image.jpg) 的方法访问它们。

对于那些想要更有规律地提供图片和其他资源以及想要将他们的资源分布在各个文章上的人来说，Hexo也提供了更组织化的方式来管理资源。这个稍微有些复杂但是管理资源非常方便的功能可以通过将 config.yml 文件中的 post_asset_folder 选项设为 true 来打开。

_config.yml
post_asset_folder: true
当资源文件管理功能打开后，Hexo将会在你每一次通过 hexo new [layout] <title> 命令创建新文章时自动创建一个文件夹。这个资源文件夹将会有与这个文章文件一样的名字。将所有与你的文章有关的资源放在这个关联文件夹中之后，你可以通过相对路径来引用它们，这样你就得到了一个更简单而且方便得多的工作流。
```