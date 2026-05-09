# 🚀 STUnet Connect · 汕头大学校园网自动认证助手---Windows[![Windows](https://img.shields.io/badge/Windows-0078D4?style=flat&logo=windows&logoColor=white)](https://github.com/xuzhihaoup/STUnet_connect)

> 🖥️ 面向远程办公、挂后台实验、校外实习的你，一键连接校园网，从此告别“远程掉线恐惧症”。  
**💡求点亮Star☆-您的鼓励是我最大的支持-在读期间我将持续维护💡**[![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=flat&logo=ubuntu&logoColor=white)](https://github.com/xuzhihaoup/STUnet_connect/blob/main/STUnet_connect_Linux)
![Stars](https://img.shields.io/github/stars/xuzhihaoup/STUnet_connect)

## ✨ 项目亮点

- ✅ **自动定时认证**：支持通过任务计划程序自动登录，确保校园网随时在线。
- 🛠️ **手动控制中心**：便捷命令界面，支持手动登录、远程切换账号、注销等多种操作。
- 🔐 **本地数据存储**：账户信息与 cookies 全部保存在本地，确保你的隐私与安全。
- 🧠 **轻量免安装**：无需管理员权限，开箱即用，适合放在远程电脑开机即连。  
- 🦄  **支持多系统**： 本工具提供Windows和Linux两个版本选择。   
---

## 📦 软件介绍

### 🖱️ `hand_connect.exe` · 手动模式

交互式操作界面，支持以下功能：  
ヽ(•‿•)ノ 汕头大学校园网自动连接助手ヽ(•‿•)ノ  
请选择操作：

0. 自动化登录  
1. 手动登录  
2. 切换账号  
3. 注销登录  
4. 当前账户信息  
5. 退出系统  

📝 初次使用需输入校园网账户信息，程序将自动生成 `cookies` 与配置文件`json`并存于当前目录。此后登录可一键完成，无需打开浏览器。

💡 提示：若当前账号流量不足，**避免远程控制中断**，可在本工具中快速切换账号并手动登录。

---

### 🤖 `auto_connect.exe` · 自动模式

专为无人值守的远程电脑设计：  

#### *Step*-1. 
**首次运行**时需手动输入账号信息，或复制 `hand_connect.exe` 目录下运行生成的账户配置文件( `cookies.pkl` 与`credentials.json`)。   

💡 **提示**：请务必确保`auto_connect.exe` || `cookies.pkl` || `credentials.json`这三个文件在一个目录下。  
![任务计划程序](https://github.com/xuzhihaoup/STUnet_connect/blob/main/image/文件目录.png)  

#### *Step*-2. 
配合 Windows **任务计划程序** 设置自动登录时间（如：每天凌晨 4 点），也可设置每小时重复认证(有远程需求时推荐使用，非远程仅需设置每天认证时间6，7，8.30，12这几个时间段基本可以满足需求)，**防止因校园网强制下线而断网**。创建任务时请确保**Step 1**图片中显示的文件结构。

![任务计划程序](https://github.com/xuzhihaoup/STUnet_connect/blob/main/image/step2.png)
![自动值守](https://github.com/xuzhihaoup/STUnet_connect/blob/main/image/自动任务.png)  
![配置](https://github.com/xuzhihaoup/STUnet_connect/blob/main/image/任务计划配置.png)    
配置任务时，这里勾选如果你不知道怎么勾选，推荐这样勾选。    
---
#### *Step*-3. 
**测试是否部署成功** 请使用hand_connect.exe程序 --> 1. 手动登录 --> 3. 注销登录 --> 打开浏览器随便打开一个网页检查是否网络已经无法使用 若无法使用则成功注销反之继续注销 --> 使用刚刚部署在**任务计划程序**中的任务右键选择运行 -->  打开浏览器随便打开一个网页检查网络能够正常使用则部署成功
## 🧩 使用建议

- **hand_connect**该软件可以创建快捷方式放置在桌面，替代之前使用校园网要去浏览器的环节，该软件可以作为远程时切换账户使用，切勿使用浏览器切换账号，会使远程断联。  
- **auto_connect**该软件并搭配定时任务，确保远程稳定在线。同时省去每天认证校园网的麻烦。  
- 所有配置文件保存在本地，**无需同步或上传**，他人无需使用你的 cookies 文件。  
- 当 `hand_connect.exe` 提示cookies无效或者过期，用户无需担心，重新登录时会自动更新。  
- `credentials.json`与`cookies.pkl`请保持与exe文件(`hand_connect.exe`/`auto_connect.exe`)在同一文件夹目录下。  
- 该项目仅作为省去需要人为每天去浏览器认证的过程，以及远程时无人认证的困扰。并不是校园网VPN。需要电脑放置在学校。  
- 当软件运行闪退时，请检查是否连接STU校园网。
- 如果使用目的是远程连接，建议多配置几个远程软件在后台，向日葵、Todesk等(防止某个远程软件退出，我的远程方案是Todesk(专业版)+向日葵。
- 记得给校园网订购套餐，不订购每天只有20M。如果忘记订购远程断开连接也不用担心，校园网00：00-04：00(大概时间段)免费使用，可以选择这个时间段进去订购校园网套餐。如果有较大文件下载也建议半夜下载。

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
| hand_connect.exe    | 手动模式主程序               |
| auto_connect.exe    | 自动模式主程序               |
| credentials.json    | 账户信息（登录自动生成）     |
| cookies.pkl         | 账户信息（登录自动生成）     |
| main.py             | `hand_connect.exe` 源代码    |
| auto_connect.py     | `auto_connect.exe` 源代码    |
| README.md           | 项目说明文档                 |

