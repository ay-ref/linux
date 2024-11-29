# level 03

## level goal

The password for the next level is stored in a hidden file in the inhere directory.

## solution

```shell
bandit3@bandit:~$ ls
inhere
bandit3@bandit:~$ ls -a
.  ..  .bash_logout  .bashrc  inhere  .profile
bandit3@bandit:~$ cd inhere/
bandit3@bandit:~/inhere$ ls -a
.  ..  ...Hiding-From-You
bandit3@bandit:~/inhere$ cat ...Hiding-From-You 
2WmrDFRmJIq3IPxneAaMGhap0pFhF3NJ
```
