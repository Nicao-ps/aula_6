
f_weather = ['Ensolarado', 'Nublado', 'Chuvoso', 'Tempestade', 'Ensolarado']

n = int(input('Informe um valor para n: '))

print(f_weather[n])  # [n] = [0, 1, 2, 3, 4]
print(f_weather[-n])  # [-n] = [0, -4, -3, -2, -1]
print(f_weather[2:])  # [2:] = [N, N, S, S, S]
print(f_weather[:2])  # [:2] = [S, S, N, N, N]
print(f_weather[-2:])  # [-2:] = [N, N, N, S, S]
print(f_weather[:-2])  # [:-2] = [S, S, S, N, N]
print(f_weather[2:-2])  # [2:-2] = [N, N, S, N, N]
