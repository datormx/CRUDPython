# def fibonacci(max):
#     a, b = 0, 1
#     while a < max:
#         yield a 
#         a, b = b, a+b

# fib1 = fibonacci(20)
# fib_nums = [num for num in fib1]
# print(fib_nums)

# double_fib_nums = [num * 2 for num in fib1] #No va a funcionar
# print(double_fib_nums)
# double_fib_nums = [num * 2 for num in fibonacci(20)] #Sí va a funcionar
# print(double_fib_nums)

def cuenta(max):
    a = 0
    while a < max:
        yield a
        a += 1


conteo = [num for num in cuenta(20)]
print(conteo)
      