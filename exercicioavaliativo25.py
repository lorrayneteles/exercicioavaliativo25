#peça os coeficientes da equaçao do 2º grau e calcule suas raizes
a = float(input('Digite o coeficiente a:'))
b = float(input('Digite o coeficiente b:'))
c = float(input('Digite o coeficiente c:'))
delta = b**2 - 4*a*c
if delta < 0:
    print('A equação não possui raizes reais')
    exit()
x1 = (-b + delta**0.5) / (2*a)
x2 = (-b - delta**0.5) / (2*a)
print(f'As raizes da equação são {x1} e {x2}')
