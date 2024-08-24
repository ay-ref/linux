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

## Chapter 4 - Graphical Interface

- using linux
  - graphical user interface - gui
  - command line interface - cli

- seamless desktop environment
  - session manager
  - window manager
  - a set of utilities

- desktop environments
  - gnome
    - most used linux desktop
    - redhat
    - fedora
    - centos
    - suse linux enterprise
    - ubuntu
    - debian
  - kde
    - suse
    - opensuse

- you can change the background almost all linux :)

- locaking desktop shortcuts
  - `windows + l`
  - `ctrl + alt + l`

- linux is true multiuser os
  - you can login with different users in one system
  - you can switch user with logout and login again

- shutdown
  - in shutdown your open app data goes out
  - you can do this with gui easily with finding shutdown icon
  - you can do this by cli!

    ```shell
    shutdown now
    ```
  
- suspend
  - in suspend your app data in ram saved to use again
  after starting system again

- you can change default application with searching it in settings

- you can change file view in file manager window with
  - `ctrl + 1`
  - `ctrl + 2`
  - `ctrl + 3`

- you can see sorted by selecting the property of file columns at top
- you can see hidden files with `ctrl + h` shortcut or selecting from view at top  
- in linux dot started name files and folders are hidden and usually they are configs
- as default when in file manager you type something it start searching for a file
- linux opposite to windows has a very powerful search power for finding files!
and everyone use linux must use it!
- you can search for a regex pattern in file manager with `ctrl + s`

- `~` means the current client path

- your deleted files (if not permanently deleted) are found in
  - `~/.local/share/Trash/files`

- delete shortcut
  - `delete` button

- delete permanently shortcut
  - `shift + delete` button

> in linux we have directory in root of the system that is `/tmp` the
> content of this directory deleted after a period of time or policy that is configed
> in some files.

- every user has a seperate home directory

## Chapter 5 - System Configuration from Graphical User Interface

- NetworkManager is who that contorl your connections to the network

- NetworkManager vpn support
  - ipsec
  - cisco connect
  - microsoft pptp
  - openvpn

### Packaging

- debian packaging
  - `dpkg` is package manager name
  - `apt` is advance package tool

- every program usually have specific and particular distro target
and usually cannot be used in different os even in the same family :/

- red hat package manager
  - `rpm`
  - compatible with
    - suse/opensuse
    - centos
    - oracle linux

- fedora
  - `dnf`
  - `yum`

- suse/opensuse
  - `zypper`
  - `rpm`

## Chapter 6 - Common Applications  

- web browsers
  - chrome
  - firefox (linux default)
  - chromium
  - opera

- email application
  - graphical
    - thunderbird
    - claws mail
    - evolution
  - cli
    - mutt
    - mail

- office application
  - libre office

- development applicatoin
  - vscode
  - eclipse
  - vim

- sound player

- movie player
  - vlc
  - mplayer
  - xine
  - totem

- movie editors
  - cine paint
  - blender
  - cinelerra
  - ffmpeg

- graphic editors
  - gimp

## Chapter 7 - Command line Operation

- any possible task is doable in cli!
- you can write scripts for repeative tasks
- you can sign into remote machine anywhere in the internet
- you can initiate graphical application directly from cli

### CLI commands

- `cat <file-path>`
  - show the file text
  - combine files
- `head <file-path>`
  - show first lines of file
- `tail <file-path>`
  - show end lines of file
- `man <command>`
  - show the manual documentation of the commmand
- `cd <dir-path>`
  - change directory
- `login`
  - login to user account
- `exit`
  - exit terminal
- `echo <text>`
  - return text as output
- `ls`
  - list files and folders
- `rmdir <dir-name>`
  - remove directory
- `mkdir <dir-name>`
  - create new directory
- `touch <file-name>`
  - create new file

- cli input format

  ```shell
  <command> <-options> arguments
  ```

- options formats
  - `--<option>`
  - `-<o>`

#### sudo

- setup and running
  - run `su`
  - input password

- setup user as root

  ```shell
  echo "<user> ALL=(ALL) ALL" > /etc/sudoers.d/<user>
  chmod 440 /etc/sudoers.d/<user>
  ```

### Utilities

- switching between cli and gui

- virtual terminals
  - tty1 to tty6
    - `ctrl + alt + f1` to `ctrl + alt + f6`
  
- back to gui
  - `ctrl + alt + f7`

- stop gui service by one of followings

  ```shell
  sudo systemctl stop gdm 
  ```

  ```shell
  sudo tellinit 3
  ```

- start gui service by one of followings

  ```shell
  sudo systemctl start gdm
  ```

  ```shell
  sudo tellinit 5
  ```

- shutdown computer

  ```shell
  shutdown now
  ```

- shutdown scheduling!
  
  ```shell
  shutdown -h 10:00
  ```

### Locating Application

- applications usually are in the below folders
  - `/bin`
  - `/usr/bin`
  - `/sbin`
  - `/usr/sbin`
  - `/opt`
  - `/usr/local/bin`
  - `/usr/local/sbin`
  - `/home/<username>/bin`

- locating the application command

  ```shell
  which <app-name>
  ```

- locating the application command and its files

  ```shell
  whereis <app-name>
  ```

- print your current user directory

  ```shell
  echo $HOME
  ```

- see the current working direcotry

  ```shell
  pwd
  ```
  
- change directory to user root directory

  ```shell
  cd ~
  ```

  ```shell
  cd
  ```

- change directory to parent directory

  ```shell
  cd ..
  ```

- change to previous directory

  ```shell
  cd -
  ```

- `pushd` and `popd` are similar to `cd` and `cd -` with stack policy difference
  
- 2 different path determining
  - relative
    - from everywhere
  - absolute
    - from the root

- multiple sequence of slashes are ignored to just one slash

  ```shell
  ///usr////////bin = /usr/bin
  ```
  
- see the file system very clean way
  - see the current directory folders structure

    ```shell
    tree -d
    ```
  
  > `-d` just show directories
  
- for see list all of files and folders in directory (even hidden files)

  ```shell
  ls -a
  ```

- for see list of files and folders recursively

  ```shell
  ls -R
  ```

- for see list of files and folders in directory with line by line format

  ```shell
  ls -l
  ```

- for see list all of files and folders with uniqueness

  ```shell
  ls -i
  ```
  
- go to root directory

  ```shell
  cd /
  ```
  
### Links

- types of links in linux

  - hard line
    - `file1` exists
    - command

      ```shell
      ln file1 file2
      ```

    - created `file2` is a link for file1
    - id of file1 and file2 is same
  - soft link (symbolic link)
    - like hard link `ln -s` command
    - it create new id for file
    - it is practical for creating the shortcuts in terminal!

- to see the list of directories history

  ```shell
  dirs
  ```

### Working with Files

- file count data

  ```shell
  wc <file-name>
  ```
  
  - output:

    ```shell
    <lines-count> <words-count> <chars-count>
    ```

- see the whole content of file

  ```shell
  cat <file-name>
  ```
  
- see the whole content of file with line numbers

  ```shell
  cat -n <file-name>
  ```

- see the whole content of file with pagination

  ```shell
  less <file-name>
  ```

  > go to next line with `enter`,
  > go to next page with `space`,
  > go out with `q`.

- see the whole content of file with pagination with line numbers

  ```shell
  less -N <file-name>
  ```

- see first 10 lines of file

  ```shell
  head <file-name>
  ```

- see n first lines of file

  ```shell
  head -<n> <file-name>
  ```

> `tail` command show from last of file.

- see the content of the files reverse!!

  ```shell
  tac <file-name>
  ```
  
- create new file

  ```shell
  touch <file-name>
  ```

- create new file

  ```shell
  echo > <file-name>
  ```

- create directory

  ```shell
  mkdir <dirname>
  ```

- create directory with parents

  ```shell
  mkdir -p <dirpath>
  ```
  
- delete directory

  ```shell
  rmdir <dirname>
  ```

- delete path (everything with path)

  ```shell
  rm -rf <path>
  ```
  
- moving and renaming file

  ```shell
  mv <oldpath> <newpath>
  ```
  
- removing file

  ```shell
  rm <filename>
  ```

- find the file!!!

  ```shell
  locate <filenameregex>
  ```

  ```shell
  find <path> -name <filenameregex>
  ```

  - before these command run below command

    ```shell
    sudo updatedb
    ```

- filter the output

  ```shell
  <command> | grep <filter-regex>
  ```

> in linux `regex` is not exactly what it is, it is called `wildcards`.\\
> while using the `wildcards` use from quotes(`""`).

---

`find` is very powerfull command in linux and has many options!

---
  
### File Streams

- standard
  - input (stdin)
  - output (stdout)
  - error (stderr)

### I/O Redirection

- redirect by stdin

  ```shell
  <input> < <file-path>
  ```
  
- redirect from stdout

  ```shell
  <input> > <file-path>
  ```

- you can pipe commands to give the output of left command to input right command

  ```shell
  <command> | <command2> | <command3> 
  ```

  > this is a pipeline :). \\
  > pipes are very efficient for running commands because they deletes
  > disk read/write overloads
  
### Package Management System

- usually we have 2 types of package manager in linux os
  - low level like: dpkg, rpm
  - high level like: apt-get, zypper, yum, dnf

- By Package Management System
  - you can install new packages
  - you can remove existing packages
  - you can see the list of packages installed on your system
  - you can search for existing packages before installation
  - you can search in your package management system cache to see what you have

## Chapter 8 - Finding Linux Documentatoin

- linux documentation sources
  - man pages
  - gnu info
  - command help
  - other documentation
    - stackoverflow!

### Man Docs

- see the all of existing documentation about a topic in `man`

  ```shell
  whatis <topicname>
  ```
  
  ```shell
  man -f <topicname>
  ```
  
- see the all content docs `man`

  ```shell
  man -a <topicname>
  ```

- see the related to the topic `man` pages

  ```shell
  man -k <topicname>
  ```

### Gnu Info

- see the manual

  ```shell
  info <topicname>
  ```
  
- after all you can use from `--help` or `-h` to see every command documentation

  ```shell
  <command> --help
  ```
  
### Other Linux Documentations

- other documentations
  - desktop help system
  - package documentatoin
  - online sources

## Chapter 9 - Processes

- process types
  - interactive processes
    - ex: bash, firefox, top
  - batch processes
    - ex: updatedb, ldconfig
  - daemons
    - ex: httpd, sshd, libvirtd
  - threads
    - ex: firefox, gnome-terminal-server
  - kernel threads
    - ex: kthreadd, migration, ksoftirqd

- process specificatoin
  - process id (pid)
  - parent process id (ppid)
  - thread id (tid)

- terminate a process

  ```shell
  kill -SIGKILL <pid>
  ```
  
  ```shell
  kill -9 <pid>
  ```
  
- to see current processes

  ```shell
  ps -A
  ```
  
  ```shell
  ps -e
  ```
  
- ids
  - ruid: user id
  - rgid: group id
  - euid: user rights
  - egid: group rights

- nice is the priority of a task

- you can see the task with nice value

  ```shell
  ps l
  ```

- you can change the nice value

  ```shell
  renice <value> <pid>
  ```

- you can see the system uptime

  ```shell
  uptime
  ```

- what is load average numbers
  - cpu utilizatoin in
    - last 1 minutes
    - last 5 minutes
    - last 15 minutes

  > if you have multi-core cpu this number is in range of
  > your cpu count!

- you can see complete task manager in terminal

  ```shell
  top
  ```

- you can see the process tree!!!

  ```shell
  pstree
  ```

- you can sleep terminal with sleep command

  ```shell
  sleep <amount-time>
  ```

## Chapter 10 - File Operations

- in linux every thing is a file

- in linux as usual of an os file system is a tree

  ```shell
  - root
    - user1
      - Documents
      - ...
    - systemfiles
      - compilers
      - ...
    - devices
      - printer
      - ...
  ```
  
- root in linux is `/`

- linux standard pathes

  ```shell
  - /   (root)
    - /bin    (user binaries)
    - /sbin   (system binaryies)
    - /etc    (configuration files)
    - /dev    (device files)
    - /proc   (process information)
    - /var    (variable files)
    - /tmp    (temporary files)
    - /usr    (user programs)
    - /home   (home directories)
    - /boot   (boot loader files)
    - /lib    (system libraries)
    - /opt    (optional applications)
    - /mnt    (mount directory)
    - /media  (removable devices)
    - /srv    (service data)
  ```
  
- you can see the difference between text files

  ```shell
  diff <firstfilepath> <secondfilepath>
  ```

- you can see the difference between binary files

  ```shell
  cmp <firstfilepath> <secondfilepath>
  ```

- in linux file extensions like `.txt` is not useful for system
and just can be useful for users

- in linux you can find the file type

  ```shell
  file <path>
  ```

- you can copy files very optimized and just transmitting the changes

  ```shell
  rsync -r <sourcepath> <destinationpath>
  ```

  > `<path>` can be in another machine with format `someone@machine:address/to/path`
  