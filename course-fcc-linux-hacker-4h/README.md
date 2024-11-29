# Free Code Camp Course - Linux Essentials for Hackers - 4 hours

- linux is imoprtant for
  - security
  - system administration
  - personal use! (I want this :) )

- linux can run on
  - virtual machine
  - baremetal

## useful keyboard shortcuts

- open terminal
  - `ctrl + alt + t`

- move window to top, right, bottom, left
  - `window + arrowkeys`

- increase/decrease font size
  - `ctrl + shift + "+"`
  - `ctrl + "-"`

- clear the terminal
  - `ctrl + l`
  - `clear` command

- end the current process
  - `ctrl + c`

- see history commands
  - `top and bottom in arrowkeys`

- auto complete command
  - `tab`
  - `right-arrowkey`

- close the window
  - `ctrl + w`
  - `ctrl + shift + w`

## file management and manipulation

- print working directory

  ```shell
  pwd
  ```

- list directory

  ```shell
  ls
  ```

- list direcotry in a table

  ```shell
  ls -l
  ```

- list directory also hiddens

  ```shell
  ls -a
  ```

- list direcotry in a table human readable

  ```shell
  ls -lh
  ```

- list direcotry recursively!

  ```shell
  ls -R
  ```

- cahnge directory to home directory

  ```shell
  cd
  ```

  ```shell
  cd ~
  ```

- change directory to previous directory

  ```shell
  cd -
  ```

- change directory to parent directory

  ```shell
  cd ..
  ```

- change directory to any directory you want

  ```shell
  cd wanteddirectorypath
  ```

- change directory to root directory

  ```shell
  cd /
  ```

- see the one line documentation of a command!!!

  ```shell
  whatis thecommand
  ```

- create new file

  ```shell
  touch newfilename
  ```

- returning a line

  ```shell
  echo yourlinegoeshere
  ```

- redirect output to a file

  ```shell
  echo "something" > somefile
  ```

- see the content of a file

  ```shell
  cat somefile
  ```

- copy content of a file to another file

  ```shell
  cat somefile > anotherfile
  ```

- remove a file or directory

  ```shell
  rm yourfile
  ```

  ```shell
  rm -r yourdirectory
  ```

- remove all files and folders in a directory

  ```shell
  rm -r *
  ```

- create a directory

  ```shell
  mkdir yournewdirectoryname
  ```

- copy a file to another directory

  ```shell
  cp yourfilepath yournewdirectory
  ```

- copy a directory to another directory

  ```shell
  cp -r yourfolderpath yournewdirectory
  ```

- move a file or folder to new directory

  ```shell
  mv yourfileorfolderpath yournewdirectory
  ```

- rename a file

  ```shell
  mv yourfileorfolderpath yournewname
  ```

- remove a direcotry

  ```shell
  rmdir yourdirectorypath
  ```

- open a file with nano editor

  ```shell
  nano filepath
  ```

- open a file with vim editor

  ```shell
  vi filepath
  ```

## file and directory permissions

- in a file config: `drwxrwxrwx`
  - `d` shows directory, `-` shows file
  - `r` shows read permission
  - `w` shows write permission
  - `x` shows execute permission
  - `-` shows without permission
  - first `rwx` is for owner of file
  - second `rwx` is for group of file
  - third `rwx` is for others of file

- change the permission of file

 ```shell
 chmod mapuserstopermissions filepath
 ```

- map users to permissions
  - `ugo`: owner, group, others
  - `rwx`: read, write, execute
  - `=+-`: equal, append, delete

- also you can use from binary to map users to permissions

- change the permission of folder

 ```shell
 chmod -R mapuserstopermissions folderpath
 ```

## file and directory ownership

- every file has a user and also a group

- change the owner of file

 ```shell
 chown newowner filepath
 ```

- change the group of file

 ```shell
 chgrp newgroup filepath
 ```

- see the groups

 ```shell
 groups
 ```

- see the groups of specific user

 ```shell
 groups username
 ```

- see the current logined users

 ```shell
 users
 ```

## `grep` and piping

```shell
$ whatis grep
grep (1)             - print lines that match patterns
```

- usually `grep` used in 2 ways
  - direct
  - pipe the last command

### direct `grep`

- searching in file

 ```shell
 grep "word" filepath
 ```

> `-i` usually used for case-insensitive way

### `grep` with pipe

- simple use

 ```shell
 yourfirstcommandwithoutput | grep "wordsearchinginoutput"
 ```

## finding files with `locate`

```shell
$ whatis locate
locate (1)           - find files by name, quickly
```

- actually `locate` is not very practical command in my opinion...

## enumerating distribution and kernel information

- current user

 ```shell
 whoami
 ```

- os(workstation) name

 ```shell
 hostname
 ```

- change `hostname`

 ```shell
 sudo nano /etc/hostname
 ```

- see the linux distribution

 ```shell
 lsb_release -a
 ```

 ```shell
 cat /etc/issue
 ```

 ```shell
 cat /etc/os-release
 ```

 ```shell
 cat /etc/*release
 ```

 ```shell
 uname -a
 ```

- cpu information

 ```shell
 lscpu
 ```

- pci information

 ```shell
 lspci
 ```

## find and bandit challanges

```shell
$ whatis find    
find (1)             - search for files(also directories) in a directory hierarchy
```

- very powerful command!

- usage

 ```shell
 find pathtosearch specifiers
 ```

- specifiers
  - `-type`
  - `-name`
  - `-iname`
  - `-size`
  - `-perm`
