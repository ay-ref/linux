# Linux

## General

### Shell

- create new file

  ```shell
  touch <filename>
  ```

- create a range of files
  - example:

    ```shell
    touch myfiles{1..10}.txt
    ```
  
- `grep` one of the most practical linux commands for filtering:
  - example:

    ```shell
    ls | grep <wanted-folder>
    ```

- how to see current user in cli

  ```shell
  whoami
  ```

- recommended to don't install snap on linux!
- just try download the file from the internet.

- how to see the hostname

  ```shell
  hostname
  ```

- how to see the hostname ip in LAN

  ```shell
  hostname -I
  ```

> first ip is your ipv4 in LAN

- how to see the current port usuage:

  ```shell
  sudo lsof -i -P -n | grep LISTEN
  ```
  
- add `alias` permanently in one command

  ```shell
  echo "alias aliasname='aliascommand'" >> ~/.bashrc && source ~/.bashrc
  echo "alias aliasname='aliascommand'" >> ~/.zshrc && source ~/.zshrc
  ```

- see the disk usage of folders and files:

  ```shell
  df -h <your-path>
  ```

  - example:

      ```shell
      df -h /
      ```

  - or

    ```shell
    sudo du -h --max-depth=1
    ```

- see the partitions

  ```shell
  lsblk
  ```

- go to your flash removable

  ```shell
  cd /run/<username>/<medianame>
  ```

- find in file contents

  ```shell
  grep -rnw yourpath -e "yourregex"
  ```
  
  
- go to terminal before login to linux shortcut:
  - `ctrl + alt + f2`
  - for back to graphical:
    - `ctrl + alt + f1` (centos worked)
    - `ctrl + alt + f7` (mint worked)

### Snap

- installing

  ```shell
  sudo snap install <your-package>
  ```

- removing

  ```shell
  sudo snap remove <your-package>
  ```

### Security

#### File Encryption

##### GPG (GNUPG)

- generate keys

  ```shell
  gpg --gen-key
  ```

- see your keys

  ```shell
  gpg --list-secret-keys
  ```
  
- export your keys

  ```shell
  gpg --export-secret-keys [key-id | email] > private_key.asc
  ```
  
- import your keys

  ```shell
  gpg --import private_key.asc
  ```

- delete a key

  ```shell
  gpg --delete-key [KeyID]
  gpg --delete-secret-key [KeyID]
  ```

- symmetric encryption with just passphrase! (***very practical***)

  ```shell
  gpg -c --no-symkey-cache <filename>
  ```

- assymetric encryption with pair key

  ```shell
  gpg -e -r <key-email> <filename>
  ```
  
- now decrypt symmetric

  ```shell
  gpg -d <filename>.gpg > <filename>
  ```

## GUI's

### Cinammon

- file manager: nemo

### Xfce

- file manager: thunar
- pdf reader: xreader

### Gnome

- file manager: nautilus

## Distros

### Mint

- install `.deb` package

  ```shell
  sudo dpkg -i <packagepath>
  ```

- for becoming root user

  ```shell
  sudo su
  ```
  
### Centos

- if the root disk usage become 100% your operating system
does not boot completely!!!
  - you probably go to your virtual terminal with `ctrl+alt+f2`
  shortcut to remove some of your data for booting completely!

## Apps and Packages

### ncat

- a package for general-purpose command-line tool for reading, writing, redirecting
and encrypting data across a network.

### Firefox

- open app

  ```shell
  firefox
  ```

### Google Chrome

- open app

  ```shell
  google-chrome
  ```
