counter = 1
while counter <= 5:
    print(counter)
    counter = counter + 1

counter_2 = 1
while counter_2 <= 10:
    print('Olá mundo!')
    counter_2 = counter_2 + 1

counter_3 = 1
quant_products = int(input('Informe a quantidade de produtos: '))
while counter_3 <= quant_products:
    name_product = input('informe o nome do produto: ')
    print(name_product)
    counter_3 = counter_3 + 1

c = 6
s = 0
while c > 0:
    n = float(input('Informe o número: '))
    s = s + n
    c -= 1
    print(f'a soma é {s}.')
