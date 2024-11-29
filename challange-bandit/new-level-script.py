import os

preword = "level"
file_content = '''# level LEVELNUMBER

## level goal

DESCRIPTION

## solution

```shell
CONTENT
```
'''

ls = os.listdir()

nmax = -1
for l in ls:
    if preword in l:
        l = l[:l.index('.')]
        try:
            print(l)
            l = l.split("-")[-1]
            l = int(l)
            nmax = max(l, nmax)
        except:
            print('not a number')
        
n = nmax + 1
new_number_string = str(n).zfill(2)
file_content.replace('LEVELNUMBER', new_number_string)
file_name = preword + "-" + new_number_string + ".md"

f = open(os.path.join('./', file_name), 'w+')
f.write(file_content)
