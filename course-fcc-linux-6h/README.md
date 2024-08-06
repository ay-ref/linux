# Free Code Camp Course - Linux

## Chapter1 - Introduction to Linux Families

- linux has many distrobutions

- in this course we consider 3 major distrobution family
  - red hat family system (rhel)
    - centos
    - fedora
  - suse family system
    - opensuse
  - debian family system
    - ubuntu
    - mint

- family is some distro together that has a common base code

### rhel family

- fedora and upstream testing platform
- red hat enterprise linux
- distors
  - centos
  - centos stream
  - fedora
  - orcale linux
- intel x86, arm, itanium, powerpc
- package manager
  - yum
  - dnf
- most popular family in enterprise

### suse family

- sles is upstream for opensuse
- rpm-based zypper package manager
- yast for system administration purposes

### debian family

- ubuntu is upstream for linux mint
- dpkg-based apt package manager
- widely used for cloud deployment

## Chapter 2 - Linux Philosophy and Concepts

- if you want to konw more about any topic in linux just `man` command

    ```shell
    man <topic>
    ```

- 3 way to run linux for learning
  - run in native (bare metal)
  - run in virtual box
  - run live on flash or cd

### Terminology

- kernel
  - kernel is glue between hardware and application

- distrobution
  - collection of software making up a linux-based os

- boot loader
  - program that boots the os
  - example
    - grub
    - isolinux

- service
  - program that runs as a background process
  - example
    - httpd
    - nfsd
    - ntpd
    - ftpd
    - named

- fily system
  - storing and organizing files
  - example
    - ext3
    - ext4
    - fat
    - xfs
    - ntfs
    - btrfs

- x windowing system
  - graphical subsystem on nearly all linux systems

- desktop environment
  - graphical user interface on top of the operating system
  - example
    - gnome
    - kde
    - xfce
    - fluxbox

- command line
  - interface for typing commands on top of the os

- shell
  - command line interpreter that interprets the command line input
    and instructs the os to perform any neccessary tasks and commands
    - example
      - bash
      - tcsh
      - zsh

## Chapter 3 - Linux Basics and System Startup

### BIOS - the first setup

- bios
  - basic input/output system

- the computer setup process
  - power on
  - bios (post process)
    - power on self test
      - in power on check the screens and keyboards
  - master boot record (mbr)
    - first sector of the disk
    - searches for the grub and store it to ram
  - boot loader (grub)
  - kernel (linux os)
  - initial ram disk (`initramfs`)
    - command shell login
      - in this level file system load to ram
      - command shell
        - show prompt for waiting input
        - after entering the command and pressing the enter (return key)
        it executes the command and show outputs
  - `/sbin/init` (parent process)
  - systemd
    - now systemd is the service runner that runs main services
    - systemd commands

      ```shell
      sudo systemctl start | stop | restart <service-name>
      sudo systemctl enable | disable <service-name> # starting at system boot
      ```

### Linux File System Basics

- conventional disk filesystems
  - ext3
  - ext4
  - btrfs
  - jfs
  - ntfs
  - vfat

- flash storage filesystems
  - ubifs
  - jffs2
  - yaffs

- database filesystems

- special purpose filesystems
  - procfs
  - sysfs
  - tmpfs
  - squashfs
  - debugfs

- partition and filesystems
  - partition is a physical division of disk for storing data
  - filesystems means the way of saving the files

|  | windows | linux |
| --- | --- | --- |
| partition | Disk1 | /dev/sda1 |
| filesystem type | ntfs/vfat | ext3/ext4/xfs/btrfs  |
| mounting parameters | DriveLetter | MountPoint |
| base folder (os is stored) | C:\ | / |

### Filesystem Hierarchy Standard

- file hierarchy standard (fhs)

- linux use from `/` to seperate path windows use `\`!

- linux shell is case sensetive

- you can select the current folder path in linux with
navigating to the folder that you want and then use shortcut
`ctrl + l` to see the copyable path of folder

### Linux Distributions Practical

- server
  - rhel/centos
  - ubuntu server
  - sles
  - debian

- desktop
  - ubuntu
  - mint
  - debian

- embedded
  - yocto
  - open embedded
  - android

### Linux Installation

- usual partitions (linux hard disk = `sda`)
  - `/` (sda1)
  - `/home` (sda2)
  - `/var` (sda3)
  - `/swap` (sda4)

- tools recomended in linux installation
  - firefox
  - libre office
  - apache web server
  - mysql database

- fedora and centos use selinux by default

- desktop usually equals to workstation in linux distros

- for linux filesystem type ext4 is recommended because it is very compatible

- end of chapter 3
