# Hidden Frequencies

100 points - By Yusuf

Tag: crypto

I downloaded one of my friend's files and he got really defensive... it looks like gibberish but I think there might be more to it.

[msg.txt](msg.txt)

## Hint

- Do all characters appear the same number of times?

## Write up


Letter frequency table in [msg.txt](msg.txt):

``` python3
import pandas as pd
msg = ''
with open('msg.txt', 'rb') as f:
    msg += f.read().decode()

print(pd.Series(list(msg)).value_counts())
```

| Letter   | Number of occurrences |
| -------- | --------------------- |
| &        |  125                  |
| g        |  123                  |
| z        |  121                  |
| v        |  117                  |
| n        |  116                  |
| e        |  116                  |
| s        |  114                  |
| p        |  114                  |
| k        |  114                  |
| u        |  113                  |
| %        |  110                  |
| x        |  110                  |
| .        |  108                  |
| $        |  106                  |
| i        |  104                  |
| r        |  102                  |
| f        |  102                  |
| #        |  101                  |
| m        |   99                  |
| d        |   99                  |
| h        |   99                  |
| 7        |   99                  |
| b        |   99                  |
| y        |   99                  |
| ^        |   98                  |
| a        |   98                  |
| c        |   97                  |
| >        |   97                  |
| 0        |   95                  |
| 6        |   95                  |
| q        |   95                  |
| ?        |   95                  |
| 3        |   95                  |
| @        |   70                  |
| !        |   53                  |
| <        |   53                  |
| 4        |   53                  |
| 2        |   53                  |
| l        |   52                  |
| j        |   52                  |
| w        |   51                  |
| o        |   51                  |
| t        |   51                  |
| 1        |   49                  |
| 8        |   48                  |
| 9        |   48                  |
| 5        |   48                  |


We notice that with each character corresponding to the number of occurrences, that is the decimal value, proceed to convert to characters according to the ascii encoding. Then match each earned character together => flag.

``` python3
c_tmp = 'a'
count = 0
flag = ""
for c in msg + " ":
    if c != c_tmp:
        c_tmp = c
        flag += chr(count)
        count = 1
    else:
        count += 1

print(flag)
```

Flag: `bcactf{ch4r4ct3r_fr3qu3ncy_15_50_c00l_55aFejnb}`