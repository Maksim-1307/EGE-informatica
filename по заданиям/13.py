from ipaddress import ip_network

def is_pol(s):
    for i in range(len(s)//2):
        if s[i] != s[-i-1]: return False
    return True 

net = ip_network('95.112.224.0/255.255.255.128')
c = 0
for ip in net:
    byte = bin(int(str(ip).split('.')[-1]))[2:]
    byte = '{:0>8}'.format(byte)
    
    if is_pol(byte): 
        c += 1
        print(byte)
print(c)