# Linux

## General

### Shell

- `grep` one of the most practical linux commands for filtering:
  - example:

    ```shell
    ls | grep <wanted-folder>
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

- open app from cli
  - firefox

    ```shell
    firefox
    ```

  - google chrome

    ```shell
    google-chrome
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
  
## Mint

- app names
  - cinammon ui
    - file manager: nemo
  - xface ui
    - file manager: thunar
    - pdf reader: xreader

- install `.deb` package

  ```shell
  sudo dpkg -i <packagepath>
  ```

- for becoming root user

  ```shell
  sudo su
  ```

- how to see current user in cli

  ```shell
  whoami
  ```
  
## Centos

- app names
  - gnome ui
    - file manager: nautilus

- if the root disk usage become 100% your operating system
does not boot!!!
