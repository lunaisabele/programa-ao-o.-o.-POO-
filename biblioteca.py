
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
#________________________________________________________________________________
class Animal():
    def __init__(self,nome,cor):
        self.nome = nome
        self.cor = cor

    def comer(self):
        print (f"O {self.nome} foi comer...")

class Gato(Animal):
    def __init__(self,nome,cor):
        super().__init__(nome,cor)

    def miar(self):
        print(f"O {self.nome} foi miar...")

class Cachorro(Animal):
    def __init__(self,nome,cor):
        self.nome = nome
        self.cor = cor

    def comer(self):
        print(f"{self.nome} foi comer...")

    def latir(self):
        print(f"{self.nome} foi latir...")

class Coelho(Animal):
    def __init__(self,nome,cor):
        self.nome = nome
        self.cor = cor

    def comer(self):
        print(f"{self.nome} foi comer...")

    def grunir(self):
        print(f"{self.nome} foi grunir...")


class Vaca(Animal):
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor

    def comer(self):
        print(f"{self.nome} foi comer...")

    def mugir(self):
        print(f"{self.nome} foi mugir...")

class Ingresso:
    def __init__(self,valor):
        self.valor = valor

    def imprimirValor(self):
        print(f"O valor do ingresso é: R${self.valor}")


class IngressoVip(Ingresso):
    def __init__(self,valor):
        super().__init__(valor*1.5)


class Forma():
    def __init__(self):
        self.area = 0
        self.perimetro = 0

class Retangulo(Forma):
    def __init__(self,base,altura):
        self.base = base
        self.altura = altura


    def calculoArea(self):
        self.area = (self.base * self.altura)
        print(f"A area do retango é: {self.area}")


    def calculoPerimetro(self):
        self.perimetro = (2*self.base + self.altura)
        print(f"O perimetro do retangulo é: {self.altura}")


class Triangulo(Forma):
    def __init__(self,altura,base):
       self.altura = altura
       self.base = base

    def calculaArea(self):
        self.area = (self.base * self.altura/2)

    def calculaPerimetro(self):
        self.altura = (self.base*3)











