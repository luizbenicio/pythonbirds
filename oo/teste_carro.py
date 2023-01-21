from unittest import TestCase
from carro import Motor

class CarroTestCase(TestCase):
    def teste_velocidade_inicial(self): #precisa começar com 'test'
        motor=Motor()
        self.assertEqual(0,motor.velocidade) #esses métodos assert são herdados da classe TestCase (valor esperado, valor obtido)
        
        