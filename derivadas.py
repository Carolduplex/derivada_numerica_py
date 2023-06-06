import numpy as np
import matplotlib.pyplot as grafico
import math

''' Testando limitações da linguagem ao calcular a derivada numerica de uma função'''

## função y = x^3*sin(x)
def f(x):
    y = (x**3)*np.sin(x)
    return y


def der_direita(f, x, delta):
    return (f(x+delta) - f(x))/delta

def der_central(f, x, delta):
    return (f(x+delta) - f(x-delta))/(2*delta)


x = 3
prova  = 3*x**2*np.sin(x) + x**3*np.cos(x) #derivada analítica f'(x)
delta = np.logspace(-16., 0, 50)

y_direita = der_direita(f, x, delta)
y_central = der_central(f, x, delta)
grafico.plot(delta, y_direita)
grafico.plot(delta, y_central)
grafico.hlines(prova,1e-16, 1e1, color = "red")
grafico.xscale('log')
grafico.show()

erro_direita = (abs(prova - y_direita))/(abs(prova))
erro_central = (abs(prova - y_central))/(abs(prova))

grafico.plot(delta, erro_direita)
grafico.plot(delta, erro_central)
grafico.xscale('log')
grafico.show()

