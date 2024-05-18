class Pessoa():
    def __init__(self, nomeAluno, pesoAluno, idadeAluno, comendo = False, falando=False, dormindo=False):
        self.nome = nomeAluno
        self.peso = pesoAluno
        self.idade = idadeAluno
        self.dormindo = dormindo
        self.falando = falando
        self.comendo = comendo

    def comer(self, comida):
        if self.dormindo == False and self.falando == False:
            if self.comendo == False:
                self.comendo = True
                print(f"{self.nome} comeu {comida}")
            else:
                print(f"{self.nome} já está comendo")
        elif self.dormindo == True:
            print(f"{self.nome} não pode comer pois está dormindo")
        elif self.falando == True:
            print(f"{self.nome} não pode falar pois esta comendo {comida}")

    def pararComer(self,comida):
        if self.comendo == True:
            self.comendo = False
            print(f"{self.nome} parou de comer {comida}")
        else:
            print(f"{self.nome} não estava falando")

    def falar(self, fala):
        if self.dormindo == False and self.comendo == False:
            if self.falando == False:
                self.falando = True
                print(f"{self.nome} falou {fala}")
            else:
                print(f"{self.nome} já está falando")
        elif self.comendo == True:
            print(f"{self.nome} não pode falar pois está comendo")
        elif self.dormindo == True:
            print(f"{self.nome} não pode falar pois está dormindo")

    def pararFalar(self, fala):
        if self.falando == True:
            self.falando = False
            print(f"{self.nome} parou de falar{fala}")
        else:
            print(f"{self.nome} não estava falando")

    def dormir(self):
        if self.falando == False and self.comendo == False:
            if self.dormindo == False:
                self.dormindo = True
            else:
                print(f"{self.nome} já está dormindo zZz")
        elif self.comendo == True:
            print(f"{self.nome} não pode dormir porque está comendo")
        elif self.falando == True:
            print(f"{self.nome} não pode dormir porque está falando")

    def pararDormir(self):
        if self.dormindo == True:
            self.dormindo = False
            print(f"{self.nome} parou de dormir zZz")
        else:
            print(f"{self.nome} não está dormindo")

