
class ClassePessoa():
    def __init__(self,nome,peso,idade):
        self.nome = nome    #atributo
        self.peso = peso    #atributo
        self.idade = idade  #atributo
        self.comendo = False
        self.dormindo = False
        self.falando = False
    def Apresentar(self):
        print(f"Olá meu nome é {self.nome} tenho {self.idade} anos "
              f"e peso {self.peso}")

    def Comer(self):
        if self.falando:
            print("Não pode falar enquanto come")
        elif self.dormindo:
            print("Não pode comer dormindo")
        elif self.comendo:
            print("Já está comendo")
        else:
            self.comendo = True
            print(f"{self.nome} começou a comer")


    def Dormir(self):
        if self.falando:
            print("Não pode falar dormindo")
        elif self.comendo:
            print("Não pode comer dormindo")
        elif self.dormindo:
            print("Jã começou a dormir")
        else:
            self.dormindo = True
            print(f"{self.nome} está dormindo")


    def Falar(self):
        if self.comendo:
            print("Não pode comer falando")
        elif self.dormindo:
            print("Não pode falar dormindo")
        elif self.falando:
            print("Jã está falando")
        else:
            self.falando = True
            print(f"{self.nome} está falando")


