import datetime
from ClassPrincipal import Painel


def main():
    print((datetime.date(2018, 11, 2) - datetime.date(2018, 11, 20)).days)
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
                        repet1 = 0
                        while repet1 == 0:
                            print("Digite a data inicial que deseja ficar com esse veículo:")
                            repet = 0
                            aux2 = 0
                            dia = int(input("digite o dia:"))
                            mes = int(input("o mês:"))
                            ano = int(input("e o ano:"))
                            print("digite a quantidade de dias que deseja passar com o carro")
                            qdia = int(input())
                            qdiai = datetime.date(ano, mes, dia)
                            qdiaf = datetime.date(ano, mes, dia) + datetime.timedelta(days=qdia)
                            if datetime.date(ano, mes, dia) < tempo:
                                print("data digitada se encontra no passado")
                            elif len(p.vetquant[veiculoNumero].vetDataInicial) == 0:
                                repet1 = 1
                            else:
                                rep = 0
                                while rep < len(p.vetquant[veiculoNumero].vetDataInicial):
                                    indicador = 0
                                    if (qdiai > p.vetquant[veiculoNumero].vetDataInicial[rep] and qdiai < p.vetquant[veiculoNumero].vetDataFinal[rep]
                                    or (qdiaf > p.vetquant[veiculoNumero].vetDataInicial[rep] and qdiaf < p.vetquant[veiculoNumero].vetDataFinal[rep])) :
                                        print("(A data digitada esta se chocando com outra reserva, por gentileza, escolha outra data:)")
                                        indicador = 1
                                    if indicador == 1:
                                        pass
                                    else:
                                        repet1 = 1
                                    rep += 1

                        '''while repet == 0:
                            if len(p.vetquant[veiculoNumero].vetDataInicial) == 0:
                                repet = 1
                            else:
                                di = datetime.date(ano, mes, dia)
                                df = di + datetime.timedelta(days=qdia)
                                repet = 1 #por enquanto'''
                        nCadastro = input("Digite seu nome como cadastro")
                        p.vetquant[veiculoNumero].vetNome.append(nCadastro)
                        p.vetquant[veiculoNumero].vetDataInicial.append(datetime.date(ano, mes, dia))
                        p.vetquant[veiculoNumero].vetDataFinal.append(datetime.date(ano, mes, dia) + datetime.timedelta(days=qdia))
                        p.vetquant[veiculoNumero].vetPrioridade.append(0)
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
                        print("(veículo não alugado ou reservado)")
                    else:
                        print(auxi,"-",aux.modelo)
                opc = int(input("~:")) - 1
                if opc > len(p.vetquant) or opc < 0:
                    print("Veículo não existe")
                else:
                    print("1-Devolver veículo")
                    print("2-Cancelar reserva")
                    escolha = input("~:")
                    if escolha == "1":
                        if p.vetquant[opc].ocuestado == 1:
                            posicao = 0
                            for im in p.vetquant[opc].vetPrioridade:
                                if im == "prioridade":
                                    pass
                                else:
                                    posicao += 1

                            diferenca_dias = (tempo - p.vetquant[opc].vetDataInicial[posicao]).days
                            print(p.vetquant[opc].vetNome[posicao], "pagou", int(diferenca_dias) * int(p.vetquant[opc].vdiaria),"reais por", diferenca_dias, "dias de uso.")
                            del(p.vetquant[opc].vetNome[posicao])
                            del(p.vetquant[opc].vetDataInicial[posicao])
                            del(p.vetquant[opc].vetDataFinal[posicao])
                            del (p.vetquant[opc].vetPrioridade[posicao])
                            p.vetquant[opc].ocuestado = "NA"
                            p.mudarData(tempo)
                            p.mudarData(tempo)
                        elif p.vetquant[opc].ocuestado == 11:
                            diferenca_dias = (p.vetquant[opc].vetDataFinal[0] - p.vetquant[opc].vetDataInicial[0]).days
                            pass
                        else:
                            print("veículo não esta alugado")


                    elif escolha == "2":
                         pass
                    else:
                        print("sem escolhas válidas digitadas")



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
