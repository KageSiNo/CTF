#import pandas as pd
msg = ''
with open('msg.txt', 'rb') as f:
    msg += f.read().decode()

#print(pd.Series(list(msg)).value_counts())
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