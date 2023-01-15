class Pessoa:
    def __init__(self,*irmaos,nome=None,idade=32):
            self.nome=nome
            self.irmaos = list(irmaos)
            self.idade = idade
    def retorna_self_id(self):
        return f'Olá {id(self)}' #returns id of the self object

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

    







