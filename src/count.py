"""
简易计算器
"""


class Count:
    result_msg = ''
    '''
        加法运算
    '''

    def add(self, value: int):
        self.result_msg += '+' + value.__str__()

    '''
        减法运算
    '''

    def subtract(self, value: int):
        self.result_msg += '-' + value.__str__()

    '''
        乘法运算
    '''

    def multiply(self, value: int):
        self.result_msg += '*' + value.__str__()

    '''
        除法运算
    '''

    def divide(self, value: int):
        self.result_msg += '/' + value.__str__()

    '''
        利用eval进行运算，并返回结果
    '''

    def result(self):
        return eval(self.result_msg)
