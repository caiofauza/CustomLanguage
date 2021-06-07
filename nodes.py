class Function_table():
    def __init__(self):
        self.dict = {}

    def get_function(self, key):
        if(not key.value in self.dict):
            return None
        return self.dict[key.value]

    def get_function_return(self, key):
        if(not key in self.dict):
            return None
        return self.dict[key]

    def set_function(self, key, value):
        if(key in self.dict and key[0] != '!'):
            raise Exception('Function has already been declared')
        self.dict[key] = value


function_table = Function_table()


class Symbol_table():
    def __init__(self):
        self.dict = {}

    def get_symbol(self, key):
        if(not key in self.dict):
            raise Exception('Undefined variable')
        return self.dict[key]

    def set_symbol(self, key, value):
        self.dict[key] = value


class Node():
    def __init__(self, value=None, children=None):
        self.value = value
        self.children = children

    def evaluate(self, symbol_table):
        return


class Func_Dec(Node):
    def __init__(self, value, children):
        super().__init__(value, children)

    def evaluate(self, symbol_table):
        function_table.set_function(self.children[0].children[0], self)


class Func_Call(Node):
    def __init__(self, value, children=[]):
        super().__init__(value, children)

    def evaluate(self, symbol_table):
        function_dec = function_table.get_function(self)
        if(function_dec == None):
            raise Exception('Undefined function')

        parameters = []
        for i in function_dec.children[0].children[1:]:
            parameters.append(i)

        if(len(parameters) != len(self.children)):
            raise Exception('Invalid function parameters size')
        self.symbol_table = Symbol_table()

        for i in range(len(self.children)):
            symbol = parameters[i]
            symbol_result = self.children[i].evaluate(symbol_table)
            self.symbol_table.set_symbol(symbol[0], symbol_result)

        function_dec.children[1].evaluate(self.symbol_table)
        return function_table.get_function_return('!{}_return'.format(self.value))


class Var_Dec(Node):
    def __init__(self, value, children):
        super().__init__(value, children)

    def evaluate(self, symbol_table):
        return


class Statement_Op(Node):
    def __init__(self, value, children):
        super().__init__(value, children)

    def evaluate(self, symbol_table=None):
        for i in self.children:
            i.evaluate(symbol_table)
            if(i.value == 'RETURN'):
                return


class Input_op(Node):
    def __init__(self, value):
        super().__init__(value)

    def evaluate(self, symbol_table):
        return input()


class While_Op(Node):
    def __init__(self, value, children):
        super().__init__(value, children)

    def evaluate(self, symbol_table):
        while (self.children[0].evaluate(symbol_table)):
            self.children[1].evaluate(symbol_table)


class Condition_Op(Node):
    def __init__(self, value, children):
        super().__init__(value, children)

    def evaluate(self, symbol_table):
        if(self.children[0].evaluate(symbol_table)):
            self.children[1].evaluate(symbol_table)
        elif(len(self.children) == 3):
            self.children[2].evaluate(symbol_table)


class Print_op(Node):
    def __init__(self, value, children):
        super().__init__(value, children)

    def evaluate(self, symbol_table):
        print(self.children[0].evaluate(symbol_table))


class Assignment_op(Node):
    def __init__(self, value, children):
        super().__init__(value, children)

    def evaluate(self, symbol_table):
        symbol_table.set_symbol(
            self.children[0].value, self.children[1].evaluate(symbol_table))


class Bin_op(Node):
    def __init__(self, value, children):
        super().__init__(value, children)

    def evaluate(self, symbol_table):
        left = self.children[0].evaluate(symbol_table)
        right = self.children[1].evaluate(symbol_table)

        if(self.value == '+'):
            return int(left+right)
        if(self.value == '-'):
            return int(left-right)
        if(self.value == '*'):
            return int(left*right)
        if(self.value == '/'):
            return int(left/right)
        if(self.value == '>'):
            return int(int(left) > int(right))
        if(self.value == '<'):
            return int(int(left) < int(right))
        if(self.value == '>='):
            return int(int(left) >= int(right))
        if(self.value == '<='):
            return int(int(left) <= int(right))
        if(self.value == '=='):
            return int(int(left) == int(right))
        if(self.value == '!='):
            return int(int(left) == int(right))
        if(self.value == 'and'):
            return int(int(left) and int(right))
        if(self.value == 'or'):
            return int(left) or int(right)


class Un_op(Node):
    def __init__(self, value, children):
        super().__init__(value, children)

    def evaluate(self, symbol_table):
        if(self.value == '+'):
            return self.children[0].evaluate(symbol_table)
        elif(self.value == '-'):
            return int(self.children[0].evaluate(symbol_table)*(-1))
        elif(self.value == '!'):
            return int(not int(self.children[0].evaluate(symbol_table)))


class Int_val(Node):
    def __init__(self, value):
        super().__init__(int(value))

    def evaluate(self, symbol_table):
        return int(self.value)


class Identifier_val(Node):
    def __init__(self, value):
        super().__init__(value)

    def evaluate(self, symbol_table):
        return symbol_table.get_symbol(self.value)


class Bool_val(Node):
    def __init__(self, value):
        super().__init__(value)

    def evaluate(self, symbol_table):
        return True if self.value == 'true' else False


class String_val(Node):
    def __init__(self, value):
        super().__init__(value[1:-1])

    def evaluate(self, symbol_table):
        return str(self.value)


class Return_val(Node):
    def __init__(self, value, children):
        super().__init__(value, children)

    def evaluate(self, symbol_table):
        function_return = self.children[1].evaluate(symbol_table)
        function_table.set_function('!{}_return'.format(
            self.children[0]), function_return)
        return function_return


class No_op(Node):
    def __init__(self, value):
        super().__init__(value)

    def evaluate(self, symbol_table):
        return
