# Linux Network Notes

- see available connection network

```sh
nmcli connectoin show
```

```sh
nmcli connection up "ConnectionName" # find connection name in above command
```

```sh
nmcli connection down "ConnectionName"
```

- set static ip

  ```shell
  sudo nmcli con mod ConnectionName ipv4.method manual ipv4.addresses 192.168.56.100/24 ipv4.gateway 192.168.56.1 ipv4.dns 8.8.8.8
  ```

- network manager setting from terminal with ui

  ```shell
  nmtui
  ```

- restart your `iptables` to first configs

```sh
sudo iptables -F
sudo iptables -X
sudo iptables -P INPUT ACCEPT
sudo iptables -P FORWARD ACCEPT
sudo iptables -P OUTPUT ACCEPT
sudo iptables -t nat -F
sudo iptables -t mangle -F
sudo systemctl restart yourservice # like docker, postgresql, ...
```

- see the porxies

  ```shell
  $ env | grep -i proxy
  NO_PROXY=localhost,127.0.0.0/8,127.0.1.1
  http_proxy=http://192.168.1.250:8080/
  FTP_PROXY=ftp://192.168.1.250:8080/
  ftp_proxy=ftp://192.168.1.250:8080/
  all_proxy=socks://192.168.1.250:8080/
  ALL_PROXY=socks://192.168.1.250:8080/
  HTTPS_PROXY=https://192.168.1.250:8080/
  https_proxy=https://192.168.1.250:8080/
  no_proxy=localhost,127.0.0.0/8,127.0.1.1
  HTTP_PROXY=http://192.168.1.250:8080/
  ```

- see network interfaces

  ```shell
  ip a
  ```

- see network connections

  ```shell
  nmcli con show
  ```

- how to see the hostname

  ```shell
  hostname
  ```

- how to see the hostname ip in LAN

  ```shell
  hostname -I
  ```

> first ip is your ipv4 in LAN

## Ports

- see which ports are used!

  ```shell
  netstat -tunlp
  ```

- see port status

  ```shell
  nmap -p 5432 172.19.0.3
  ```

- how to see the current port usuage:

  ```shell
  sudo lsof -i -P -n | grep LISTEN
  ```

## Troubleshooting

### `ping` okay, browser not okay!

- probably you should fix dns
