---
type: Linux
archive: false
---
## Apache2, MariaDB, PHP

---

### Apache2

```Bash
# Ubuntu 22.04
sudo apt update
sudo apt upgrade
sudo apt install apache2

sudo systemctl status apache2

sudo systemctl enable apache2
sudo systemctl disable apache2
```

  

### MariaDB

```Bash
# Ubuntu 22.04
sudo apt update
sudo apt upgrade

sudo apt install mariadb-server mariadb-client -y

sudo systemctl status mariadb
sudo systemctl start mariadb
sudo systemctl stop mariadb
sudo systemctl restart mariadb

# 시스템 시작 시 MariaDB 활성화
sudo systemctl enable mariadb
sudo systemctl disable mariadb
```

  

### PHP

```Bash
# Ubuntu 22.04
sudo apt update && sudo apt upgrade -y

sudo apt install software-properties-common apt-transport-https -y
sudo add-apt-repository ppa:ondrej/php -y

sudo apt update && sudo apt upgrade -y


sudo apt install php7.4 php7.4-common php7.4-cli

# Apache 모듈로 설치 시 다음 명령어 실행
sudo apt install libapache2-mod-php7.4
sudo systemctl restart apache2
```

  

### Apache2 Service 등록

```Bash
# service 파일 생성
vim /etc/systemd/system/apache2.service
```

```Plain
[Unit]
Description=The Apache HTTP Server

[Install]
WantedBy=multi-user.target

[Service]
Type=forking
\#EnvironmentFile=/usr/local/apache2/bin/envvars
PIDFile=/usr/local/apache/logs/httpd.pid
ExecStart=/usr/local/apache/bin/apachectl start
ExecReload=/usr/local/apache/bin/apachectl graceful
ExecStop=/usr/local/apache/bin/apachectl stop
KillSignal=SIGCONT
PrivateTmp=true
```

  

### MariaDB Service 등록

```Bash
# service 파일 생성
vim /etc/systemd/system/mariadb.service
```

```Plain
[Unit]
Description=MariaDB 10.6.7 database server
After=network.target
After=syslog.target

[Install]
WantedBy=multi-user.target
Alias=mariadbd.service

[Service]
User=maria
Group=maria

# Execute pre and post scripts as root
PermissionStartOnly=true

# Needed to create system tables etc.
\#ExecStartPre=

# Start main service
ExecStart=/usr/local/src/mariadb-10.6.7-linux-systemd-x86_64/bin/mariadb-safe

# Don't signal startup success before a ping works
\#ExecStartPost=

# Give up if ping don't get an answer
TimeoutSec=300
PrivateTmp=false
```

  

### Systemctl daemon 재시작

```Bash
sudo systemctl daemon-reload
```