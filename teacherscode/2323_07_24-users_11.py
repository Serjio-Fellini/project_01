# Наследование

# класс-модель User

# родительский класс
class User:
    '''Модель пользователя'''

    active = True

    def __init__(self, name=None) -> None:
        self.name = name
        self.gid = 1000
        self.get_permissions(7, 0, 0)
    
    def __str__(self):
        return f'{self.__class__.__name__}, id({self.gid}), status({"Active" if self.active else "Dead"})'

    def get_permissions(self, *args):
        self.u, self.g, self.o = args
        return self.u, self.g, self.o

    def check_permissions(self):
        print(f'Права: {self.u}, {self.g}, {self.o}')




# дочерний класс
class Guest(User):
    '''Гость'''


# дочерний класс
class Admin(User):
    '''Администратор'''

    def __init__(self, name=None) -> None:
        super().__init__(name)
        self.get_permissions(7, 6, 4)


# Инкапсуляция
# дочерний класс
class Root(User):
    '''Суперпользователь'''

    active = False

    def __init__(self, token, name=None) -> None:
        super().__init__(name)
        self.gid = 0
        self.__token = token
        # print(self.__token)  # работает внутри класса
        self.get_permissions(7, 7, 7)

# Множественное наследование
class RemoteDesktop:
    '''Удаленный доступ РС'''
    def __str__(self) -> str:
        return 'Подключение к РС'

class RemoteDesktopUser(RemoteDesktop, User):
    pass


# Пример
# class DB:

#     class __PrimaryKey:
#         def __init__(self) -> None:
#             pass
    
#     PK = __PrimaryKey()

#     def __init__(self) -> None:
#         self.COLUMN1 = 1
#         self.COLUMN2 = 2
        


print('Сэм')
acc1 = Admin(name='Сэм')
print(acc1)
acc1.check_permissions()

print('Радж')
acc2 = Guest(name='Радж')
print(acc2)
acc2.check_permissions()

print('Суперпользователь')
acc0 = Root(123456789)
print(acc0)
acc0.check_permissions()
print(acc0.__token)


