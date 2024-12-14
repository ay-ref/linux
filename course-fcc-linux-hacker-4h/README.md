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

- see the complete documentation of a command

  ```shell
  man thecommand
  ```

- usual way to see the command(app) documentation

  ```shell
  thecommand -h
  ```

  ```shell
  thecommand --help
  ```

  ```shell
  thecommand -help
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

- pci information (see the graphic card)

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
  
> you can see my `bandit` challange solutions in linux reference root folder `challange-bandit`

## `xargs`

- get the output as an input for a command!!!

  ```shell
  $ ls
  another.txt  myfile.txt  README.md
  $ cat another.txt myfile.txt README.md 
  inside text wrote file
  inside text wrote file
  inside markdown text
  $ ls | grep -E "*.txt" | xargs cat
  inside text wrote file
  inside text wrote file
  ```

## `file` command

```shell
$ whatis file   
file (1)             - determine file type
```

```shell
file *
another.txt:      ASCII text
myfile.txt:       ASCII text
README.md:        ASCII text
```

## shell

- the terminal interface that you works with it

- see the default shell

  ```shell
  echo $SHELL                          
  /usr/bin/zsh
  ```

- see the all available shells

  ```shell
  cat /etc/shells
  # /etc/shells: valid login shells
  /bin/sh
  /bin/bash
  /usr/bin/bash
  /bin/rbash
  /usr/bin/rbash
  /usr/bin/sh
  /bin/dash
  /usr/bin/dash
  /bin/zsh
  /usr/bin/zsh
  ```

### bash and zsh

- bash config files

  ```shell
  ls -a | grep .bash 
  .bash_history
  .bash_logout
  .bash_profile
  .bashrc
  ```
  
- zsh config files

  ```shell
  ls -a | grep .zsh    
  .oh-my-zsh
  .shell.pre-oh-my-zsh
  .zshenv
  .zsh_history
  .zshrc
  ```

- `history` command

  ```shell
  history (3readline)  - GNU History Library
  ```
  
## space usage

```shell
whatis du     
du (1)               - estimate file space usage
```

> du runs on current path recursively!

- very practical example usage

  ```shell
  du -sh * | sort -rh
  ```

> `sort -h` means human readable sort! (1G > 23K)

## disk usage

```shell
whatis df
df (1)               - report file system disk space usage
```

> not very practical!

## `tar`

```shell
whatis tar
tar (1)              - an archiving utility
```

- archiving

  ```shell
  tar -cvf tarnewfilename.tar folderpath
  ```

  ```shell
  tar -czvf tarnewfilename.tar.gz folderpath
  ```

- unarchiving
  
  ```shell
  tar -xvf archivedfile.tar
  ```

  ```shell
  tar -xzvf archivedfile.tar.gz
  ```

## users and groups creation
