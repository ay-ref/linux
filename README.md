# Linux

- install `.deb` package

```shell
sudo dpkg -i packagepath
```

- recommended to don't install snap on linux!
- just try download the file from the internet.

- how to see the hostname ip in LAN

```shell
hostname -I
```

> first ip is your ip in LAN

- add `alias` permanently in one command
  ```shell
  echo "alias aliasname='aliascommand'" >> ~/.bashrc && source ~/.bashrc
  echo "alias aliasname='aliascommand'" >> ~/.zshrc && source ~/.zshrc
  ```
