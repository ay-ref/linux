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
