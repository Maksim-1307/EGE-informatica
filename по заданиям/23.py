def f(a, b):
    if a == b: return 1
    if a == 5: return 0 # 5 избегаемый
    if a > b: return 0
    return f(a+2, b) + f(a*3, b)
print(f(1,9)*f(9,17)) # 9 обязательный



