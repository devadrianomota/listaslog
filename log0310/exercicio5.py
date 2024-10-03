def primo (b):
    if b<2 or b==2 or b%2==0:
       return f'{b} nao é numero primo'
    else: 
        return f'{b} é um numero primo'
print (primo(9))   
print (primo(12))