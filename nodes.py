class Symbol_table():
    def __init__(self):
        self.dict = {}

    def get_symbol(self, key):
        if(not key in self.dict): raise Exception('Undefined variable')
        return self.dict[key]

    def set_symbol(self, key, value):
        self.dict[key] = value
symbol_table = Symbol_table()

class Node():
    def __init__(self, value = None, children = None):
        self.value = value
        self.children = children
    
    def evaluate(self):
        return

class Statement_Op(Node):
    def __init__(self, value, children):
        super().__init__(value, children)
    
    def evaluate(self):
        for i in self.children:
            i.evaluate()

class Input_op(Node):
    def __init__(self, value):
        super().__init__(value)

    def evaluate(self):
        return input()

class While_Op(Node):
    def __init__(self, value, children):
        super().__init__(value, children)

    def evaluate(self):
        while (self.children[0].evaluate()):
            self.children[1].evaluate()

class Condition_Op(Node):
    def __init__(self, value, children):
        super().__init__(value, children)
    
    def evaluate(self):
        if(self.children[0].evaluate()):
            self.children[1].evaluate()
        elif(len(self.children) == 3):
            self.children[2].evaluate()

class Print_op(Node):
    def __init__(self, value, children):
        super().__init__(value, children)

    def evaluate(self):
        print(self.children[0].evaluate())

class Assignment_op(Node):
    def __init__(self, value, children):
        super().__init__(value, children)

    def evaluate(self):
        symbol_table.set_symbol(self.children[0].value, self.children[1].evaluate())

class Bin_op(Node):
    def __init__(self, value, children):
        super().__init__(value, children)
    
    def evaluate(self):
        if(self.value == '+'):
            return int(self.children[0].evaluate()+self.children[1].evaluate())
        if(self.value == '-'):
            return int(self.children[0].evaluate()-self.children[1].evaluate())
        if(self.value == '*'):
            return int(self.children[0].evaluate()*self.children[1].evaluate())
        if(self.value == '/'):
            return int(self.children[0].evaluate()/self.children[1].evaluate())
        if(self.value == '>'):
            return int(int(self.children[0].evaluate()) > int(self.children[1].evaluate()))
        if(self.value == '<'):
            return int(int(self.children[0].evaluate()) < int(self.children[1].evaluate()))
        if(self.value == '>='):
            return int(int(self.children[0].evaluate()) >= int(self.children[1].evaluate()))
        if(self.value == '<='):
            return int(int(self.children[0].evaluate()) <= int(self.children[1].evaluate()))
        if(self.value == '=='):
            return int(int(self.children[0].evaluate()) == int(self.children[1].evaluate()))
        if(self.value == '!='):
            return int(int(self.children[0].evaluate()) == int(self.children[1].evaluate()))
        if(self.value == 'and'):
            return int(int(self.children[0].evaluate()) and int(self.children[1].evaluate()))
        if(self.value == 'or'):
            return int(self.children[0].evaluate()) or int(self.children[1].evaluate())

class Un_op(Node):
    def __init__(self, value, children):
        super().__init__(value, children)

    def evaluate(self):
        if(self.value == '+'):
            return self.children[0].evaluate()
        elif(self.value == '-'):
            return int(self.children[0].evaluate()*(-1))
        elif(self.value == '!'):
            return int(not int(self.children[0].evaluate()))

class Int_val(Node):
    def __init__(self, value):
        super().__init__(int(value))
    
    def evaluate(self):
        return int(self.value)

class Identifier_val(Node):
    def __init__(self, value):
        super().__init__(value)

    def evaluate(self):
        return symbol_table.get_symbol(self.value)

class Bool_val(Node):
    def __init__(self, value):
        super().__init__(value)
    
    def evaluate(self):
        return True if self.value == 'true' else False

class String_val(Node):
    def __init__(self, value):
        super().__init__(value[1:-1])
    
    def evaluate(self):
        return str(self.value)


class No_op(Node):
    def __init__(self, value):
        super().__init__(value)

    def evaluate(self):
        return