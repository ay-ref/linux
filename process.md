# Process

- see all process

  ```shell
  ps aux | grep whatyouwant
  ```

- see process for port usage

  ```shell
  sudo lsof -i :5432
  ```

- running and background and also saving logs!

  ```shell
  yourcommand >output.log 2>&1 &
  ```

- see your background procceses

  ```shell
  jobs
  ```

> you can have the latest runned background job in the session with **`$i`** command!

- The `+` symbol indicates the current job. This is the job that will be affected by commands like fg or bg if you don't specify a job ID.

- The `-` symbol indicates the previous job (the one before the current job).

- Other jobs do not have a symbol.

- Running

  - The job is actively running in the background.

- Stopped

  - The job has been paused (e.g., with Ctrl+Z).

- Done

  - The job has completed execution.

- brings job [1] to the foreground.

```shell
fg %1
```

- resumes job [1] in the background.

```shell
bg %1
```

- kills job [1].

```shell
kill %1
```

## Signals to Processes

![signals](./figs/signals.png)

[IMAGE LINK](https://i.sstatic.net/9EQBC.png)

- see all signals

  ```shell
  sudo kill -l
  ```

- kill process

  ```shell
  sudo kill -9 pid
  ```

## systemd

- start the service

```shell
systemctl start yourservice.service
```

- stop the service

```shell
systemctl stop yourservice.service
```

- restart the service

```shell
systemctl restart yourservice.service
```

- enable the service to run after boot

```shell
systemctl enable yourservice.service
```

- diable the service to run after boot

```shell
systemctl diable yourservice.service
```

## ssh

- get a file from remote

  ```shell
  scp remoteuser@remotehostip:/path/to/file localdirectory
  ```

- get a folder complete from remote

  ```shell
  scp -r remoteuser@remotehostip:/path/to/directory localdirectory
  ```

- send a file to destination ip

  ```shell
  scp filepath remoteuser@remotehostip:/remote/to/directory
  ```

- send a folder to destination ip

  ```shell
  scp -r folderpath remoteuser@remotehostip:/remote/to/directory
  ```

- copy files with progress status

  ```shell
  rsync -ah --progress source destination
  ```

- sha2 hash of string

  ```shell
  echo -n "your text" | sha256sum
  ```

- send DHCP

  ```shell
  sudo dhclient -r
  sudo dhclient
  ```

- change date

  ```shell
  date -s "date_output_like"
  ```

- while linux is up it should create a swap in size of your ram,
  if it can't (for example for having full disk drive),
  the system does not goes up, (if you can)decrease
  the amount of ram for solving from problem temporary!
