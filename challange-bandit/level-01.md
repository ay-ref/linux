# level 01

## level goal

The password for the next level is stored in a file called - located in the home directory

## solution

```shell
bandit1@bandit:~$ ls
-
bandit1@bandit:~$ ls
-
bandit1@bandit:~$ ls -a
-  .  ..  .bash_logout  .bashrc  .profile
bandit1@bandit:~$ cat -
^C
bandit1@bandit:~$ ls
-
bandit1@bandit:~$ cd /
bandit1@bandit:/$ ls
bin                dev      formulaone  lib    lib.usr-is-merged  media  proc  sbin                srv  usr
bin.usr-is-merged  drifter  home        lib32  libx32             mnt    root  sbin.usr-is-merged  sys  var
boot               etc      krypton     lib64  lost+found         opt    run   snap                tmp
bandit1@bandit:/$ cd home/
bandit1@bandit:/home$ ls
bandit0   bandit15  bandit21  bandit27-git  bandit30-git  bandit6    drifter12  drifter5     formulaone2  krypton4
bandit1   bandit16  bandit22  bandit28      bandit31      bandit7    drifter13  drifter6     formulaone3  krypton5
bandit10  bandit17  bandit23  bandit28-git  bandit31-git  bandit8    drifter14  drifter7     formulaone5  krypton6
bandit11  bandit18  bandit24  bandit29      bandit32      bandit9    drifter15  drifter8     formulaone6  krypton7
bandit12  bandit19  bandit25  bandit29-git  bandit33      drifter0   drifter2   drifter9     krypton1     ubuntu
bandit13  bandit2   bandit26  bandit3       bandit4       drifter1   drifter3   formulaone0  krypton2
bandit14  bandit20  bandit27  bandit30      bandit5       drifter10  drifter4   formulaone1  krypton3
bandit1@bandit:/home$ cd bandit28
bandit1@bandit:/home/bandit28$ ls
bandit1@bandit:/home/bandit28$ ls
bandit1@bandit:/home/bandit28$ cd ..
bandit1@bandit:/home$ cd bandit1
bandit1@bandit:~$ ls
-
bandit1@bandit:~$ less -
bandit1@bandit:~$ 
bandit1@bandit:~$ ls -l
total 4
-rw-r----- 1 bandit2 bandit1 33 Sep 19 07:08 -
bandit1@bandit:~$ ls -
bandit1@bandit:~$ cat ./-
263JGJPfgU6LtdEvgfWU1XP5yac29mFx
```
