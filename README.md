# Linux

```sh
rsync -avz -e ssh \
  --exclude='*.log' \
  --exclude='temp/' \
  user@remote:/var/www/html/ \
  /backup/local_html/
```

## General

### Shell

- install and config **zsh**

  - [LINK](https://gist.github.com/n1snt/454b879b8f0b7995740ae04c5fb5b7df)

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

    > you have very very practical flag `-v` that **exclude** files.

- how to see current user in cli

  ```shell
  whoami
  ```

- recommended to don't install snap on linux!

- just try download the file from the internet.

- change the password to everything you want!

  ```sh
  sudo passwd youruser
  ```

> **_`_` does not contains hidden files!!!\***

- add `alias` permanently in one command

  ```shell
  echo "alias aliasname='aliascommand'" >> ~/.bashrc && source ~/.bashrc
  echo "alias aliasname='aliascommand'" >> ~/.zshrc && source ~/.zshrc
  ```

- one of the fastest way to define your commands as shortcut
  is to use from `alias`es, even in your running project!

  - in your project folder

    - create a file like name `setup.sh`

    - define your function

      ```sh
      yourname() {
          yourcommand
      }
      ```

      - you can use from input arguments by `$1`, `$2`, ...
      - you can call the function like `yourname firstarg secondarg`

    - now use from your `command1`, `command2` easily

- add app to path

  ```shell
  echo 'export PATH=/your/directory/path:$PATH' >> ~/.bashrc && source ~/.bashrc
  ```

- see the disk usage useful commands

  ```shell
  df -h yourpath
  df -h /
  du -shx * | sort -rh | head -10
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

- fast dns add/remove

```sh
sudo sed -i '2i\nameserver 192.168.200.168' /etc/resolv.conf
sudo sed -i '2d' /etc/resolv.conf
```

- issue with entering bios in fast boot

```sh
systemctl reboot --firmware-setup
```

- issue with opening drive in kde gui or arch linux

```sh
lsblk
sudo ntfs-3g /dev/sda2 .
```

- go to terminal before login to linux shortcut:

  - `ctrl + alt + f2`
  - for back to graphical:
    - `ctrl + alt + f1` (centos worked)
    - `ctrl + alt + f7` (mint worked)

- how to run `.jar` file

  ```shell
  java -jar yourjarfile.jar
  ```

  > if you saw large files in linux think about NTFS.

> **for large files( > 2GB) zipping you should use from zip splitting feature in linux if you dont use from ntfs**

- remove a file recursively

  ```shell
  find . -name "FILENAMEWILDCARD" -delete
  ```

- increase the time login time

  ```shell
  sudo visudo
  ```

  ```shell
  Defaults        timestamp_timeout=240 # in minutes (4 hours)
  ```

- to beautify the `json` format

  ```shell
  jsonoutputer | jq .
  ```

- see log online

  ```shell
  tail -f output.log
  ```

- find and replace all command from out of text file

  ```shell
  sed 's/pattern/replacement/g' file
  ```

  ```shell
  sed -i 's/pattern/replacement/g' file
  ```

  ```shell
  sed -i.bak 's/pattern/replacement/g' file
  ```

- just a process to up system

  ```shell
  sleep 600 # 10 minutes
  ```

- run a command periodic to see the result realtime

  ```shell
  watch -n 0.5 your_command
  ```

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

- symmetric encryption with just passphrase! (**_very practical_**)

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

#### apps

- file manager: thunar
- disk usage analyzer: baobab
- pdf reader: xreader
- text editor: xed

#### tricks

- zooming (in normal mode :) )
  - `alt` + `scroll`

### Gnome

- file manager: nautilus
- disk usage analyzer: baobab
- pdf reader: xdg-open
- text editor: gedit

### KDE

- file manager: dolphin

## Distros

### Debian

- install `.deb` package

  ```shell
  sudo dpkg -i <packagepath>
  ```

- list packages (YOU SHOULD DO THIS BEFORE DELETE)

  ```shell
  sudo dpkg --list
  ```

- remove `.deb` package

  ```shell
  sudo dpkg -r <packagepath>
  ```

### Ubuntu

- problem with the screen stuck on login after sleep mode
	- after starting your system and up you should
	  restart the `mdm` or `lightdm` service

		```sh
		sudo service mdm restart # or
		sudo service lightdm restart
		```

### Mint

- mint has has no default root password!, you should set for it

  ```shell
  sudo passwd root
  ```

- install `.deb` package

  ```shell
  sudo dpkg -i <packagepath>
  ```

- remove `.deb` package

  ```shell
  sudo dpkg -r <packagepath>
  ```

- for becoming root user

  ```shell
  sudo su
  ```

- install font

  - download the font and its typefaces

  - copy your `.ttf` or `.otf` or `...` files in the `~/.fonts` folder

  - create `~/.fonts` if it does not exist.

  - the fonts loaded after you reopen the apps that you are used!

### fedora

- see the all installed Packages

```shell
rpm -aq
```

- download your rpm with **DEPENDENCIES**

```shell
yumdownloader --resolve <package_name>
```

- export `rpm` file.

```shell
sudo yum install rpmrebuild
```

- create `rpm`

```shell
rpmrebuild your_app_name
```

### centos

- if the root disk usage become 100% your operating system
  does not boot completely!!!
  - you probably go to your virtual terminal with `ctrl+alt+f2`
    shortcut to remove some of your data for booting completely!

## Apps and Packages

### ncat

- a package for general-purpose command-line tool for reading, writing, redirecting
  and encrypting data across a network.

- run server

  ```shell
  nc -lv <port>
  ```

- sending data to server

  ```shell
  nc -v localhost <port> # tcp
  ```

  ```shell
  nc -u localhost <port> # udp
  ```
  
### unrar

- extract `.rar` file

  ```shell
  unrar x yourfile.rar
  ```

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

## Games!

### SuperTuxCart

- racing
- open-source
- singleplayer
- multiplayer
- online and lan possible
- 700 MB :)

### AssaultQube

- shooting
- open-source
- singleplayer
- multiplayer
- online and lan possible
- 50 MB :))
