# Crappy Colonization Corp
225 points - By skysky

Tag: crypto, rev

Yay, we finally got someone to Mars! It's bureaucracy time!

[provided.rs](provided.rs)

`nc crypto.bcactf.com 49157`

## Hint
- Your IGUID is not used as an index into the hashmap. Only the result of the "proprietary algorithm" is used.
- Although your IGUID is not used as an index into the hashmap... it is still stored as a vector of bytes in "used_keys".
- How proprietary is this "proprietary algorithm", anyway?

## Write up

In this challenge I did not solve it because I am not fluent in the programming language `Rust`. I provided a write up from another organization:

[Original writeup - Alleviation](https://alleviation.xyz/2022/06/07/bcactf-3-0-2022/4/).

Flag: `bcactf{m@yb3_d0nt_u53_md5_f0r_int3rg@lact1c_c0l0n1z@t10n}`