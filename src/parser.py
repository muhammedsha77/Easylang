import ply.yacc as yacc
from lexer import Mylexer

#lexer build
easylanglexer=Mylexer()
easylanglexer.build()

#token
tokens=easylanglexer.tokens

#Ast Node classes



class programnode:
    def __init__(self,statement):
        self.statement=statement
    def __repr__(self):
        return f"program ({self.statement})"


class declarationnode:
    def __init__(self,identifier,exprs):
        self.identifier=identifier
        self.exprs=exprs
    def __repr__(self):
        return f"declaritionnode({self.identifier} {self.exprs})"

class identifiernode:
    def __init__(self,name):
        self.name=name

    def __repr__(self):
        return f"indentifier({self.name})"

class Binaryopnode:
    def __init__(self,leftpart,op,rightpart):
        self.leftpart= leftpart
        self.op=op
        self.rightpart=rightpart

    def __repr__(self):
        return f"Binaryopnode({self.leftpart} {self.op} {self.rightpart})"


class Numbernode:

    def __init__(self,value):
        self.value=value

    def __repr__(self):
        return f"Numbernode({self.value})"



class Returnode:

    def __init__(self,exp):
        self.exp=exp
    def __repr__(self):
        return f"Returnnode({self.exp})"

class ifNode:
    def __init__(self,condition,thenblock,elseblock):
        self.condition=condition
        self.thenblock=thenblock
        self.elseblock=elseblock
    def __repr__(self):
        return f"ifNode({self.condition},{self.thenblock},{self.elseblock})"

class WhileNode:
    def __init__(self,condition,body):
        self.condition=condition
        self.body=body
    def __repr__(self):
        return f"whilenode({self.condition} {self.body})"



if __name__ == "__main__":
    binaryinstance=Binaryopnode(5,'+',6)
    print(binaryinstance)







