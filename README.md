# AutoProxy
IP代理池服务, 获取daili666/快代理(都是收费)提供的代理IP并验证可用性后以接口/代理方式提供服务。
从免费网站爬代理的方式效率太低，本项目不涉及。

## 环境依赖
1. python库: termcolor、web.py、requests
2. 可选进程管理工具pm2

## 文件说明

1. rest_server.py 提供restful接口服务，可通过接口获取可用的代理
2. alive_checker.py 检查代理的存活性，应该加入到crontab中
3. proxy_server.py 代理服务器

## 部署说明
1. 添加crontab: ` */2 * * * * python check_alive.py `
2. 运行接口服务：`python rest_server.py`, 默认端口80
3. 运行代理服务：`python proxy_server.py`，默认端口

## 配置说明
内置了两个网站的代理IP服务, 需要配置购买订单号，选择默认使用的服务商
部署代理服务需要启动一个本地代理，8080，当代理服务器无法连接的时候就使用本地网络直接访问

