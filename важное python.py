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