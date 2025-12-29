---
title: Pyspider ARM64(AARCH64)安装教程
---

<div align="center">

***注意：此教程仅通用于Ubuntu_22.04.3_Server_Arm64，树莓派(Raspberry Pi OS)原系统可能并不适用此教程***

</div>

### 准备
- 硬件：SD卡读卡器、手、脑子(非常重要)
- 软件：BalenaEtcher(可用树莓派官方标准写入工具代替，个人认为BalenaEtcher更好用)、SSH工具(Xshell、MobaXterm或其他，个人比较爱用MobaXterm)、浏览器(Chrome、Edge等都行)
### 开始
- 笔者打包好的镜像文件[Ubuntu Server 22.04.3](https://www.123pan.com/s/LuI9-vKGsH.html)(此版本仅适用于SD卡大小为32GB或者更大容量的版本！)
```提取码
4cqW
```
```注意
此版本为Ubuntu_22.04.3_Server_Arm64，
已集成:
Conda(miniforge3)、
Python3.6(虚拟环境内)、
Pyspider(虚拟环境内)、
Phantomjs(虚拟环境内，版本aarch64 2.1.1)
此版本帐号为ubuntu，密码(ubuntu/root密码)：0000
这个可用于SSH或者正式登陆的帐号密码
Linux权限非常分明，如不知或不清楚可自行百度或请教老师、同学
此版本仅适用于SD卡大小为32GB或者更大容量的版本！
```
### 安装系统
- 下载镜像文件(如果这个项目仍是树莓派4B来跑的话)，镜像架构：Arm64 Ubuntu镜像下载地址[Download | Ubuntu](https://ubuntu.com/download)里面可自行寻找需要的系统
- 打开BalenaEtcher进行刷写系统，如有不知怎么用的可百度解决。
- SSH远程连接，如果为Ubuntu Server，那么账号为ubuntu，密码为ubuntu，如果下载的是我的系统，那么账号为ubuntu，密码为0000，原版的Ubuntu Server第一次安装开机之后会让你重设密码，打密码的时候没有显示，不用担心，重设密码之后重新连接即可。
### 安装相应软件
- 安装相应软件
  ```更新命令
  sudo apt update && sudo apt upgrade -y
  ```
如果更新过慢可自行换源，我的系统本身为清华源，拥有不错的下载更新速度
### 安装依赖软件
- 安装依赖软件
  ```命令
  sudo apt install wget gcc libssl-dev bzip2 curl make -y
  ```
  如果更新过慢可自行换源，我的系统本身为清华源，拥有不错的下载更新速度
- 获取你当前树莓派的IP
  ```终端键入
  ip a
  ```
  记住这个IP，后面会用到
### 安装Conda虚拟化工具
- 你当然可以选择安装[Anaconda](https://www.anaconda.com/download/)，但是那将面临大量的资源重构 (这个东西可没有arm架构的东西) ，如果你有实力可以试着更改一下，当然也可以使用[miniconda](https://docs.anaconda.com/free/miniconda/index.html)，这个东西已经八百年不更新了，如果想用这个那么就可能意味着要自己编译资源，所以我推荐使用[miniforge3](https://github.com/conda-forge/miniforge)，这个东西本身就是为aarch64编译的conda虚拟环境，理论使用方法通用于[Anaconda](https://www.anaconda.com/download/)，但是可能存在依赖或者其他的问题，但是对于PySpider已经够用，下载地址:Miniforge3-23.10.0-0-Linux-aarch64.sh(速度可能有些慢，毕竟来自GitHub，可适当开启加速器加速)
```终端键入
curl -o Miniforge3-23.10.0-0-Linux-aarch64.sh https://ghproxy.net/https:/github.com/conda-forge/miniforge/releases/download/23.10.0-0/Miniforge3-23.10.0-0-Linux-aarch64.sh && sudo chmod 777 Miniforge3-23.10.0-0-Linux-aarch64.sh && bash Miniforge3-23.10.0-0-Linux-aarch64.sh
```
按照提示完成应有的操作。
### 更改Conda虚拟化工具的源(避免下载速度过慢)
- 1.查看下载源地址
  ```终端键入
  conda config --show-sources
  ```
  查看域名是哪个(因为我改完了，而且改的时候忘记截图了，所以没有图)
- 2.更改下载源地址
  ```终端键入
  conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free
  ```
  ```终端键入
  conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
  ```
  ```设置搜索时显示通道地址(终端键入)
  conda config --set show_channel_urls yes
  ```
  查看是否设置成功
  ```终端键入
  conda config --show-sources
  ```
- 换回默认源：
  ```终端键入
  conda config --remove-key channels
  ```
### 创建Python虚拟环境
##### conda创建环境使用方法：conda create -n env_name python=xxx
- 1.创建Python虚拟环境
  ```终端键入
  conda create -n pyspider python=3.6.7
  ```
  接下来按照要求输入“y”
- 2.进入Python虚拟环境(方法为：source activate your_env_name)
  ```终端键入
  conda activate pyspider
  ```
- 3.退出Python虚拟环境(方法为：source deactivate)
  ```终端键入
  conda deactivate
  ```
### 安装Python包(Pyspider & PhantomJS)
- 1.给PIP换源
  检查当前混啊经是否存在pip，如果不存在，则需要安装pip
  ```安装pip，终端键入
  conda install pip
  ```
  换源(中科大的源，不知道为啥，在写这篇教程的时候清华源老是抽风)
  ```终端键入
  pip config set global.index-url https://pypi.mirrors.ustc.edu.cn/simple
  ```
- 2.安装Python包(Pyspider)
  现在我们就可以正式的安装Pyspider了
  ```终端键入
  pip install pyspider
  ```
  如果有要求就可以按照那个要求来继续安装(一般来说不需要)
- 3.安装PhantomJS 2.1.1 for arm64
  本身的PhantomJS并没有相应版本的PhantomJS，所以我们需要安装自编译的版本，正好有人维护这个东西，[PhantomJS 2.1.1 for arm64](https://github.com/fg2it/phantomjs-on-raspberry/releases)
  ```终端键入
  wget https://github.com/fg2it/phantomjs-on-raspberry/releases/download/v2.1.1-jessie-stretch-arm64/phantomjs 
  ```
  ```终端键入
  sudo mv phantomjs /usr/local/bin/ && sudo chmod +x phantomjs
  ```
### 安装Mysql服务器以及创建相应的数据库和链接数据库
##### 哎~，没想到吧，这鬼东西连接数据库呢吧 (^▽^ ),我也不想写了，给你几个参考链接，大差不差
- 1.[安装数据库](https://blog.csdn.net/qq_18301257/article/details/112209931)
- 2.[pyspider使用mysql作为任务数据库](https://blog.csdn.net/paulluo0739/article/details/94446234)
##### 声明：数据库的安装是可以不和树莓派放一块的，而且这东西可以连接同一个数据库，所以你也可以把数据库放在其他电脑上，这个数据库的架构没要求，Arm也好PC也好或者是其他的什么也好都一样，然后通过网络连接即可

### 正式启动Pyspider
- 1.进入虚拟环境
  ```终端键入
  source activate pyspider
  ```
- 2.启动Pyspider
  ```终端键入
  pyspider -c 路径+你的配置文件.json all
  ```
- 3.默认这个端口为5000，那么访问地址就是ip:5000
- 4.进入Pyspider
  浏览器输入ip:5000并回车，一般来说就可以进入了
  如果进不去或者拒绝连接请检查防火墙是否开启，如果开启请全部关闭，然后重新连接尝试。
### 编写爬虫脚本
  这个东西就要看你们自己的了，说实话，我写的东西也不咋地，建议百度！好了，教程就到这里就结束了，剩下的请自行摸索吧，有问题可以评论区找我。