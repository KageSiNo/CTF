
chessies = []
with open('FEN.txt', 'r') as f:
    chessies = [l.strip() for l in f.readlines()]


m = ""

for chessy in chessies:
    for row in reversed(chessy.split('/')):
        for c in row:
            m += '0' * int(c) if c.isdigit() else '1'
                
print(int(m, 2).to_bytes((len(m) + 7) // 8, byteorder='big').decode())