# -*- coding: utf-8 -*-
import datetime
class Veiculo():

    def __init__(self, ocuestado1, marca1, modelo1, ano1, vdiaria1, atraso1, vetDataInicial1, vetDataFinal1, vetnome1,vetestado1):
        self.ocuestado = ocuestado1
        self.marca = marca1
        self.modelo = modelo1
        self.ano = ano1
        self.vdiaria = vdiaria1
        self.atraso = atraso1
        self.vetDataInicial = vetDataInicial1
        self.vetDataFinal = vetDataFinal1
        self.vetNome = vetnome1
        self.vetPrioridade = vetestado1




    def __str__(self):
        return self.modelo




