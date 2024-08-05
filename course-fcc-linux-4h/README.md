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
