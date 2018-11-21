# -*- coding: utf-8 -*-
import datetime
from ClassVeiculo import Veiculo


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


    def quantAlugados(self):
        cont = 0
        for auxcont in self.vetquant:
            if auxcont.ocuestado == 1:
                cont = cont + 1
            else:
                pass
        return cont
    def quantAtrasados(self):
        cont = 0
        for auxcont in self.vetquant:
            if auxcont.ocuestado == 11:
                cont = cont + 1
            else:
                pass
        return cont

    def mudarData(self,novoTempo):
        for auxiliar in self.vetquant:
            #a = 0
            i = -1
            if auxiliar.ocuestado == 0:
                pass
            elif auxiliar.ocuestado == 2:
                a = len(auxiliar.vetDataFinal)
                if len((auxiliar.vetDataFinal)) == 0:
                    auxiliar.ocuestado = 0
                else:
                    pass
                while i < a - 1:
                    i = i + 1
                    #print(self.vetquant[a].vetDataInicial)
                    print(auxiliar.vetDataFinal[i])
                    if auxiliar.vetDataFinal[i] < novoTempo:
                        auxiliar.vetPrioridade[i] = "prioridade"
                        auxiliar.ocuestado = 11
                        break
                    elif auxiliar.vetDataInicial[i] <= novoTempo and auxiliar.vetDataFinal[i] > novoTempo:
                        auxiliar.vetPrioridade[i] = "prioridade"
                        auxiliar.ocuestado = 1
                        break

                    else:
                        print("continua reservado")
            elif auxiliar.ocuestado == 1:
                a = len(auxiliar.vetDataFinal)
                while i < a - 1:
                    i = i + 1
                    if auxiliar.vetDataFinal[i] < novoTempo:
                        auxiliar.vetPrioridade[i] = "prioridade"
                        auxiliar.ocuestado = 11

                    else:
                        pass


            elif auxiliar.ocuestado == "NA":
                if len(auxiliar.vetDataFinal) == 0:
                    auxiliar.ocuestado = 0
                else:
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
                                    break
                                iaux = iaux + 1
                            else:
                                break
                            break

                    if len(auxiliar.vetDataInicial) > 0:
                        auxiliar.ocuestado = 2
                    else:
                        auxiliar.ocuestado = 0