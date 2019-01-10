### Quick Start
## 功能如下：
1）登录微信，可以获取聊天记录，判断设定的人物如果被@。则调用机器人ownthink进行对话
2）在聊天记录中如果有人上传图片或者音频，可以对这些信息进行处理或者将这些信息保存在磁盘。


##

### Quick Start
 >  适用于Mac系统
### 步骤一： 本地mysql安装（本项目使用 mysql 5.7版本）
#### 1. 本地Mysql ROOT用户密码免登录
  > mysql安装 下载地址: [点击跳转页面](https://dev.mysql.com/downloads/file/?id=481129)     
  > 使用root权限登录本地mysql（无密码登录步骤）
  > 1. 停止启动的mysql  Mac系统下在系统 偏好设置 下    
    ```
    'System Prefrences' > MySQL > 'Stop MySQL Server’
    ```
  > 2. 以安全命令的模式启动 Mysql，终端执行以下命令:   
    ```
    sudo /usr/local/mysql/bin/mysqld_safe --skip-grant-tables3
    ```
  > 3. 打开新的终端页面，以root权限身份登录Mysql，进入mysql客户端命令行:   
    ```
    sudo /usr/local/mysql/bin/mysql -u root -p   
    ```
  > 4. 设置root密码    
    ```
    update mysql.user set authentication_string=password('root') where user='root';
    ```
  > 5. 刷新权限    
    ```
    FLUSH PRIVILEGES;
    ```
    
#### 2. Mysql配置
  > 1. 确定my.cnf文件位置    
    ```
    sudo find / -name my.cnf
    ```
  > 2. 修改配置文件，并重新启动 Mysql     
        [client]
        port = 3306     
        socket = /tmp/mysql.sock    
        default-character-set = utf8   
        [mysqld]
        # Only allow connections from localhos   
        collation-server = utf8_unicode_ci   
        character-set-server = utf8   
        init-connect ='SET NAMES utf8'   
        max_allowed_packet = 64M   
        bind-address = 127.0.0.1   
        port = 3306
        socket = /tmp/mysql.sock  
        innodb_file_per_table=1    
        [mysqld_safe]
        timezone = '+0:00'  
       
    
#### 3. 增加本项目 数据库、用户
  > 1. 登录Mysql客户端控制台:     
    ```
    mysql -u root -p
    ```
  > 2. 进入登录Mysql客户端控制台，使用mysql数据库     
    ```
    use mysql;
    ```
  > 3. 创建数据库    
    ```
    CREATE DATABASE wechat_robot;
    ```
  > 3. 添加用户并设置该数据库(wechat_robot)权限  
    ```
    GRANT SELECT,INSERT,UPDATE,DELETE,CREATE,DROP ON wechat_robot.* TO 'wechat_robot'@'localhost' IDENTIFIED BY 'wechat_robot';
    ```
  > 4. 刷新权限   
    ```
    FLUSH PRIVILEGES; 
    ```
  > 5. 退出    
    ```
    Enter: \q
    ```

#### 4. 使用Mysql客户端连接数据库
  > 1. Navicat 下载
  > 2. 本地用户使用 wechat_robot 用户连接 密码为 wechat_robot



### 步骤二：python环境配置
  本项目使用python3.6版本
#### 1. python环境配置
  > 1. 
  
  
 1. python -m venv env       
 2. source env/bin/activate      
 3. pip install -r requirements.txt
 4. python savemsg.py



#### 本地启动# wechat_bot
