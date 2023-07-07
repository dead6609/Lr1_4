with open('1.dat', 'rb') as in_f:
    b = in_f.read()
with open('2.dat', 'wb') as out_f:
    out_f.write(b[::-1])