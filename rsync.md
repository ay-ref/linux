# rsync linux command

- this is one of super command in linux!

- add new changes to a bakcup like folder

```bash
rsync -avn --ignore-existing updatedFolder backupFolder 
```

```bash
rsync -av --ignore-existing updatedFolder backupFolder 
```

- moving file from a remote to current host

```bash
rsync -avz -e ssh \
  --exclude='*.log' \
  --exclude='temp/' \
  user@remote:/var/www/html/ \
  /backup/local_html/
```
