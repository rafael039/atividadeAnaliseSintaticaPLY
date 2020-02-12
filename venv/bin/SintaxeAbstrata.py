# classe abstrada

from abc import abstractmethod
from abc import ABCMeta

class Exp(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
        pass

# classe concreta

class SomaExp(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, Visitor):
        Visitor.visitSomaExp(self)

class MulExp(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, Visitor):
        Visitor.visitMulExp(self)

class PotExp(Exp):
    def __init__(self,exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, Visitor):
        Visitor.visitPotExp(self)

class ChamadaExp(Exp):
    def __init__(self, call):
        self.call = call
    def accept(self, Visitor):
        Visitor.visitChamadaExp(self)

class ChamadaParamExp(Exp):
    def __init__(self, call, id, params):
        self.call = call
        self.id = id
        self.params = params
    def accept(self, Visitor):
        Visitor.visitChamadaParamExp(self)

class AtribuicaoExp(Exp):
    def __init__(self, assign, id, exp):
        self.assign=assign
        self.id=id
        self.exp=exp
    def accept(self, Visitor):
        Visitor.visitAtribuicaoExp(self)