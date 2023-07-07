import random
import linecache
from os.path import dirname, join
current_dir = dirname(__file__)
file_path = join(current_dir, "./lines.txt")
f = open(file_path,"r", encoding="UTF-8")
k=random.randint(1,sum(1 for _ in f))
print(linecache.getline(file_path , (k)))

linecache.clearcache()
f.close()
input()
