'''Criar uma classe carro que vai possuir dois atributos compostos por outras duas classes

- Motor
- Direção

O motor será responsável por controlar a velocidade. Ele oferece os seguintes atributos:
1) Atributo de dado velocidade
2) Método acelerar, que deverá incrementar a velocidade de uma unidade
3) Método frear, que deverá decrementar a velocidade em duas unidades

A direção terá a responsabilidade de controlar a direção. Ela oferece os seguintes atributos:
1) Valor de direção com valores possíveis:Norte, Sul, Leste, Oeste
2) Método girar à direita, N->L->S->O->N
3) Método girar à esquerda (sentido oposto)


Exemplo:
#Testando motor
>>> motor = Motor()
>>> motor.velocidade
0
>>> motor.acelerar()
>>> motor.velocidade
1
>>> motor.acelerar()
>>> motor.velocidade
2
>>> motor.acelerar()
>>> motor.velocidade
3
>>> motor.frear()
>>> motor.velocidade
1
>>> motor.frear()
>>> motor.velocidade
0

#Testando direção

>>> direcao = Direcao()
>>> direcao.valor
'Norte'
>>> direcao.girar_a_direita()
>>> direcao.valor
'Leste'
>>> direcao.girar_a_direita()
>>> direcao.valor
'Sul'
>>> direcao.girar_a_direita()
>>> direcao.valor
'Oeste'
>>> direcao.girar_a_esquerda()
>>> direcao.valor
'Sul'
>>> direcao.girar_a_esquerda()
>>> direcao.valor
'Leste'
>>> direcao.girar_a_esquerda()
>>> direcao.valor
'Norte'
>>> direcao.girar_a_esquerda()
>>> direcao.valor
'Oeste'
>>> carro = Carro(motor,direcao)
>>> carro.calcular_velocidade()
0
>>> carro.acelerar()
>>> carro.calcular_velocidade()
1
>>> carro.acelerar()
>>> carro.calcular_velocidade()
2
>>> carro.frear()
>>> carro.calcular_velocidade()
0
>>> carro.calcular_direcao()
'Oeste'
>>> carro.girar_a_direita()
>>> carro.calcular_direcao()
'Norte'
>>> carro.girar_a_direita()
>>> carro.calcular_direcao()
'Leste'
>>> carro.girar_a_esquerda()
>>> carro.calcular_direcao()
'Norte'
>>> carro.girar_a_esquerda()
>>> carro.calcular_direcao()
'Oeste'

'''
NORTE = 'Norte'
SUL = 'Sul'
OESTE = 'Oeste'
LESTE = 'Leste'
class Motor:
    def __init__(self):
        self.velocidade = 0
    def acelerar(self):
        self.velocidade +=1
    def frear(self):
        self.velocidade-=2
        self.velocidade = max(0,self.velocidade)
        
class Direcao:
    def __init__(self):
        self.valor=NORTE
    def girar_a_direita(self):
        if self.valor == NORTE:
            self.valor = LESTE
        elif self.valor == LESTE:
            self.valor = SUL
        elif self.valor == SUL:
            self.valor = OESTE
        elif self.valor == OESTE:
            self.valor = NORTE
        else:
            print("O carro se perdeu, direção desconhecida.")
    def girar_a_esquerda(self):
        if self.valor == NORTE:
            self.valor = OESTE
        elif self.valor == OESTE:
            self.valor = SUL
        elif self.valor == SUL:
            self.valor = LESTE
        elif self.valor == LESTE:
            self.valor = NORTE
        else:
            print("O carro se perdeu, direção desconhecida.")
class Carro:
    def __init__(self,motor,direcao):
        self.motor = motor
        self.direcao = direcao
    def calcular_velocidade(self):
        return self.motor.velocidade
    def acelerar(self):
        return self.motor.acelerar()
    def frear(self):
        return self.motor.frear()
    def calcular_direcao(self):
        return self.direcao.valor
    def girar_a_direita(self):
        return self.direcao.girar_a_direita()
    def girar_a_esquerda(self):
        return self.direcao.girar_a_esquerda()

motor = Motor()
direcao = Direcao()
c = Carro(motor,direcao) 
print(c.motor.velocidade,c.direcao.valor)


if __name__=='__main__':
    import doctest
    doctest.testmod() #test the whole module
   
  