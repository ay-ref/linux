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

- how to see the hostname ip in LAN

```shell
hostname -I
```

> first ip is your ip in LAN

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

## Mint

- mint app names
  - cinammon ui
    - file manager: nemo
  - xface ui
    - file manager: thunar
    - pdf reader: xreader

- install `.deb` package

```shell
sudo dpkg -i packagepath
```

## Centos

- if the root disk usage become 100% your operating system
does not boot!!!
