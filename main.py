from biblioteca import *
aluno01 = ClassePessoa ("luna",80,19)

print(aluno01.nome)

aluno01.Dormir()
aluno01.Dormir()
aluno01.Falar()

gato = Gato("Jhonny","cinza")
gato.miar()
gato.comer()

cachorro = Cachorro("Poty","preto")
cachorro.comer()
cachorro.latir()

coelho = Coelho("Mococa","preto")
coelho.comer()
coelho.grunir()

vaca = Vaca("Mimosa","malhada")
vaca.comer()
vaca.mugir()

ingresso = Ingresso(20)
ingresso.imprimirValor()

ingressovip = IngressoVip(20)
ingressovip.imprimirValor()

retangulo = Retangulo(30,70)
retangulo.calculoArea()
retangulo.calculoPerimetro()

triangulo = Triangulo(40,20)
triangulo.calculaArea()
triangulo.calculaPerimetro()
