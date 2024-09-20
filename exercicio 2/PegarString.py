def testarstring(a):
    count = 0

    for i in range(len(a)):
         if a[i] in ('a', 'A', 'á', 'â', 'ã', 'Á', 'Ã', 'Â'):
            count = count+1

    
    if count != 0:
        print(f"A String '{a}' tem um total de {count} letras 'A'")
    else:
         print(f"A String '{a}' não possuie letras 'A' ")




testarstring(input("Digite a String: "))