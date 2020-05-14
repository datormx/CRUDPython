def funcion(valor):
    valor+=1
    print(f'valor del namespace local: {valor}')


valor = int('23')
print(f'valor del namespace global: {valor}')


funcion(23)
