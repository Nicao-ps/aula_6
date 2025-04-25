answer = ''
while True:
    n = float(input('Informe um número: '))
    print(n)

    answer = input('Deseja continuar? S/N ').upper()[0]
    print(answer)
    if answer == 'N':
        break
