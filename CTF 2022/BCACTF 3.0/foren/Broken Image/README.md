# Broken Image

50 points - By Krish

Tag: foren

My friend said that he made a really cool drawing in MS Paint but I can't open it! Maybe my computer is broken? Or the image? I really don't know. Could you try opening it for me and telling me what it is?

## Write up
1. Using the `file` tool, detect the type of the image as png.

``` bash
┌──(kali㉿kali)-[~/Desktop]
└─$ file chall.svg 
chall.svg: PNG image data, 1011 x 169, 8-bit/color RGB, non-interlaced
```

2. Change the image extension and open the image.

![](solve.png)

Flag: `bcactf{br0k3n_1m4g3_4nd_1m4g3_4nd_1m4g3}`