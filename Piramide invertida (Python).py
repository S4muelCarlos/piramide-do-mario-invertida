altura=int(input('qual e a altura da piramide?'))
contador = 1
while contador <=altura:
    espacos = altura - contador 
    print('#'*espacos + ' '* contador)
    contador = contador+1