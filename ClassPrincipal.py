# -*- coding: utf-8 -*-
import datetime
from ClassVeiculo import Veiculo
from ClassVeiculoAlugar import VeiculoAlugado


class Painel():
    def __init__(self, vq, vqa, datahoje):
        self.vetquant = vq
        self.vetquantAlu = vqa
        self.dhoje = datahoje

    def consultarVeiculos(self):
        cont = 0
        for i in self.vetquant:
            cont += 1
            if i.ocuestado == 0:
                estado = "Livre"
            elif i.ocuestado == 1:
                estado = "Alugado"
            elif i.ocuestado == 2:
                estado = "Reservado"
            elif i.ocuestado == 11:
                estado = "alugado com atraso"
            print(str(cont).zfill(3),"-",i,estado)
        else:
            print("---------")

    def addveiculo(self):
        print("Digite a marca do veiculo:")
        marca = input()
        print("Digite o modelo do veiculo")
        modelo = input()
        print("Digite o ano do veiculo:")
        ano = input()
        print("Digite o valor da diaria")
        diaria = input()
        self.vetquant.append(Veiculo(0, marca, modelo, ano, diaria, 0,[],[],[],[]))



    def vetalugados(self):
        self.vetDias = []

    '''def admdatas(self, veiculoNumero):
        self.vetquant[veiculoNumero].vetDataInicial.append(self.vetquant[veiculoNumero].dataInicial)
        #self.vetquant[veiculoNumero].admDatas.append(self.vetquant[veiculoNumero].dataFinal)'''

    '''def admdataspegar(self,veiculoNumero):
        print(self.vetquant[veiculoNumero].vAdmDatasI[0])'''

    def mudarData(self,novoTempo):
        print("passou aqui0")
        for auxiliar in self.vetquant:
            #a = 0
            i = -1
            if auxiliar.ocuestado == 0:
                print("passou aqui")
                pass
            elif auxiliar.ocuestado == 2:
                print("passou aqui1")
                a = len(auxiliar.vetDataFinal)
                while i < a - 1:
                    i = i + 1
                    print("passou aqui3")
                    #print(self.vetquant[a].vetDataInicial)
                    print(auxiliar.vetDataFinal[i])
                    if auxiliar.vetDataFinal[i] < novoTempo:
                        print("ita")
                        auxiliar.vetPrioridade[i] = "prioridade"
                        auxiliar.ocuestado = 11
                        break
                    elif auxiliar.vetDataInicial[i] <= novoTempo and auxiliar.vetDataFinal[i] > novoTempo:
                        print("passou aqui2")
                        auxiliar.vetPrioridade[i] = "prioridade"
                        auxiliar.ocuestado = 1
                        break

                    else:
                        print("continua reservado")
            elif auxiliar.ocuestado == 1:
                a = len(auxiliar.vetDataFinal)
                while i < a - 1:
                    i = i + 1
                    print("passou aquiaa")
                    if auxiliar.vetDataFinal[i] < novoTempo:
                        print("itaala")
                        auxiliar.vetPrioridade[i] = "prioridade"
                        auxiliar.ocuestado = 11

                    else:
                        pass
            elif auxiliar.ocuestado == "NA":
                print("passou aqui NA")
                if len(auxiliar.vetDataFinal) == 0:
                    print("passou aqui NA1")
                    auxiliar.ocuestado = 0
                else:
                    print("passou aqui NA2")
                    #a = len(auxiliar.vetDataFinal)
                    iaux = 0
                    for contador in range(0, 1000):

                        for iaux in range(0,len(auxiliar.vetDataFinal)):
                            print(len(auxiliar.vetDataFinal))

                            if auxiliar.vetDataFinal[iaux] < novoTempo or auxiliar.vetDataInicial[iaux] < novoTempo:
                                del (auxiliar.vetDataFinal[iaux])
                                del (auxiliar.vetDataInicial[iaux])
                                del (auxiliar.vetNome[iaux])
                                del (auxiliar.vetPrioridade[iaux])

                                if len(auxiliar.vetDataFinal) == 0:
                                    print("FUNCIONA")
                                    break
                                iaux = iaux + 1
                            else:
                                break
                            break




                    for iaux in auxiliar.vetDataFinal:
                        if iaux == "excluido":
                            del (iaux)
                        else:
                            pass

                    for iaux in auxiliar.vetDataInicial:
                        if iaux == "excluido":
                            del (iaux)
                        else:
                            pass

                    for iaux in auxiliar.vetNome:
                        if iaux == "excluido":
                            del (iaux)
                        else:
                            pass

                    for iaux in auxiliar.vetPrioridade:
                        if iaux == "excluido":
                            del (iaux)
                        else:
                            pass



                        '''a = len(auxiliar.vetDataFinal)
                        iaux = 0
                        print("-",iaux)
                        if len(auxiliar.vetDataFinal) == 0:
                            auxiliar.ocuestado = 0
                            break

                        while iaux < a:
                            print(iaux)
                            if auxiliar.vetDataFinal[iaux] < novoTempo or auxiliar.vetDataInicial[iaux] < novoTempo:
                                print("1")
                                del (auxiliar.vetNome[iaux])
                                del (auxiliar.vetDataInicial[iaux])
                                del (auxiliar.vetDataFinal[iaux])
                                del (auxiliar.vetPrioridade[iaux])
                                auxiliar.ocuestado = 0
                                iaux = a
                            else:
                                print("NA1")
                                iaux = iaux + 1'''

                        '''if len(auxiliar.vetDataInicial) > 0:
                            print("NA2")
                            auxiliar.ocuestado = 2
                            break'''


                    if len(auxiliar.vetDataInicial) > 0:
                        auxiliar.ocuestado = 2
                    else:
                        auxiliar.ocuestado = 0






