# level 02

## level goal

The password for the next level is stored in a file called spaces in this filename located in the home directory

## solution

```shell
bandit2@bandit:~$ ls
spaces in this filename
bandit2@bandit:~$ ls -l
total 4
-rw-r----- 1 bandit3 bandit2 33 Sep 19 07:08 spaces in this filename
bandit2@bandit:~$ ls
spaces in this filename
bandit2@bandit:~$ ls -a
.  ..  .bash_logout  .bashrc  .profile  spaces in this filename
bandit2@bandit:~$ cat spaces\ in\ this\ filename 
MNk8KNH3Usiio41PRUEoDFPqfxLPlSmx
```
