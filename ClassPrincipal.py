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
            else:
                estado = "Alugado"
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
        self.vetquant.append(Veiculo(0, marca, modelo, ano, diaria, 0, 0))

    #def addveiculoAlugado(self, veiculonumero, nome, dalugado):
     #   aux = VeiculoAlugado(1 ,nome ,dalugado)
      #  self.vetquantAlu.append(aux)
       # self.vetquant[veiculonumero].ocuestado = 1

    '''
    def consultarVeiculosAlugados(self):
       cont = 0
       for i in self.vetquantAlu:
            cont += 1
            print(cont, "-", i)
       else:
            print("---------")
'''
    def devolverVeiculo(self,numeroveiculo):
        del(self.vetquantAlu[numeroveiculo])


    def mudarData(self,novoTempo):
        for auxiliar in self.vetquant:
            if auxiliar.dataEntrega == 0:
                pass
            else:
                if novoTempo <= auxiliar.dataInicial:
                    auxiliar.atraso = 1
