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
                veiculoNumero = int(input("~:")) - 1 #como se trata de um vetor a posição 1 é representada como 0 logo 1-1
                if veiculoNumero >= len(p.vetquant) or veiculoNumero < 0:
                    print("veiculo não existe")
                else:
                    if p.vetquant[veiculoNumero].ocuestado == 1:
                        print("este veículo não esta disponível")
                    else:

                        print("Digite a data inicial que deseja ficar com esse veículo:")
                        #repet = 0 so pra lembrar dos limitadores
                        dia = int(input("digite o dia:"))
                        mes = int(input("o mês:"))
                        ano = int(input("e o ano:"))
                        print("digite a quantidade de dias que deseja passar com o carro")
                        qdia = int(input())
                        nCadastro = input("Digite seu nome como cadastro")
                        p.vetquant[veiculoNumero].vetNome.append(nCadastro)
                        p.vetquant[veiculoNumero].vetDataInicial.append(datetime.date(ano, mes, dia))
                        p.vetquant[veiculoNumero].vetDataFinal.append(datetime.date(ano, mes, dia) + datetime.timedelta(days=qdia))
                        p.vetquant[veiculoNumero].ocuestado = 2 #quando o estado passa a ser 2 veiculo deixa de ser livre(0) e recebe o estatus de reservado

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
            op = int(input()) - 1
            if p.vetquant[op].ocuestado == 1:
                print("Este veículo não pode ser excluido pois está alugado")
            elif p.vetquant[op].ocuestado == 2:
                print("Este veículo não pode ser excluido pois está reservado")
            elif p.vetquant[op].ocuestado == 11:
                print("Este veículo não pode ser excluido pois está alugado com atraso(cliente ainda não desolveu)")
            else:
                print("veículo",p.vetquant[op],"excluído com sucesso")
                del(p.vetquant[op])

        elif opcao == "6":
            print("a quantidade de dias que deseja avançar")
            nt = int(input())
            tempo = tempo + datetime.timedelta(days=nt)
            p.mudarData(tempo)





        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")



main()
