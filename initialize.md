# essential packages

## ubuntu

> one of best options for usual server installation is **ubuntu server** os!

```shell
sudo nano /etc/netplan/50-cloud-init.yaml
```

```shell
network:
    ethernets:
        enp0s3:
            dhcp-identifier: mac
            dhcp4: true
            optional: true
    version: 2
```

```shell
sudo systemctl restart systemd-networkd
```

```shell
sudo apt update
sudp apt upgrade
```

```shell
sudo apt install nano vim
sudo apt install inetutils-ping
```

```shell
sudo apt install network-manager
```

```shell
sudo apt install isc-dhcp-client
```

```shell
sudo apt install firewalld
```

```shell
sudo apt install net-tools
```

```shell
sudo apt install openssh-server
sudo systemctl enable ssh
sudo systemctl start ssh
```

```shell
sudo visudo
```

```shell
Defaults        timestamp_timeout=240 # in minutes (4 hours)
```

## centos

> for minimal installation, install the server mode **at least**

```shell
ls /etc/sysconfig/network-scripts/ifcfg-*
nano /etc/sysconfig/network-scripts/ifcfg-enp0s3
```

```shell
BOOTPROTO=dhcp
ONBOOT=yes
```

```shell
ping 8.8.8.8
```

```shell
systemctl restart network
```

```shell
sudo nano /etc/yum.repos.d/CentOS-Base.repo
```

```shell
[base]
name=CentOS-$releasever - Base
baseurl=http://vault.centos.org/7.9.2009/os/$basearch/
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7

[updates]
name=CentOS-$releasever - Updates
baseurl=http://vault.centos.org/7.9.2009/updates/$basearch/
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7

[extras]
name=CentOS-$releasever - Extras
baseurl=http://vault.centos.org/7.9.2009/extras/$basearch/
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7

[centosplus]
name=CentOS-$releasever - Plus
baseurl=http://vault.centos.org/7.9.2009/centosplus/$basearch/
gpgcheck=1
enabled=0
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7
```

```shell
sudo yum update
sudo yum upgrade
```

```shell
sudo yum install -y epel-release
sudo yum install -y yum-utils
```
