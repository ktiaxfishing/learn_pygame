
print('start')
class A:
    def __init__(self):
        print('in init')
    def do(self):
        print('do')

print('----')
b = A()
b.do()
b.do()
print('end')
    