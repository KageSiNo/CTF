
import string

ALPHA = "_{}" + string.ascii_lowercase + string.ascii_uppercase

bin =  '01010000001011100010110000010110001101000110111000111100000101100000100000101100001001000001111000100000000110100001011001000000010000000011101000010100000101100100000000101100010000000011011000100000001000100001011001000000001110000011110000011010001101000000010'
bin = "".join(["0" if b == "1" else "1" for b in bin])

flag = ""
while True:
    for c in ALPHA:
       t = format(ord(c), 'b')
       if bin.startswith(t + "1"):
           flag += c
           print(flag)
           bin = bin[len(t) + 1:]
           break
    if len(bin) <= 8:
        flag += chr(int('0b' + bin, 2))
        break
       
print(flag)