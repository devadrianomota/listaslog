import math 
def equacao (a, b, c):
    if a == 0:
        return 'nao é uma equaçao de segundo grau'
    delta= b**2-4*a*c 
    if delta<0 :
        return 'nao possui raiz a equacao'
    elif delta ==0:
        raiz = -b/(2*a)
        return f'equacao possui uma raiz dupla {raiz}'
    else: 
        raiz1=(-b+ math.sqrt(delta))/(2*a)
        raiz2=(-b- math.sqrt(delta))/(2*a)
        return f'a equacao tem duas raizes{raiz1} e {raiz2}'
resultado= equacao(2, -3, 2)   
print (resultado)
      