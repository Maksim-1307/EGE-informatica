# сортировка по первому по возрастанию, потом по второму по убыванию
array = [(1, 0), (3, 2) … ]
sortedarr = sorted(array, lambda el: (el[0], -el[1])) 

# ускорение рекурсии, кеширует значения 
from functools import lru_cache
@lru_cache(None)
def myfunc(a):
    return 

# перебор всех комбинаций  
from itertools import product
for word in product('01234', repeat=3):
	print(word)
      
# перевод из 10 в любую
string = ''
while n > 0:
    string+=str(n%3)
    n//= 3 
print(string[::-1])

# перевод из любой в 10
int('F8', 16)

# округление в меньшую и большую стороны
from math import ceil, floor

#ip
from ipaddress import ip_network
net = ip_network("address/mask")
c = 0
for ip in net:
     if f'{ip:b}'.count('1') % 2 == 0: c += 1

# дополнение строки незначащими нулями до 8 символов
formatted_num = '{:0>8}'.format(num)

# разделение с несколькими разделителями
# 1 аргумент - любые разделители через |
import re
re.split("a | b | c|d|    ", "str to split")
# разделение по символам A-F
re.split("[A-F]+", "str to split")

#filter
arr = ['some', '', 'array', 'with', '', '', 'gapes']
arr = list(filter(lambda x: x != '', arr)) # removes gapes