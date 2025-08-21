#high Order Functions
def increment(x):
    return x + 1
def high_ord_func(x, func): #func es una funcion que se pasa como parametro
    return x + func(x)

res = high_ord_func(2, increment)
print(res)

#AHORA CON LAMBDA
increment_v2 = lambda x : x + 1
high_ord_func_v2 = lambda x, func: x + func(x)

res = high_ord_func_v2(2, increment_v2)
print(res)

res = high_ord_func_v2(2, lambda x: x * 2)
print(res)