# 🚀 STUnet Connect · 汕头大学校园网自动认证助手---Linux[![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=flat&logo=ubuntu&logoColor=white)](https://github.com/xuzhihaoup/STUnet_connect/blob/main/STUnet_connect_Linux)

> 🖥️ 面向远程办公、挂后台实验、校外实习的你，一键连接校园网，从此告别“远程掉线恐惧症”。  
**💡求点亮Star☆-您的鼓励是我最大的支持-在读期间我将持续维护💡** [![Windows](https://github.com/xuzhihaoup/STUnet_connect)](https://img.shields.io/badge/Windows-0078D4?style=flat&logo=windows&logoColor=white)
视频配置教程[![Bilibili](https://img.shields.io/badge/Bilibili-E95420?style=flat&logo=bilibili&logoColor=white)](https://www.bilibili.com/video/BV1EwhvzoEis/?vd_source=14c6392964a3f4218c6147d1ed82bcbc)
## ✨ 项目亮点

- ✅ **自动定时认证**：支持通过任务计划程序自动登录，确保校园网随时在线。
- 🛠️ **手动控制中心**：便捷命令界面，支持手动登录、切换账号、注销等多种操作。
- 🔐 **本地数据存储**：账户信息与 cookies 全部保存在本地，确保你的隐私与安全。
- 🧠 **轻量免安装**：无需管理员权限，开箱即用，适合放在远程电脑开机即连。
---

## 📦 软件介绍

### 🖱️ `hand_connect.sh` · 手动模式
#### *Step*-1.   
将**hand.connect.sh**与下载的**main.py**文件放置在同一文件夹  
#### *Step*-2.  **（可选）**
如提示权限不足，添加权限  
```bash
$ chmod +x hand.connect.sh
```
![运行界面](https://github.com/xuzhihaoup/STUnet_connect/blob/main/STUnet_connect_Linux/fig_linux_1.png) 


📝 初次使用请选择 **[1]** 需输入校园网账户信息，程序将自动生成 `cookies` 与配置文件（JSON）并存于当前目录。此后登录可一键完成，无需打开浏览器。部分浏览器无法返回账户剩余流量信息  

💡 提示：若当前账号流量不足，**避免远程控制中断**，可在本工具中快速切换账号并手动登录。

---

### 🤖 `auto_connect.sh` · 自动模式

专为无人值守的远程电脑设计：  

#### *Step*-1. 
**首次运行**时需手动输入账号信息，或复制 `hand_connect.sh` 目录下运行生成的账户配置文件( `cookies.pkl` 与'credentials.json')。   

💡 **提示**：请务必确保 **auto_connect.sh||cookies.pkl||credentials.json||auto_connect.py** 这四个文件在一个目录下。  
![文件结构](https://github.com/xuzhihaoup/STUnet_connect/blob/main/STUnet_connect_Linux/fig_linux_2.png)  
🚨 **重点**：请务必确保 **auto_connect.sh文件中红框的路径修改为你自己文件下载的路径**  
![路径修改](https://github.com/xuzhihaoup/STUnet_connect/blob/main/STUnet_connect_Linux/fig_linux_5.png)  
#### *Step*-2. 
配合 linux **Cron** 设置自动登录时间（如：每天凌晨 4 点），也可设置每小时重复认证(有远程需求时推荐使用，非远程仅省去每天认证流程设置6，7，8.30，12这几个时间段基本可以满足需求)，**防止因校园网强制下线而断网**。创建任务时请确保**Step 1**图片中显示的文件结构。
打开终端  
```bash
$ cd #你的auto_connect.sh所在文件夹 如下图示意
$ crontab -e #进入编辑模式 输入完成后 请ctrl+o保存后在ctrl+x退出
按照下列格式输入你的文件路径注意是绝对路径
30 6 * * * /home/zhxu/STUnet_connect-main/auto_connect.sh  #表示每天的6：30分自动执行
30 7 * * * /home/zhxu/STUnet_connect-main/auto_connect.sh
30 8 * * * /home/zhxu/STUnet_connect-main/auto_connect.sh
0 12 * * * /home/zhxu/STUnet_connect-main/auto_connect.sh
命令解释
* * * * *  command_to_run
- - - - -
| | | | |
| | | | +--- 星期几 (0 - 7) (0和7代表星期天)
| | | +----- 月份 (1 - 12)
| | +------- 日期 (1 - 31)
| +--------- 小时 (0 - 23)
+----------- 分钟 (0 - 59)
```
![终端](https://github.com/xuzhihaoup/STUnet_connect/blob/main/STUnet_connect_Linux/fig_linux_3.png)  
![cron配置](https://github.com/xuzhihaoup/STUnet_connect/blob/main/STUnet_connect_Linux/fig_linux_4.png) 
---
#### *Step*-3. 
**测试是否部署成功** 请使用hand_connect.sh脚本 --> 1. 手动登录 --> 3. 注销登录 --> 打开浏览器随便打开一个网页检查是否网络已经无法使用 若无法使用则成功注销反之继续注销 --> 在 **crontab -e** 里面添加每分钟执行一次  
```
* * * * * /home/zhxu/STUnet_connect-main/auto_connect.sh  
```
-->  等待1分钟，打开浏览器随便打开一个网页检查网络能够正常使用则部署成功
##### 一些其他命令
``` bash
$ crontab -l #打印配置的全部任务
$ tail -f /var/log/syslog #打印cron运行日志
```
## 🧩 使用建议

- **hand_connect**该脚本可以替代之前使用校园网要去浏览器的环节，更重要的是该软件可以作为远程时切换账户使用，切勿使用浏览器切换账号，会使远程断联。  
- **auto_connect**该脚本并搭配定时任务，确保远程稳定在线。同时省去每天认证校园网的麻烦。  
- 所有配置文件保存在本地，**无需同步或上传**，他人无需使用你的 cookies 文件。  
- 当 `hand_connect.exe` 提示cookies无效或者过期，用户无需担心，重新登录时会自动更新。  
- 'credentials.json'与'cookies.pkl'请保持与exe文件(hand_connect.sh/auto_connect.sh)在同一文件夹目录下。  
- 该项目仅作为省去需要人为每天去浏览器认证的过程，以及远程时无人认证的困扰。并不是校园网VPN。需要电脑放置在学校。  
- 当软件运行闪退时，请检查是否连接STU校园网。
- 如果使用目的是远程连接，建议多配置几个远程软件在后台，向日葵、Todesk等(防止某个远程软件退出，我的远程方案是Todesk(专业版)+向日葵。  

---

## 💬 特别声明

本工具为学习与交流目的开发，**不涉及任何破解或绕过认证行为**。  
源代码完全开源，欢迎同学们魔改、复刻、再创作！

> 🧑‍💻 By 汕头大学 2024级 工学院 zhx  
> 📧   软件相关问题可致Outlook联系我24zhxu  

---

## 📁 项目结构
| 文件名              | 说明                        |
|---------------------|------------------------------|
| credentials.json    | 账户信息（登录自动生成）     |
| cookies.pkl         | 账户信息（登录自动生成）     |
| main.py             | `hand_connect` 源代码    |
| auto_connect.py     | `auto_connect` 源代码    |
| auto_connect.sh     | Linux运行脚本     |
| hand_connect.sh     | Linux运行脚本    |
| README.md           | 项目说明文档                 |

