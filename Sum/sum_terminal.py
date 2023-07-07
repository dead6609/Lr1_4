from os.path import dirname, join

current_dir = dirname(__file__)
f = open(current_dir + "./chek.txt", "r", encoding="UTF-8")
summ=0
for k in f:
    z=k.split("\t")
    summ+= float(z[1])*float(z[2])
    
print('%.2f' %summ)
f.close()
a = input()
