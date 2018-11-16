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
                    if auxiliar.vetDataFinal[i] < novoTempo:
                        print("ita")
                        auxiliar.vetPrioridade[i] = "prioridade"
                        auxiliar.ocuestado = 11
                        '''auxiliar.vetDataFinal.insert(0, auxiliar.vetDataFinal[i])
                        auxiliar.vetDataInicial.insert(0, auxiliar.vetDataInicial[i])
                        auxiliar.vetNome.insert(0, auxiliar.vetNome[i])
                        del(auxiliar.vetDataFinal[i+1])
                        del (auxiliar.vetDataInicial[i+1])
                        del (auxiliar.vetNome[i+1])'''
                    elif auxiliar.vetDataInicial[i] <= novoTempo and auxiliar.vetDataFinal[i] > novoTempo:
                        print("passou aqui2")
                        auxiliar.vetPrioridade[i] = "prioridade"
                        auxiliar.ocuestado = 1
                        '''auxiliar.vetDataFinal.insert(0, auxiliar.vetDataFinal[i])
                        auxiliar.vetDataInicial.insert(0, auxiliar.vetDataInicial[i])
                        auxiliar.vetNome.insert(0, auxiliar.vetNome[i])
                        del (auxiliar.vetDataFinal[i+1])
                        del (auxiliar.vetdatainicial[i+1])
                        del (auxiliar.vetnome[i+1])'''
                    else:
                        print("deixar aqui pra ver nunca vai acontecer")
            elif auxiliar.ocuestado == 1:
                a = len(auxiliar.vetDataFinal)
                while i < a - 1:
                    i = i + 1
                    print("passou aquiaa")
                    if auxiliar.vetDataFinal[i] < novoTempo:
                        print("itaala")
                        auxiliar.vetPrioridade[i] = "prioridade"
                        auxiliar.ocuestado = 11
                        '''auxiliar.vetDataFinal.insert(0, auxiliar.vetDataFinal[i])
                        auxiliar.vetDataInicial.insert(0, auxiliar.vetDataInicial[i])
                        auxiliar.vetNome.insert(0, auxiliar.vetNome[i])
                        del (auxiliar.vetDataFinal[i+1])
                        del (auxiliar.vetDataInicial[i+1])
                        del (auxiliar.vetNome[i+1])'''
                    else:
                        pass
            elif auxiliar.ocuestado == "NA":
                if len(auxiliar.vetDataInicial) == 0:
                    auxiliar.ocuestado = 0
                else:
                    a = len(auxiliar.vetDataFinal)
                    while i < a - 1:
                        i = i + 1
                        if auxiliar.vetDataFinal[i] < novoTempo or auxiliar.vetDataInicial[i] < novoTempo:
                            del (auxiliar.vetNome[i])
                            del (auxiliar.vetDataInicial[i])
                            del (auxiliar.vetDataFinal[i])
                            del (auxiliar.vetPrioridade[i])
                            auxiliar.ocuestado = 0
                        elif auxiliar.vetDataInicial[i] > novoTempo:
                            auxiliar.ocuestado = 2

                            '''chec = 0
                            for qlq in auxiliar.vetPrioridade:
                                chec = 0
                                if qlq == "prioridade":
                                    chec = 1
                                else:
                                    pass
                            if chec == 0:
                                auxiliar.vetPrioridade[i] = "prioridade"
                            else:
                                pass'''





