def beecrowd2540():
    while True:
        try:
            n = int(input())
        except EOFError as EOF:
            break
        aprovacao = (2/3)*n
        votos = map(int,input().split())
        soma = 0
        for voto in votos:
            soma+=voto
        #print(soma)
        if (soma>=aprovacao):
            print("impeachment")
        else:
            print("acusacao arquivada ")

def beecrowd1021():
    notas = [100, 50, 20, 10, 5, 2]
    moedas = [1, 0.50, 0.25, 0.10, 0.05 , 0.01]
    QTDNotas = [0]*len(notas)
    QTDMoedas = [0]*len(moedas)
    valor_entrada = input().split(".")
    parte_inteira = int(valor_entrada[0])
    parte_decimal = int(valor_entrada[1])
    valorInt = parte_inteira
    for i in range (len(notas)):
        while(valorInt>=notas[i]):
            QTDNotas[i]+=1
            valorInt-=notas[i]
        print("NOTAS:")
        for i in range(len(notas)):
            strg = f"{QTDNotas[i]} de R${notas[i]}"
            print(strg)
    Original_Moedas = moedas.copy()
    for i in range (len(moedas)):
        moedas[i] *= 100
        moedas[i] = int(moedas[i])
    #print("Parte decimal",parte_decimal)
    #print(moedas)
        valorInteiro = parte_decimal+valorInt*100
        for i in range(len(moedas)):
            while (valorInteiro>=moedas[i]):

                QTDMoedas[i]+=1
                valorInteiro-=moedas[i]
            print("MOEDAS:")
            for i in range(len(moedas)):
                strg = "arrumar"

    







if __name__=="__main__":
    beecrowd1021()