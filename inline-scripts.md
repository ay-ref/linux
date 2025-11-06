# Inline Scripts

## range download

```sh
python3 -c "
import os
for i in range(3, 36):
    os.system(f'wget https://site/downloadlist/item-{i}.pdf')
"
```
