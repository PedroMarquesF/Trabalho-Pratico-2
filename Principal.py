# -*- coding: utf-8 -*-
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


        #print("data atual:",tempo)
        print("Digite o numero respectivo a opcao:\n")
        print("1-Consultar veiculos")
        print("2-Adicionar veiculo")
        print("3-Alugar/Reservar veiculo")
        print("4-Devolver/Liberar veiculo")
        print("5-Excluir veiculo")
        print("6-Avancar data atual")
        print("===================================")
        print("data atual:", tempo)
        print("quantidade de veiculos cadastrados:",len(p.vetquant))
        print("quantidade de veiculos alugados:",p.quantAlugados())
        print("quantidade de veiculos atrasados:", p.quantAtrasados())

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
                print("*****Tenha em mente que se o veiculo nao estiver disponivel(por motivos de atraso na entrega*****\n"
                      "*****de outro cliente) ate o dia do inicio da sua reserva ela sera automaticamente cancelada*****")
                print("Digite o veiculo que deseja de acordo com a numeração:")
                p.consultarVeiculos()
                veiculoNumero = int(input("~:")) - 1 #como se trata de um vetor a posição 1 é representada como 0 logo 1-1
                if veiculoNumero >= len(p.vetquant) or veiculoNumero < 0:
                    print("veiculo não existe")
                else:
                    if p.vetquant[veiculoNumero].ocuestado == "NA1":
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
                                    if indicador == "1":
                                        pass
                                    else:
                                        repet1 = 1
                                    rep += 1

                        nCadastro = input("Digite seu nome como cadastro")
                        p.vetquant[veiculoNumero].vetNome.append(nCadastro)
                        p.vetquant[veiculoNumero].vetDataInicial.append(datetime.date(ano, mes, dia))
                        p.vetquant[veiculoNumero].vetDataFinal.append(datetime.date(ano, mes, dia) + datetime.timedelta(days=qdia))
                        p.vetquant[veiculoNumero].vetPrioridade.append(0)
                        if p.vetquant[veiculoNumero].ocuestado == 0:
                            p.vetquant[veiculoNumero].ocuestado = 2 #quando o estado passa a ser 2 veiculo deixa de ser livre(0) e recebe o estatus de reservado
                        else:
                            pass
                        p.mudarData(tempo)
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
                    print("Digite 999 para sair")
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
                                    break
                                else:
                                    print("nop1")
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
                            posicao = 0
                            for im in p.vetquant[opc].vetPrioridade:
                                if im == "prioridade":
                                    break
                                else:
                                    print("nop")
                                    posicao = posicao + 1
                            diferenca_dias = (p.vetquant[opc].vetDataFinal[posicao] - p.vetquant[opc].vetDataInicial[posicao]).days
                            diferenca_dias_atraso = (tempo - p.vetquant[opc].vetDataFinal[posicao]).days
                            print(p.vetquant[opc].vetNome[posicao], "pagou",int(diferenca_dias) * int(p.vetquant[opc].vdiaria),"reais por", diferenca_dias,"dias de uso dentro do praso.")
                            cont = 0
                            valor_majorado = int(p.vetquant[opc].vdiaria) * 2
                            valor_a_pagar = valor_majorado * diferenca_dias_atraso

                            print(p.vetquant[opc].vetNome[posicao],"também pagou",valor_a_pagar,"reais de multa por",diferenca_dias_atraso,"dias de atraso")
                            del (p.vetquant[opc].vetNome[posicao])
                            del (p.vetquant[opc].vetDataInicial[posicao])
                            del (p.vetquant[opc].vetDataFinal[posicao])
                            del (p.vetquant[opc].vetPrioridade[posicao])
                            p.vetquant[opc].ocuestado = "NA"
                            p.mudarData(tempo)
                            p.mudarData(tempo)
                        else:
                            print("veículo não esta alugado")

                    elif escolha == "2":
                        if len(p.vetquant[opc].vetNome) == 0:
                            print("nao ha reservas cadastradas para esse veiculo")
                        else:
                            contador = 0
                            for aux in p.vetquant[opc].vetNome:
                                if p.vetquant[opc].vetPrioridade[contador] == 0:
                                    print(contador,"-", aux)
                                else:
                                    print(" - (conta nao disponivel,veiculo alugado ou atrasado)")
                                contador = contador + 1
                            conta_concelar = int(input("Digite a conta que deseja cancelar a partir da numeracao\nou\nDigite 999 para sair"))
                            if conta_concelar == 999:
                                pass
                            else:
                                if p.vetquant[opc].vetPrioridade[conta_concelar] == 0:
                                    del (p.vetquant[opc].vetDataFinal[conta_concelar])
                                    del (p.vetquant[opc].vetDataInicial[conta_concelar])
                                    del (p.vetquant[opc].vetNome[conta_concelar])
                                    del (p.vetquant[opc].vetPrioridade[conta_concelar])
                                    p.mudarData(tempo)
                                else:
                                    print("veiculo digitado nao existe ou esta alugado/com atraso")






                    else:
                        print("escolha uma das opcoes entre 1 e 2")




        elif opcao == "5":
            if len(p.vetquant) == 0:
                print("nao ha veiculos cadastrados")
            else:
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
            if nt < 0:
                print("não ha opcao retroceder data")
            else:
                tempo = tempo + datetime.timedelta(days=nt)
                p.mudarData(tempo)





        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")



main()
