def testarsequencia(n):
    fibonacci = [0,1]

    if  isinstance(n, (int)):
        a = 0;
        
        while n > a:
            fibonacci.append(fibonacci[-2] + fibonacci[-1])
            a = fibonacci[-1]

        if n == fibonacci[-1]:
            return f"O seu numero {n} Se encontra na sequencia de fibonacci.A sequencia até seu numero é: {fibonacci}"
        else:
            return f"O seu numero {n} não se encontra na sequencia de fibonacci.A sequencia até o numero mais proximo é: {fibonacci}"


    else:
        return "Caractere Informado não é valido."
    


try:
    num = int(input("Digite o valor que deseja pesquisar na sequência de Fibonacci: "))

    print(testarsequencia(num))

except ValueError:

    print("insira um número inteiro valido.")
