---
title: “hexo+live2d模型”
date: 2022-08-15 10:30:49
categories : 
- hexo
aplayer: true


---
![miao](./%E2%80%9Chexo-live2d%E6%A8%A1%E5%9E%8B%E2%80%9D/a.jpg)
# 安装
```
npm install --save hexo-helper-live2d

```

## 从官方下载一个模型包
```
npm install live2d-widget-model-hijiki
```
（是一只小黑猫）

## 或者自己在网上找一个

 在根目录-node_modules 下创建你包的名字如live2d-widget-model-cat文件夹

 然后文件夹内新建assets用来放你下载的模型

 （暂没尝试需要对下载的模型进行什么更改）

 然后需要在npm注册一个账号将你的新文件发布（npm publisch)


 ## 配置
 在根目录的  _config.yml  文件中
```
 live2d:
  enable: true
  scriptFrom: local
  pluginRootPath: live2dw/
  pluginJsPath: lib/
  pluginModelPath: assets/
  tagMode: false
  debug: false
  model:
    use: live2d-widget-model-hijiki（你的包名）
  display:
    position: right
    width: 150
    height: 300
  mobile:
    show: true
```

**完成**


--------------------------------------------------------



{% aplayer "Caffeine" "Jeff Williams" "caffeine.mp3" "picture.jpg" "lrc:caffeine.txt" %}


{% aplayer title author url [picture_url, narrow, autoplay, width:xxx, lrc:xxx] %}







