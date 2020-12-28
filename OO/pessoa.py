class Pessoa:
    def __init__(self, *filhos, nome=None, idade=11):
        self.idade = idade
        self.nome = None
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'"Olá" {id(self)}'
if __name__ == '__main__':
    amanda = Pessoa(nome='felipe')
    felipe = Pessoa(amanda, nome="Felipe")
    print(Pessoa.cumprimentar(felipe))
    print(id(felipe))
    print(felipe.cumprimentar())
    print(felipe.nome)
    print(felipe.idade)
    for filho in felipe.filhos:
         print(filho.nome)