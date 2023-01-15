class Pessoa:
    olhos=2 #clal attribute or defaul attribute
    def __init__(self,*irmaos,nome=None,idade=32):
            self.nome=nome
            self.irmaos = list(irmaos)
            self.idade = idade
    def retorna_self_id(self):
        return f'Olá {id(self)}' #returns id of the self object
    @staticmethod
    def metodo_estatico(): #o método estático funciona como uma função atrelada à classe pessoa, independe do objeto, não precisa receber atributos
        return 42
    @classmethod
    def nome_e_atributos_de_classe(cls): #método estático usado como queremos acessar dados da própria classe
        return f'{cls} - olhos {cls.olhos}'


if __name__ == '__main__':
    #First Object
    eu = Pessoa()
    print(id(eu)) # prints id of the p object of class Pessoa
    print(eu.retorna_self_id()) #prints id of the self object (the same as the p object)
    eu = Pessoa ('Benicio')
    print(eu.nome)
    eu.nome = 'Luiz Benicio'
    print(eu.nome)

    #Complex attributes
    bia = Pessoa(eu,nome='Tobias',idade=30) #eu is an object of the class Pessoa passed as a parameter
    for irmao in bia.irmaos: 
        print(irmao.nome)
    
    #Changing the object
    bia.sobrenome = 'Degli Esposte' #add attribute
    print(bia.sobrenome) #this attribute is created for this object only

    #Checking all of the attributes of an object:
    print(eu.__dict__)
    print(bia.__dict__) #shows that 'sobrenome' is present in the bia object only

    #Removing attributes
    del eu.irmaos #removes the attrubute of the 'eu' object only

    #Class attributes
    print(Pessoa.olhos) #I can access/print a class attribute from the class
    print(eu.olhos) #I can also access it from any instance of the class
    print(id(Pessoa.olhos),id(eu.olhos)) #the ids are the same
    print(eu.__dict__) # class attributes  do not show on __dict__ of the instances
    eu.olhos = 1 #I can override locally, now it is a new id and it shows on eu.__dict__
    print(eu.__dict__)
    #Python first looks for instance attributes, then parent class attributes,
    del eu.olhos #now eu.olhos returns the class attribute again 

    #Métodos de Classe
    print(Pessoa.metodo_estatico(),eu.metodo_estatico())
    print(eu.nome_e_atributos_de_classe())

    #Herança
    class Homem(Pessoa): #a classe homem herda de pessoa (Pessoa é a classe pai de homem)
        pass
    #a herança inclui todos os métodos e atributos de dados da classe pai
    #tomando a instância 'eu', poderíamos usar a classe Homem ao invés de pessoa
    #ou seja, se alterássemos a linha de eu = Pessoa('Benicio') para eu = Homem('Benicio'), nada mudaria
        
    #checando se um objeto é de determinado tipo: isinstance()
    pessoa = Pessoa('Anonimo')
    print(isinstance(pessoa,Pessoa))
    print(isinstance(pessoa,Homem))
    #Um homem é uma pessoa, mas uma pessoa não necessariamente é um homem
    homem = Homem('Fulano')
    print(isinstance(homem,Pessoa))
    print(isinstance(homem,Homem))


