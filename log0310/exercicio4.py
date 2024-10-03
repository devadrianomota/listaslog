def fat (a):
    if a == 0 or a==1:
        return 1 
    else:
        return a* fat (a-1)
print (fat(7)) 