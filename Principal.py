import datetime
from ClassPrincipal import Painel


def main():
    #date_1 = datetime.date(2018, 11, 2)
    #end_date = date_1 + datetime.timedelta(days=60)
    #print(end_date)

    repetidor = "a"
    p = Painel([],[],datetime.date.today())
    #if datetime.date.today() > datetime.date(2018, 11, 2):
        #print("funfou")
    tempo = datetime.date.today()
    while repetidor == "a":


        print("data atual:",tempo)
        print("Digite o numero respectivo a opcao:\n")
        print("1-Consultar veiculos")
        print("2-Adicionar veiculo")
        print("3-Alugar/Reservar veiculo")
        print("4-Devolver/Liberar veiculo")
        print("5-Excluir veiculo")
        print("6-Avançar data atual")
        print("===================================")
        print("quantidade de veículos cadastrados:",len(p.vetquant))
        print("")

        opcao = input("~:")
        if opcao == "1":
            p.consultarVeiculos()
            ver = input("deseja ver mais informações sobre algum veículo S/N")
            if ver == "S" or ver == "s":
                ver1 = int(input("digite o número respectivo ao veículo")) - 1
                print("marca:",p.vetquant[ver1].marca,"\nano:",p.vetquant[ver1].ano,"\nValor da diária:",p.vetquant[ver1].vdiaria)
            else:
                pass
        elif opcao == "2":
            p.addveiculo()
        elif opcao == "3":
            if len(p.vetquant) == 0:
                print("não há veiculos cadastrados")
            else:
                print("Digite o veiculo que deseja de acordo com a numeração:")
                p.consultarVeiculos()
                veiculoNumero = int(input("~:")) - 1
                if veiculoNumero >= len(p.vetquant) or veiculoNumero < 0:
                    print("veiculo não existe")
                else:
                    if p.vetquant[veiculoNumero].ocuestado == 1:
                        print("este veículo não esta disponível")
                    else:

                        print("Digite a data inicial que deseja ficar com esse veículo:")
                        dia = int(input("digite o dia:"))
                        mes = int(input("o mês:"))
                        ano = int(input("e o ano:"))
                        print("digite a quantidade de dias que deseja passar com o carro")
                        qdia = int(input())
                        p.vetquant[veiculoNumero].dataInicial = datetime.date(ano, mes, dia)
                        p.vetquant[veiculoNumero].dataFinal = p.vetquant[veiculoNumero].dataInicial + datetime.timedelta(days=qdia)
                        print(p.vetquant[veiculoNumero].dataInicial)
                        print(p.vetquant[veiculoNumero].dataFinal)
                        print(p.vetquant[0].modelo)
                        #p.admdataspegar(veiculoNumero)

        elif opcao == "4":
            if len(p.vetquant) == 0:
                print("não há veiculos cadastrados")
            else:
                print("Digite o veiculo que deseja devolver de acordo com a numeração:")
                auxi = 0
                for aux in  p.vetquant:
                    auxi += 1
                    if aux.ocuestado == 0:
                        print("(veículo não alugado)")
                    else:
                        print(auxi,"-",aux.nome)
                opc = int(input("~:")) - 1
                if opc > len(p.vetquant) or opc < 0:
                    print("Veículo não existe")
                else:
                    p.vetquant[opc].ocuestado = 0
                    p.vetquant[opc].dataInicial = 0

        elif opcao == "5":
            print("Digite o veiculo que deseja de acordo com a numeração:")
            p.consultarVeiculos()
            op = int(input())
            del(p.vetquant[op])

        elif opcao == "6":
            print("a quantidade de dias que deseja avançar")
            nt = int(input())
            tempo = tempo + datetime.timedelta(days=nt)
            p.mudarData(tempo)





        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")



main()
