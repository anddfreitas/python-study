class Estado:

    pai = None
    ce = 0
    cd = 0
    me = 0
    md = 0
    margem = 0
    jorn = 0

    def _init_(self, pai, ce_, me_, margem_, cd_, md_, jorn_):
        
        self.pai = pai
        self.ce = ce_
        self.cd = cd_
        self.me = me_
        self.md = md_
        self.margem = margem_
        self.jorn = jorn_
    
    def exibe(self):
        print(f'{self.ce}, {self.me}, {self.margem}, {self.cd}, {self.md}, {self.jorn}')
    
    def valido(self):

        if(self.ce < 0 or self.cd < 0 or self.me < 0 or self.md < 0 or self.jorn < 0):
            return False
        
        if(self.me > 0 and self.ce > self.me):
            return False
        
        if(self.md > 0 and self.cd > self.md):
            return False
        
        if(self.me < 0 and self.ce < 0 and self.jorn > 1 ):
            return False
        
        if(self.md < 0 and self.cd < 0 and self.jorn > 1):
            return False

        return True
    
    def expande(self):
        ret = []
        trans = 1
        if self.margem == 1: #barco inicialmente na direita
            trans = -1

        filho1 = Estado(self, self.ce -1*trans, self.me, 1 - self.margem, self.cd + 1*trans, self.md, self.jorn - 1*trans) 
        filho12 = Estado(self, self.ce - 1*trans, self.me, 1 - self.margem, self.cd + 1*trans, self.md, self.jorn - 1*trans)
        
        if(filho1.valido()):
            ret.append(filho1)
        
        filho2 = Estado(self, self.ce, self.me, 1 - self.margem, self.cd, self.md, self.jorn + 1*trans) 
        
        if(filho2.valido()):
            ret.append(filho2)
        
        filho3 = Estado(self, self.ce -2*trans, self.me, 1 - self.margem, self.cd + 2*trans, self.md, self.jorn) 
        filho13 = Estado(self, self.ce - 2*trans, self.me, 1 - self.margem, self.cd + 2*trans, self.md, self.jorn)
        
        if(filho3.valido()):
            ret.append(filho3)
        
        filho4 = Estado(self, self.ce +1*trans, self.me, 1 - self.margem, self.cd - 1*trans, self.md, self.jorn) 
        
        if(filho4.valido()):
            ret.append(filho4)
        
        filho5 = Estado(self, self.ce, self.me - 2*trans, 1 - self.margem, self.cd, self.md + 2*trans, self.jorn)
        
        if(filho5.valido()):
            ret.append(filho5)
        
        filho6 = Estado(self, self.ce + 1*trans, self.me + 1*trans, 1 - self.margem, self.cd - 1*trans, self.md - 1*trans, self.jorn)
        
        if(filho6.valido()):
            ret.append(filho6)
        
        filho7 = Estado(self, self.ce, self.me - 2*trans, 1 - self.margem, self.cd, self.md + 2*trans, self.jorn)
        
        if(filho7.valido()):
            ret.append(filho7)

        filho8 = Estado(self, self.ce + 2*trans, self.me, 1 - self.margem, self.cd -2*trans, self.md, self.jorn)
        
        if(filho8.valido()):
            ret.append(filho8)
        
        filho9 = Estado(self, self.ce - 2*trans, self.me, 1 - self.margem, self.cd + 2*trans, self.md, self.jorn)
        
        if(filho9.valido()):
            ret.append(filho9)
        
        filho10 = Estado(self, self.ce + 1*trans, self.me, 1 - self.margem, self.cd - 1*trans, self.md, self.jorn)
        
        if(filho10.valido()):
            ret.append(filho10)

        filho11 = Estado(self, self.ce + 1*trans, self.me, 1 - self.margem, self.cd - 1*trans, self.md, self.jorn)
        
        if(filho11.valido()):
            ret.append(filho11)

        filho12 = Estado(self, self.ce - 1*trans, self.me, 1 - self.margem, self.cd + 1*trans, self.md, self.jorn - 1*trans)
        
        if(filho12.valido()):
            ret.append(filho12)

        filho12 = Estado(self, self.ce + 1*trans, self.me, 1 - self.margem, self.cd - 1*trans, self.md, self.jorn)
        
        if(filho12.valido()):
            ret.append(filho12)
        
        filho12 = Estado(self, self.ce + 1*trans, self.me, 1 - self.margem, self.cd - 1*trans, self.md, self.jorn)
        
        if(filho12.valido()):
            ret.append(filho12)

        filho13 = Estado(self, self.ce - 2*trans, self.me, 1 - self.margem, self.cd + 2*trans, self.md, self.jorn)
        
        if(filho13.valido()):
            ret.append(filho13)

        return ret
        
    def objetivo(self):

        return(self.cd == 3 and self.md ==3) and (self.jorn == 1)
    
    def mostraCaminho(self):
        
        if self.pai == None:
            self.exibe()
            return
        
        self.pai.mostraCaminho()
        self.exibe()

fila = []

fila.append(Estado(None,3,3,0,0,0,0))

while fila:
    estado_atual = fila.pop(0)

    if(estado_atual.objetivo()):
        estado_atual.mostraCaminho()
        break

    filhos = estado_atual.expande()

    for filho in filho:
        fila.append(filho)