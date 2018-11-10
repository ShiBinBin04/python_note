class Stu():
    def __init__(self, name='haha', age=18):
        self.name = name
        self.age = age

    def sayhello(self):
        print('i am {0} and i am {1} years old.'.format(self.name, self.age))


def func():
    print('i am module001')

print('hello,everyone')